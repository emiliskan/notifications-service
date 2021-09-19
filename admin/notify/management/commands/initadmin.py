from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create superuser'

    def add_arguments(self, parser):
        parser.add_argument('--user', nargs='?', type=str,
                            default='admin', help='username')
        parser.add_argument('--email', nargs='?', type=str,
                            default='admin@email.com', help='email')
        parser.add_argument('--passwd', nargs='?', type=str,
                            default='password', help='password')

    def handle(self, *args, **options):
        name = options['user']
        email = options['email']
        password = options['passwd']
        if User.objects.filter(username=name, email=email).first():
            print(f'Admin account can only be initialized: {name}:{password}')
        else:
            User.objects.create_superuser(name, email, password)
            print(f'Creating account for {name} with password: {password}')
