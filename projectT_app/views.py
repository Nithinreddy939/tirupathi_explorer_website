from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Tirupathi_data_collection
# Create your views here.

def index(request):
    return render(request, 'index.html')
# @login_required(login_url='signin')
def about(request):
    return render(request, 'about.html')
# @login_required(login_url='signin')
def all_items(request,pk):
    # list all food items (reuse template `all_items.html` or `items.html`)
    food_items = Tirupathi_data_collection.objects.filter(name=pk)
    # food_items = Tirupathi_data_collection.objects.all()
    context = {
        'food_items': food_items,
    }
    return render(request, 'all_items.html', context)

def street_food(request):
    # Query all food items and derive categories from the category integer field.
    # Assumption: `category` is stored as an integer and different integers map to category names.
    # Build a simple category list from existing items.
    food_items = Tirupathi_data_collection.objects.all()
    # Build categories as unique ints with a simple name (you may replace with a real Category model later)
    category_ids = food_items.values_list('category', flat=True).distinct()
    categories = []
    for cid in category_ids:
        categories.append({'id': cid, 'name': f'Category {cid}'})

    context = {
        'food_items': food_items,
        'categories': categories,
    }
    return render(request,'street_food.html', context)


def item_detail(request, pk):
    # simple detail view for a food item
    item = Tirupathi_data_collection.objects.filter(pk=pk).first()
    if not item:
        messages.error(request, 'Item not found')
        return redirect('street_food')
    return render(request, 'all_items.html', {'food_items': [item]})

# login and signup pages
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request,username=username, password=password)
        if user is None:
            user = User.objects.filter(username=username).first()
            if user is not None and not user.check_password(password):
                error_message = "Incorrect password."
                return render(request, 'signin.html', {'error_message': error_message})
            else:
                error_message = "User does not exist."
        # Check if the user exists and the password is correct

        if user is not None:
            auth.login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('index')
        else:
            error_message = "Invalid username or password."
            return render(request, 'signin.html', {'error_message': error_message})
    return render(request, 'signin.html')
def signup(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        Password = request.POST.get('password1')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            error_message = "Username already exists."
            return render(request, 'signup.html', {'error_message': error_message})
        else:
            user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=Password,
                )
            User
            messages.success(request, "Account created successfully! Please sign in.")
            return redirect('signin')
    else:
        return render(request, 'signup.html')
    

#myprofile page
def profile(request):
    return render(request, 'profile.html')
#settings page
def setting(request):
    return render(request,'setting.html')
    
def signout(request):
    auth.logout(request)
    return redirect('/')
# cart pages
def cart(request):
    return render(request, 'cart.html')

# Temples pages
# @login_required(login_url='signin')
def famous_temples(request):
    return render(request, 'famous_temples.html')
def temple_1(request):
    return render(request, 'temples/Sri_Venkateswara_Temple.html')
def temple_2(request):
    return render(request, 'temples/sri_padmavathi_temple.html')
def temple_3(request):
    return render(request, 'temples/govindhrajula_temple.html')
def temple_4(request):
    return render(request, 'temples/kapileswara_temple.html')
def temple_5(request):
    return render(request, 'temples/sri_kalyana_venkateswara_temple.html')