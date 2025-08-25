from django.shortcuts import render,redirect
from .models import Tour
from .forms import ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib.auth.models import User 




def home_view(request):
    form = ContactForm()
    tours= Tour.objects.all()
    context = {
        'tours':tours,
        'form':form
    }
    return render(request, 'tours/home.html',context) 

#Define the contact_view function to handle

def contact_view(request):
    if request.method=="POST":
         form= ContactForm(request.POST)
         if form.is_valid():
             form.send_email()
             return redirect('contact-sucess')
    else:
        form= ContactForm()

    context={
        'form':form
    }
    return render(request, 'tours/contact.html',context)  
        
   
#define the contact_sucess view to render the contact_sucess.html template

def contact_sucess_view(request):
    return render(request, 'tours/contact_success.html')

def hot_deals_view(request):
    """View to display only hot deals"""
    hot_deals = Tour.objects.filter(is_hot_deal=True).order_by('-discount')
    
    context = {
        'tours': hot_deals,
        'category': 'hot_deals',
        'page_title': 'Hot Deals',
    }
    return render(request, 'tours/tours_grid.html', context)

def data_views(request):
    category = request.GET.get('category', 'all')
    
    # Create sample data if no tours exist
    if Tour.objects.count() == 0:
        create_sample_tours()
    
    # Filter tours based on category
    if category == 'all':
        tours = Tour.objects.all()
    else:
        tours = Tour.objects.filter(category=category)
    
    # Get hot deals (random 3 tours with discount)
    hot_deals = Tour.objects.filter(is_hot_deal=True).order_by('?')[:3]
    
    context = {
        'tours': tours,
        'category': category,
        'hot_deals': hot_deals,
    }
    return render(request, 'tours/tours_grid.html', context)

def create_sample_tours():
    # Economic Tours
    Tour.objects.create(
        title='Bangkok Budget Getaway',
        description='Explore the vibrant streets of Bangkok with our budget-friendly package.',
        origin_country='India',
        destination_country='Thailand',
        number_of_nights=4,
        price=19999,
        category='economic',
        is_hot_deal=True,
        discount=15,
        image_url='https://source.unsplash.com/random/600x400/?bangkok'
    )
    
    # Moderate Tours
    Tour.objects.create(
        title='Bali Paradise Escape',
        description='Experience the beauty of Bali with our comfortable mid-range package.',
        origin_country='India',
        destination_country='Indonesia',
        number_of_nights=5,
        price=49999,
        category='moderate',
        is_hot_deal=True,
        discount=10,
        image_url='https://source.unsplash.com/random/600x400/?bali'
    )
    
    # Luxury Tours
    Tour.objects.create(
        title='Maldives Luxury Retreat',
        description='Indulge in ultimate luxury with our exclusive Maldives package.',
        origin_country='India',
        destination_country='Maldives',
        number_of_nights=6,
        price=149999,
        category='luxury',
        is_hot_deal=True,
        discount=20,
        image_url='https://source.unsplash.com/random/600x400/?maldives'
    )
    
    # Add more sample tours...
    sample_tours = [
        {
            'title': 'Singapore City Tour',
            'description': 'Discover the modern marvels of Singapore.',
            'destination_country': 'Singapore',
            'nights': 3,
            'price': 39999,
            'category': 'moderate'
        },
        {
            'title': 'Dubai Extravaganza',
            'description': 'Experience the luxury and opulence of Dubai.',
            'destination_country': 'UAE',
            'nights': 5,
            'price': 89999,
            'category': 'luxury'
        },
        {
            'title': 'Nepal Adventure',
            'description': 'Trek through the beautiful landscapes of Nepal.',
            'destination_country': 'Nepal',
            'nights': 7,
            'price': 24999,
            'category': 'economic'
        }
    ]
    
    for tour in sample_tours:
        Tour.objects.create(
            title=tour['title'],
            description=tour['description'],
            origin_country='India',
            destination_country=tour['destination_country'],
            number_of_nights=tour['nights'],
            price=tour['price'],
            category=tour['category'],
            image_url=f'https://source.unsplash.com/random/600x400/?{tour["destination_country"].lower()}'
        )

