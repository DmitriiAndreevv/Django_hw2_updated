from django.core.management.base import BaseCommand
from modapp.models import User

class Command(BaseCommand):
    help = 'Create_User'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name')
        parser.add_argument('phone', type=str, help='Phone number')
        parser.add_argument('email', type=str, help='Email address')
        parser.add_argument('address', type=str, help='Address')
        parser.add_argument('country', type=str, help='Country')
        parser.add_argument('city', type=str, help='City')
        parser.add_argument('state', type=str, help='State')

        def handle(self, *args, **kwargs):
            name = kwargs.get['name']
            phone = kwargs.get['phone']
            email = kwargs.get['email']
            address = kwargs.get['address']
            country = kwargs.get['country']
            city = kwargs.get['city']
            state = kwargs.get['state']

            user = User(name=name, phone=phone, email=email, address=address, country=country, city=city, state=state)
            user.save()

            self.stdout.write(f'{user}')