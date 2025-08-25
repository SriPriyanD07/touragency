from django.core.management.base import BaseCommand
from asiantoursagency.models import Tour
import random

class Command(BaseCommand):
    help = 'Load economic tour data into the database'

    def handle(self, *args, **kwargs):
        # Clear existing economic tours
        Tour.objects.filter(category='economic').delete()
        
        # Economic tour data
        economic_tours = [
            {
                'title': 'Bangkok Budget Getaway',
                'origin_country': 'Mumbai',
                'destination_country': 'Bangkok, Thailand',
                'number_of_nights': 5,
                'price': 40000,
                'description': 'Experience Bangkok on a budget with comfortable accommodations and great value experiences.',
                'image_url': 'https://source.unsplash.com/random/800x600/?bangkok-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Singapore Value Tour',
                'origin_country': 'Delhi',
                'destination_country': 'Singapore',
                'number_of_nights': 4,
                'price': 57000,
                'description': 'Explore Singapore on a budget without missing out on key attractions.',
                'image_url': 'https://source.unsplash.com/random/800x600/?singapore-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Tokyo Budget Adventure',
                'origin_country': 'Bengaluru',
                'destination_country': 'Tokyo, Japan',
                'number_of_nights': 7,
                'price': 120000,
                'description': 'Experience the best of Tokyo with budget-friendly accommodations and activities.',
                'image_url': 'https://source.unsplash.com/random/800x600/?tokyo-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Andaman Budget Retreat',
                'origin_country': 'Chennai',
                'destination_country': 'Port Blair, Andaman',
                'number_of_nights': 6,
                'price': 29500,
                'description': 'Enjoy the beautiful Andaman Islands on a budget with comfortable stays.',
                'image_url': 'https://source.unsplash.com/random/800x600/?andaman-budget',
                'transport': 'Ship'
            },
            {
                'title': 'Dubai Budget Experience',
                'origin_country': 'Hyderabad',
                'destination_country': 'Dubai, UAE',
                'number_of_nights': 4,
                'price': 57000,
                'description': 'Experience Dubai\'s wonders with budget-friendly accommodations and tours.',
                'image_url': 'https://source.unsplash.com/random/800x600/?dubai-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Kathmandu Budget Tour',
                'origin_country': 'Kolkata',
                'destination_country': 'Kathmandu, Nepal',
                'number_of_nights': 5,
                'price': 40000,
                'description': 'Explore the cultural heritage of Kathmandu on a budget.',
                'image_url': 'https://source.unsplash.com/random/800x600/?kathmandu-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Goa Budget Holiday',
                'origin_country': 'Ahmedabad',
                'destination_country': 'Goa, India',
                'number_of_nights': 4,
                'price': 18500,
                'description': 'Enjoy the beaches of Goa with budget accommodations and local experiences.',
                'image_url': 'https://source.unsplash.com/random/800x600/?goa-budget',
                'transport': 'Train (domestic)'
            },
            {
                'title': 'Jaipur Budget Experience',
                'origin_country': 'Pune',
                'destination_country': 'Jaipur, India',
                'number_of_nights': 3,
                'price': 20500,
                'description': 'Explore the Pink City on a budget with comfortable stays.',
                'image_url': 'https://source.unsplash.com/random/800x600/?jaipur-budget',
                'transport': 'Flight (domestic)'
            },
            {
                'title': 'Maldives Budget Escape',
                'origin_country': 'Kochi',
                'destination_country': 'Malé, Maldives',
                'number_of_nights': 5,
                'price': 84000,
                'description': 'Experience the Maldives on a budget with great value accommodations.',
                'image_url': 'https://source.unsplash.com/random/800x600/?maldives-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Hong Kong Budget Tour',
                'origin_country': 'Jaipur',
                'destination_country': 'Hong Kong',
                'number_of_nights': 6,
                'price': 99000,
                'description': 'Explore Hong Kong on a budget with comfortable accommodations.',
                'image_url': 'https://source.unsplash.com/random/800x600/?hongkong-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Kuala Lumpur Budget Trip',
                'origin_country': 'Delhi',
                'destination_country': 'Kuala Lumpur, Malaysia',
                'number_of_nights': 5,
                'price': 44000,
                'description': 'Discover Kuala Lumpur on a budget with great value experiences.',
                'image_url': 'https://source.unsplash.com/random/800x600/?kualalumpur-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Ho Chi Minh Budget Tour',
                'origin_country': 'Mumbai',
                'destination_country': 'Ho Chi Minh City, Vietnam',
                'number_of_nights': 6,
                'price': 48000,
                'description': 'Experience the energy of Ho Chi Minh City on a budget.',
                'image_url': 'https://source.unsplash.com/random/800x600/?hochiminh-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Colombo Budget Stay',
                'origin_country': 'Chennai',
                'destination_country': 'Colombo, Sri Lanka',
                'number_of_nights': 4,
                'price': 30000,
                'description': 'Enjoy the beaches and culture of Colombo on a budget.',
                'image_url': 'https://source.unsplash.com/random/800x600/?colombo-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Seoul Budget Experience',
                'origin_country': 'Bengaluru',
                'destination_country': 'Seoul, South Korea',
                'number_of_nights': 7,
                'price': 111000,
                'description': 'Explore Seoul on a budget with comfortable accommodations.',
                'image_url': 'https://source.unsplash.com/random/800x600/?seoul-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Taipei Budget Adventure',
                'origin_country': 'Hyderabad',
                'destination_country': 'Taipei, Taiwan',
                'number_of_nights': 6,
                'price': 99000,
                'description': 'Discover Taipei on a budget with great value experiences.',
                'image_url': 'https://source.unsplash.com/random/800x600/?taipei-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Dhaka Budget Tour',
                'origin_country': 'Kolkata',
                'destination_country': 'Dhaka, Bangladesh',
                'number_of_nights': 3,
                'price': 28500,
                'description': 'Experience the vibrant culture of Dhaka on a budget.',
                'image_url': 'https://source.unsplash.com/random/800x600/?dhaka-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Phuket Budget Holiday',
                'origin_country': 'Ahmedabad',
                'destination_country': 'Phuket, Thailand',
                'number_of_nights': 5,
                'price': 44000,
                'description': 'Enjoy the beautiful beaches of Phuket on a budget.',
                'image_url': 'https://source.unsplash.com/random/800x600/?phuket-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Tbilisi Budget Trip',
                'origin_country': 'Pune',
                'destination_country': 'Tbilisi, Georgia',
                'number_of_nights': 6,
                'price': 48000,
                'description': 'Discover the charm of Tbilisi on a budget.',
                'image_url': 'https://source.unsplash.com/random/800x600/?tbilisi-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Baku Budget Experience',
                'origin_country': 'Mumbai',
                'destination_country': 'Baku, Azerbaijan',
                'number_of_nights': 5,
                'price': 44000,
                'description': 'Explore Baku on a budget with comfortable stays.',
                'image_url': 'https://source.unsplash.com/random/800x600/?baku-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Almaty Budget Tour',
                'origin_country': 'Delhi',
                'destination_country': 'Almaty, Kazakhstan',
                'number_of_nights': 5,
                'price': 44000,
                'description': 'Experience the beauty of Almaty on a budget.',
                'image_url': 'https://source.unsplash.com/random/800x600/?almaty-budget',
                'transport': 'Flight'
            },
            {
                'title': 'Kochi Backwaters Budget',
                'origin_country': 'Chennai',
                'destination_country': 'Kochi, India',
                'number_of_nights': 3,
                'price': 12500,
                'description': 'Experience the famous Kerala backwaters on a budget.',
                'image_url': 'https://source.unsplash.com/random/800x600/?kochi-budget',
                'transport': 'Train (domestic)'
            },
            {
                'title': 'Srinagar Budget Stay',
                'origin_country': 'Hyderabad',
                'destination_country': 'Srinagar, India',
                'number_of_nights': 5,
                'price': 34500,
                'description': 'Enjoy the beauty of Srinagar on a budget.',
                'image_url': 'https://source.unsplash.com/random/800x600/?srinagar-budget',
                'transport': 'Flight (domestic)'
            },
            {
                'title': 'Andaman Budget Hopping',
                'origin_country': 'Kolkata',
                'destination_country': 'Port Blair, Andaman',
                'number_of_nights': 5,
                'price': 34500,
                'description': 'Explore the Andaman Islands on a budget.',
                'image_url': 'https://source.unsplash.com/random/800x600/?andaman2-budget',
                'transport': 'Ship'
            },
            {
                'title': 'Goa Budget Coastal',
                'origin_country': 'Jaipur',
                'destination_country': 'Goa, India',
                'number_of_nights': 4,
                'price': 17500,
                'description': 'Enjoy the beaches of Goa on a budget.',
                'image_url': 'https://source.unsplash.com/random/800x600/?goa2-budget',
                'transport': 'Bus (domestic)'
            }
        ]
        
        # Add some random hot deals (about 30% of total tours)
        num_hot_deals = max(3, len(economic_tours) // 3)
        hot_deal_indices = random.sample(range(len(economic_tours)), num_hot_deals)
        
        for i, tour_data in enumerate(economic_tours):
            # Include transport in description for display
            full_description = f"{tour_data['description']}\n\nTransport: {tour_data['transport']}"
            
            tour = Tour(
                title=tour_data['title'],
                origin_country=tour_data['origin_country'],
                destination_country=tour_data['destination_country'],
                number_of_nights=tour_data['number_of_nights'],
                price=tour_data['price'],
                description=full_description,
                category='economic',
                is_hot_deal=(i in hot_deal_indices),
                discount=random.choice([10, 15, 20]) if i in hot_deal_indices else 0,
                image_url=tour_data['image_url']
            )
            tour.save()
            
            deal_status = " (Hot Deal!)" if i in hot_deal_indices else ""
            self.stdout.write(self.style.SUCCESS(f'Successfully added economic tour: {tour.title}{deal_status}'))
        
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(economic_tours)} economic tours!'))