# --- Cost Tier Data (static mapping for demo) ---
COST_TIER_DATA = [
    {"orgin_country": "Japan", "destination_country": "China", "number_of_nights": 10, "mode_of_transport": "Flight", "economic": 180, "moderate": 350, "luxury": 600},
    {"orgin_country": "India", "destination_country": "S. Korea", "number_of_nights": 8, "mode_of_transport": "Flight", "economic": 260, "moderate": 500, "luxury": 850},
    {"orgin_country": "Malaysia", "destination_country": "Korea", "number_of_nights": 13, "mode_of_transport": "Flight", "economic": 320, "moderate": 600, "luxury": 920},
    {"orgin_country": "India", "destination_country": "Sri Lanka", "number_of_nights": 9, "mode_of_transport": "Flight / Ferry", "economic": 100, "moderate": 230, "luxury": 480},
    {"orgin_country": "India", "destination_country": "France", "number_of_nights": 7, "mode_of_transport": "Flight", "economic": 600, "moderate": 950, "luxury": 1400},
    {"orgin_country": "USA", "destination_country": "Japan", "number_of_nights": 10, "mode_of_transport": "Flight", "economic": 750, "moderate": 1100, "luxury": 1700},
    {"orgin_country": "UK", "destination_country": "Australia", "number_of_nights": 14, "mode_of_transport": "Flight", "economic": 800, "moderate": 1200, "luxury": 1800},
    {"orgin_country": "Canada", "destination_country": "Italy", "number_of_nights": 8, "mode_of_transport": "Flight", "economic": 690, "moderate": 1050, "luxury": 1500},
    {"orgin_country": "Germany", "destination_country": "Thailand", "number_of_nights": 6, "mode_of_transport": "Flight", "economic": 450, "moderate": 700, "luxury": 1100},
    {"orgin_country": "Brazil", "destination_country": "South Africa", "number_of_nights": 9, "mode_of_transport": "Flight", "economic": 600, "moderate": 950, "luxury": 1350},
    {"orgin_country": "Australia", "destination_country": "Switzerland", "number_of_nights": 7, "mode_of_transport": "Flight", "economic": 750, "moderate": 1100, "luxury": 1600},
    {"orgin_country": "UAE", "destination_country": "Turkey", "number_of_nights": 5, "mode_of_transport": "Flight", "economic": 200, "moderate": 400, "luxury": 700},
    {"orgin_country": "Singapore", "destination_country": "New Zealand", "number_of_nights": 12, "mode_of_transport": "Flight", "economic": 550, "moderate": 850, "luxury": 1200},
    {"orgin_country": "South Korea", "destination_country": "Vietnam", "number_of_nights": 4, "mode_of_transport": "Flight", "economic": 160, "moderate": 300, "luxury": 500},
    {"orgin_country": "Russia", "destination_country": "Egypt", "number_of_nights": 6, "mode_of_transport": "Flight", "economic": 400, "moderate": 700, "luxury": 1000},
    {"orgin_country": "China", "destination_country": "Maldives", "number_of_nights": 5, "mode_of_transport": "Flight", "economic": 480, "moderate": 750, "luxury": 1150},
    {"orgin_country": "Japan", "destination_country": "Canada", "number_of_nights": 8, "mode_of_transport": "Flight", "economic": 820, "moderate": 1300, "luxury": 1800},
    {"orgin_country": "Mexico", "destination_country": "Spain", "number_of_nights": 9, "mode_of_transport": "Flight", "economic": 700, "moderate": 1050, "luxury": 1500},
    {"orgin_country": "Netherlands", "destination_country": "India", "number_of_nights": 10, "mode_of_transport": "Flight", "economic": 600, "moderate": 950, "luxury": 1400},
    {"orgin_country": "Argentina", "destination_country": "Portugal", "number_of_nights": 7, "mode_of_transport": "Flight", "economic": 700, "moderate": 1050, "luxury": 1500},
    {"orgin_country": "Indonesia", "destination_country": "Sri Lanka", "number_of_nights": 6, "mode_of_transport": "Flight / Ferry", "economic": 120, "moderate": 250, "luxury": 500},
    {"orgin_country": "UK", "destination_country": "Morocco", "number_of_nights": 5, "mode_of_transport": "Flight", "economic": 190, "moderate": 350, "luxury": 600},
    {"orgin_country": "USA", "destination_country": "Greece", "number_of_nights": 8, "mode_of_transport": "Flight", "economic": 750, "moderate": 1150, "luxury": 1700},
    {"orgin_country": "India", "destination_country": "Singapore", "number_of_nights": 4, "mode_of_transport": "Flight", "economic": 200, "moderate": 400, "luxury": 700},
]

