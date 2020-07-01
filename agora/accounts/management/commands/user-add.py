import os
import json

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from rest_framework.authtoken.models import Token
from accounts.models import User


class Command(BaseCommand):
    help = 'Create a user'

    def add_arguments(self, parser):

        parser.add_argument(
            '--username',
            dest='username',
            help='Unique user name',
        )

        parser.add_argument(
            '--password',
            dest='password',
            help='pasword',
        )

        parser.add_argument(
            '--email',
            dest='email',
            help='Unique user email',
        )

        parser.add_argument(
            '--role',
            dest='role',
            default='superamdin',
            choices=['superadmin', 'serviceadmin', 'observer'],
            help='Choose a role for the user')

    def handle(self, *args, **options):

        data = {}

        username = options['username']
        password = options['password']
        role = options['role']
        email = options['email']

        try:
            a = User.objects.create_user(
                    username=username,
                    password=password,
                    role=role,
                    email=email)
        except IntegrityError as e:
            raise CommandError(e.message)

        token = Token.objects.create(user=a)

        self.stdout.write(
            "User with id: %s, role: %s, token:%s created" %
            (a.pk, options['role'], token))
