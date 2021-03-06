from django.shortcuts import render, render_to_response
from django.template import RequestContext
from match.forms import UserForm, UserProfileForm, MatchRequestForm
from match.models import MatchRequest


def join_match(request):

    context = RequestContext(request)        
    requests = MatchRequest.objects.filter().count() 
    
    if request.method == 'POST':
    
        matchRequest_form = MatchRequestForm(data=request.POST)

        if matchRequest_form.is_valid():

            #if there is already a match request from another player
            # then make a match
            

            matchRequest = matchRequest_form.save()

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(matchRequest_form.errors)

    else:
        matchRequest_form = MatchRequestForm()

    return render_to_response(
            'match_request.html',
            {'matchRequest_form': matchRequest_form, 'requests': requests},
            context)

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def home_page(request):
	return render(request, 'home.html', {
        'new_username': request.POST.get('username', ''),
    })