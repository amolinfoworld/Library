from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import string,random

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        print(parser)
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

        # Optional argument
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix', )

        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs['prefix']
        admin = kwargs['admin']
        print(kwargs)

        for i in range(total):
            if prefix:
                username = '{prefix}_{random_string}'.format(prefix=prefix, random_string=get_random_string())
            else:
                username = get_random_string()

            if admin:
                User.objects.create_superuser(username=username, email='', password='123')
            else:
                User.objects.create_user(username=username, email='', password='123')



    '''def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            username=get_random_string()
            email=username+'@gmail.com'
            s1=string.digits
            #print(s1)
            s2=string.ascii_uppercase
             #print(s2)
            s3=string.ascii_lowercase
            #print(s3)
            s4=string.punctuation
            #print(len(s4))
            s=[]
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4)) 
            s.extend(list(username))
            random.shuffle(s)
            password=("".join(s[0:10]))
            User.objects.create_user(username, email, password)
            '''