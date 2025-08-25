from django.core.management.base import BaseCommand
from asiantoursagency.models import Tour
import random

class Command(BaseCommand):
    help = 'Load luxury tour data into the database'

    def handle(self, *args, **kwargs):
        # Clear existing luxury tours
        Tour.objects.filter(category='luxury').delete()
        
        # All luxury tours data
        luxury_tours = [
            {
                'title': 'Bangkok Luxury Getaway',
                'origin_country': 'Mumbai',
                'destination_country': 'Bangkok, Thailand',
                'number_of_nights': 5,
                'price': 126000,
                'description': 'Experience the vibrant city of Bangkok with luxury accommodations and exclusive experiences.',
                'image_url': 'https://source.unsplash.com/random/800x600/?bangkok-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Singapore Premium Experience',
                'origin_country': 'Delhi',
                'destination_country': 'Singapore',
                'number_of_nights': 4,
                'price': 190000,
                'description': 'Discover the modern marvels of Singapore with premium accommodations and VIP experiences.',
                'image_url': 'https://source.unsplash.com/random/800x600/?singapore-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Tokyo Luxury Adventure',
                'origin_country': 'Bengaluru',
                'destination_country': 'Tokyo, Japan',
                'number_of_nights': 7,
                'price': 422000,
                'description': 'Immerse yourself in the unique blend of traditional and modern Japan with our luxury tour.',
                'image_url': 'https://source.unsplash.com/random/800x600/?tokyo-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Andaman Island Retreat',
                'origin_country': 'Chennai',
                'destination_country': 'Port Blair, Andaman',
                'number_of_nights': 6,
                'price': 138000,
                'description': 'Experience the pristine beaches and marine life of Andaman Islands in luxury.',
                'image_url': 'https://source.unsplash.com/random/800x600/?andaman-luxury',
                'transport': 'Ship'
            },
            {
                'title': 'Dubai Extravaganza',
                'origin_country': 'Hyderabad',
                'destination_country': 'Dubai, UAE',
                'number_of_nights': 4,
                'price': 190000,
                'description': 'Experience the opulence of Dubai with luxury shopping, desert safaris, and iconic landmarks.',
                'image_url': 'https://source.unsplash.com/random/800x600/?dubai-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Kathmandu Cultural Tour',
                'origin_country': 'Kolkata',
                'destination_country': 'Kathmandu, Nepal',
                'number_of_nights': 5,
                'price': 126000,
                'description': 'Explore the rich cultural heritage and Himalayan landscapes of Nepal in style.',
                'image_url': 'https://source.unsplash.com/random/800x600/?kathmandu-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Goa Beach Paradise',
                'origin_country': 'Ahmedabad',
                'destination_country': 'Goa, India',
                'number_of_nights': 4,
                'price': 94500,
                'description': 'Luxury beachfront resorts and vibrant nightlife in India\'s party capital.',
                'image_url': 'https://source.unsplash.com/random/800x600/?goa-luxury',
                'transport': 'Train (domestic)'
            },
            {
                'title': 'Jaipur Royal Experience',
                'origin_country': 'Pune',
                'destination_country': 'Jaipur, India',
                'number_of_nights': 3,
                'price': 74000,
                'description': 'Live like royalty in the Pink City with palace stays and private tours.',
                'image_url': 'https://source.unsplash.com/random/800x600/?jaipur-luxury',
                'transport': 'Flight (domestic)'
            },
            {
                'title': 'Maldives Paradise Escape',
                'origin_country': 'Kochi',
                'destination_country': 'Malé, Maldives',
                'number_of_nights': 5,
                'price': 322000,
                'description': 'Experience ultimate luxury in the beautiful islands of Maldives with overwater villas.',
                'image_url': 'https://source.unsplash.com/random/800x600/?maldives-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Hong Kong Luxury Getaway',
                'origin_country': 'Jaipur',
                'destination_country': 'Hong Kong',
                'number_of_nights': 6,
                'price': 276000,
                'description': 'Experience the vibrant city life and stunning skyline of Hong Kong in luxury.',
                'image_url': 'https://source.unsplash.com/random/800x600/?hongkong-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Kuala Lumpur Adventure',
                'origin_country': 'Delhi',
                'destination_country': 'Kuala Lumpur, Malaysia',
                'number_of_nights': 5,
                'price': 134000,
                'description': 'Discover the perfect blend of modern and traditional in Malaysia\'s capital.',
                'image_url': 'https://source.unsplash.com/random/800x600/?kualalumpur-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Ho Chi Minh City Tour',
                'origin_country': 'Mumbai',
                'destination_country': 'Ho Chi Minh City, Vietnam',
                'number_of_nights': 6,
                'price': 158000,
                'description': 'Experience the energy of Vietnam\'s largest city with luxury accommodations.',
                'image_url': 'https://source.unsplash.com/random/800x600/?hochiminh-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Colombo Coastal Retreat',
                'origin_country': 'Chennai',
                'destination_country': 'Colombo, Sri Lanka',
                'number_of_nights': 4,
                'price': 102000,
                'description': 'Luxury beachfront experience in the heart of Sri Lanka.',
                'image_url': 'https://source.unsplash.com/random/800x600/?colombo-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Seoul Cultural Experience',
                'origin_country': 'Bengaluru',
                'destination_country': 'Seoul, South Korea',
                'number_of_nights': 7,
                'price': 318000,
                'description': 'Immerse yourself in Korean culture with luxury stays and private tours.',
                'image_url': 'https://source.unsplash.com/random/800x600/?seoul-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Taipei Exploration',
                'origin_country': 'Hyderabad',
                'destination_country': 'Taipei, Taiwan',
                'number_of_nights': 6,
                'price': 276000,
                'description': 'Discover the perfect blend of traditional and modern in Taiwan.',
                'image_url': 'https://source.unsplash.com/random/800x600/?taipei-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Dhaka City Tour',
                'origin_country': 'Kolkata',
                'destination_country': 'Dhaka, Bangladesh',
                'number_of_nights': 3,
                'price': 78000,
                'description': 'Experience the vibrant culture of Bangladesh with luxury accommodations.',
                'image_url': 'https://source.unsplash.com/random/800x600/?dhaka-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Phuket Beach Paradise',
                'origin_country': 'Ahmedabad',
                'destination_country': 'Phuket, Thailand',
                'number_of_nights': 5,
                'price': 134000,
                'description': 'Luxury beachfront resorts and crystal clear waters in Thailand\'s largest island.',
                'image_url': 'https://source.unsplash.com/random/800x600/?phuket-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Tbilisi Cultural Tour',
                'origin_country': 'Pune',
                'destination_country': 'Tbilisi, Georgia',
                'number_of_nights': 6,
                'price': 158000,
                'description': 'Discover the rich history and culture of Georgia\'s capital in luxury.',
                'image_url': 'https://source.unsplash.com/random/800x600/?tbilisi-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Baku City Experience',
                'origin_country': 'Mumbai',
                'destination_country': 'Baku, Azerbaijan',
                'number_of_nights': 5,
                'price': 134000,
                'description': 'Experience the perfect blend of modern architecture and ancient history in Baku.',
                'image_url': 'https://source.unsplash.com/random/800x600/?baku-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Almaty Mountain Retreat',
                'origin_country': 'Delhi',
                'destination_country': 'Almaty, Kazakhstan',
                'number_of_nights': 5,
                'price': 134000,
                'description': 'Luxury mountain resorts and stunning landscapes in Kazakhstan\'s largest city.',
                'image_url': 'https://source.unsplash.com/random/800x600/?almaty-luxury',
                'transport': 'Flight'
            },
            {
                'title': 'Kochi Backwaters',
                'origin_country': 'Chennai',
                'destination_country': 'Kochi, India',
                'number_of_nights': 3,
                'price': 74500,
                'description': 'Luxury houseboat experience through the famous Kerala backwaters.',
                'image_url': 'https://source.unsplash.com/random/800x600/?kochi-luxury',
                'transport': 'Train (domestic)'
            },
            {
                'title': 'Srinagar Houseboat Stay',
                'origin_country': 'Hyderabad',
                'destination_country': 'Srinagar, India',
                'number_of_nights': 5,
                'price': 114000,
                'description': 'Luxury houseboat experience on Dal Lake with stunning Himalayan views.',
                'image_url': 'https://source.unsplash.com/random/800x600/?srinagar-luxury',
                'transport': 'Flight (domestic)'
            },
            {
                'title': 'Andaman Island Hopping',
                'origin_country': 'Kolkata',
                'destination_country': 'Port Blair, Andaman',
                'number_of_nights': 5,
                'price': 114000,
                'description': 'Explore multiple islands of Andaman with luxury accommodations.',
                'image_url': 'https://source.unsplash.com/random/800x600/?andaman2-luxury',
                'transport': 'Ship'
            },
            {
                'title': 'Goa Coastal Drive',
                'origin_country': 'Jaipur',
                'destination_country': 'Goa, India',
                'number_of_nights': 4,
                'price': 94000,
                'description': 'Luxury beach-hopping experience along Goa\'s stunning coastline.',
                'image_url': 'https://source.unsplash.com/random/800x600/?goa2-luxury',
                'transport': 'Bus (domestic)'
            }
        ]
        
        # Add some random hot deals (about 30% of total tours)
        num_hot_deals = max(3, len(luxury_tours) // 3)
        hot_deal_indices = random.sample(range(len(luxury_tours)), num_hot_deals)
        
        for i, tour_data in enumerate(luxury_tours):
            # Include transport in description for display
            full_description = f"{tour_data['description']}\n\nTransport: {tour_data['transport']}"
            
            tour = Tour(
                title=tour_data['title'],
                origin_country=tour_data['origin_country'],
                destination_country=tour_data['destination_country'],
                number_of_nights=tour_data['number_of_nights'],
                price=tour_data['price'],
                description=full_description,
                category='luxury',
                is_hot_deal=(i in hot_deal_indices),
                discount=random.choice([10, 15, 20]) if i in hot_deal_indices else 0,
                image_url=tour_data['image_url']
            )
            tour.save()
            
            deal_status = " (Hot Deal!)" if i in hot_deal_indices else ""
            self.stdout.write(self.style.SUCCESS(f'Successfully added luxury tour: {tour.title}{deal_status}'))
        
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(luxury_tours)} luxury tours!'))
