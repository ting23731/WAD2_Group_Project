from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from artyParty.models import Piece

#maybe rename this or homepage to have the same name?
def home(request):
    # top 4 pieces ordered by popularity
    # change template to display them line 11


    #need to figure out how to sort by rating
    piece_list = Piece.objects.order_by('-piece_id')[:4]

    context_dict = {}

    context_dict['pieces'] = piece_list



    return render(request, 'artyParty/homepage.html', context=context_dict)


def login(request):
    # can we copy from rango?

    ############################################################################
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return redirect(reverse('artyParty:homepage.html'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your artyParty account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'artyParty/login.html')
    ############################################################################


def sign_up(request):

    ############################################################################
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user



            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors, profile_form.errors)
    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request, 'artyParty/sign_up.html', context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
    ############################################################################


def about(request):
    context_dict = {}
    # no real need for context come back to
    #

    return render(request, 'artyParty/about.html', context=context_dict)


def contact_us(request):
    # what happens to submitted form? -> maybe put into db?
    # redirect to homepage
    context_dict = {}

    return render(request, 'artyParty/contact_us.html', context=context_dict)

@login_required
def my_account(request):
    # @loginrequired decorator
    #
    context_dict = {}



    #context_dict[''] =

    return render(request, 'artyParty/myaccount.html', context=context_dict)


@login_required
def add_piece(request):
    # take from rango
    context_dict = {}

    return render(request, 'artyParty/add_pieces.html', context=context_dict)


@login_required
def add_gallery(request):
    # from rango
    context_dict = {}

    return render(request, 'artyParty/add_galleries.html', context=context_dict)



@login_required
def manage_users(request):
    # for power users
    context_dict = {}

    return render(request, 'artyParty/manage_users.html', context=context_dict)


@login_required
def edit_details(request):
    # ???????

    #needs template
    return HttpResponse("Edit details")


def posts(request):
    # what is this posts page about? Is this where we post info?

    context_dict = {}

    return render(request, 'artyParty/post.html', context=context_dict)

    # res = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/Christ_of_Saint_John_of_the_Cross")
    # data = res.json()
    # context_dict = {'descript': data['extract']}
    # return render(request, "View Posts", context_dict)

# CATEGORIES MAYBE ADD LATER, BUT LIKE FUCK THAT RN - james

def category(request):
    # show all pieces in given category
    # query db for pieces where category == passed value


    #needs template
    return HttpResponse("Category (is)")


@login_required
def add_category(request):

    #needs template
    return HttpResponse("Add Category")

def show_category(request):

    #needs template
    return HttpResponse("Add Piece")


def galleries(request):
    # querey db for all pieces where gallery == passed val
    #
    context_dict = {}

    return render(request, 'artyParty/galleries.html', context=context_dict)



def show_gallery(request):
    ## see rango show_category
    context_dict = {}

    return render(request, 'artyParty/pieces.html', context=context_dict)



def show_piece(request):
    ## see rango show_category
    context_dict = {}

    # return render(request, 'artyParty/post.html', context=context_dict)

    res = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/Christ_of_Saint_John_of_the_Cross")
    data = res.json()
    context_dict = {'descript': data['extract']}
    # return render(request, "View Posts", context_dict)

    return render(request, 'artyParty/post.html', context=context_dict)



def show_review(request):
    ## see rango show_category

    #which template is this?
    return HttpResponse("Showing Review")