def get_cost_tier_data(tour):
    for entry in COST_TIER_DATA:
        if (entry["orgin_country"].lower() == tour.orgin_country.lower() and
            entry["destination_country"].lower() == tour.destination_country.lower() and
            entry["number_of_nights"] == tour.number_of_nights):
            return entry
    return None

def cost_tier_select_view(request, tour_id):
    from .models import Tour
    tour = Tour.objects.get(id=tour_id)
    data = get_cost_tier_data(tour)
    context = {
        'tour_id': tour.id,
        'orgin_country': tour.orgin_country,
        'destination_country': tour.destination_country,
        'number_of_nights': tour.number_of_nights,
        'mode_of_transport': data['mode_of_transport'] if data else 'N/A',
    }
    return render(request, 'tours/cost_select.html', context)

def cost_tier_detail_view(request, tour_id, tier):
    from .models import Tour
    tour = Tour.objects.get(id=tour_id)
    data = get_cost_tier_data(tour)
    if not data:
        context = {
            'orgin_country': tour.orgin_country,
            'destination_country': tour.destination_country,
            'number_of_nights': tour.number_of_nights,
            'mode_of_transport': 'N/A',
            'economic': 'N/A',
            'moderate': 'N/A',
            'luxury': 'N/A',
        }
    else:
        context = {
            'orgin_country': tour.orgin_country,
            'destination_country': tour.destination_country,
            'number_of_nights': tour.number_of_nights,
            'mode_of_transport': data['mode_of_transport'],
            'economic': data['economic'],
            'moderate': data['moderate'],
            'luxury': data['luxury'],
        }
    # Only show the selected tier as active
    if tier == 'economic':
        context['economic'] = context['economic']
        context['moderate'] = '---'
        context['luxury'] = '---'
    elif tier == 'moderate':
        context['moderate'] = context['moderate']
        context['economic'] = '---'
        context['luxury'] = '---'
    elif tier == 'luxury':
        context['luxury'] = context['luxury']
        context['economic'] = '---'
        context['moderate'] = '---'
    context['tier'] = tier.capitalize()
    return render(request, 'tours/cost_tiers.html', context)

from .forms import RegisterForm

from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # This will handle password hashing
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('tours:login')  # Redirect to login page after successful registration
    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }
    return render(request, 'tours/register.html', context)
def login_view(request):
    if request.user.is_authenticated:
        return redirect('tours:home')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Try to authenticate with email or username
        user = None
        if '@' in username:  # If input looks like an email
            try:
                user = User.objects.get(email=username)
                user = authenticate(username=user.username, password=password)
            except User.DoesNotExist:
                pass
        
        # If not authenticated with email, try with username
        if user is None:
            user = authenticate(username=username, password=password)
            
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'tours:home'
            return redirect(next_url)
        else:
            error = 'Invalid username/email or password'
            return render(request, 'accounts/login.html', {'error': error})
            
    return render(request, 'accounts/login.html')

def logout_view(request):
    if request.method =='POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('tours:home')

@login_required
def home_view(request):
    return render(request, 'tours/home.html')

# protected view
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    
    def get(self, request):
        return render(request, 'registration/protected.html')