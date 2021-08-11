from resume.models import *
from faker import Faker
from django.contrib.auth.models import User
import random
from datetime import date

faker: Faker = Faker(locale="pt-br")

User.objects.create_user("admin",
                         password="1q2w",
                         is_superuser=True,
                         is_staff=True).save()

SocialMedia(name='LinkedIn',
            base_url='https://www.linkedin.com/in',
            icon_color='0e76a8',
            bi_icon='bi-linkedin').save()

SocialMedia(name='GitHub',
            base_url='https://github.com/',
            icon_color='211F1F',
            bi_icon='bi-github').save()


Skill(type=0, name="Git").save()
Skill(type=1, name="Python").save()
Skill(type=1, name="JavaScript").save()
Skill(type=2, name="Django").save()
Skill(type=3, name="React Native").save()
Skill(type=3, name="DevOps").save()
Skill(type=0, name="Docker").save()
