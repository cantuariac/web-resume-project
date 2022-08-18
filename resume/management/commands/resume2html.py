from resume.models import *
from django.template.loader import render_to_string
from django.utils import translation
from django.core.management.base import BaseCommand, CommandError
import argparse

from user_profile.models import UserProfile


class Command(BaseCommand):
    help = 'Generates a html file of a given user\'s resume'

    def add_arguments(self, parser):
        parser.add_argument('username', help='Profile\'s username', type=str)
        parser.add_argument('-l','--language', help='resume\'s locale code, default is en-us', action='store', type=str)

    def handle(self, *args, **options):
        username = options['username']
        profile = UserProfile.objects.filter(username=username).first()
        if not profile:
            raise CommandError(f'User {username} does not exists')
        print(f'Generating html resume for {profile}\'s profile')

        # print(translation.get_language())
        if options['language']:
            language = options['language']
            if translation.check_for_language(language):
                translation.activate(language)
            else:
                raise CommandError(f'"{language}" is not a valid language code')

        html = render_to_string('resume.html', {'profile':profile})
        # print(html)

        open(f'resume-{username}-{translation.get_language()}.html', 'wb').write(html.encode())


'''
parser = argparse.ArgumentParser(description="Script to generate static html from a user's resume")
parser.add_argument(dest='username', action='store', type=str)
parser.add_argument('-l', dest='language', action='store', type=str)

args = parser.parse_args()

username = 'caio'
language = None

profile = Profile.objects.filter(user__username=username).first()
print(profile)

# print(translation.get_language())
if language:
    if translation.check_for_language(language):
        translation.activate(language)
    else:
        print(f'"{language}" is not a valid language code')

html = render_to_string('resume.html', {'profile':profile})
# print(html)

open(f'resume_{username}.html', 'wb').write(html.encode())
'''
