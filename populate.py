from resume.models import *
from faker import Faker
from django.contrib.auth.models import User
import random
from datetime import date

faker: Faker = Faker(locale='pt-br')

User.objects.create_user('admin', password='1q2w',
                         is_superuser=True, is_staff=True).save()

user = User.objects.create_user(
    'caio', password='1234', first_name="Caio", last_name="Cantuária")
user.save()

profile = Profile(user=user, display_name="Caio Cantuária",
                  title="Desenvolvedor Full Stack",
                  birthday=date(1992, 3, 16),
                  location="Montes Claros, Brasil",
                  contact_email="caio.cantuaria@gmail.com",
                  )
profile.save()

SocialLink(profile=profile, social_network=0, link="https://github.com/cantuariac/").save()

JobExperience(profile=profile,
              start_date=date(2021, 4, 19),
              company="OP Soluções Digitais",
              role="Desenvolvedor de Software",
              location="Montes Claros, Brasil",).save()

AcademicExperience(profile=profile, start_date=date(2016, 9, 3),
                   school="Instituto Federal do Norte de Minas Gerais",
                   course="Ciência da Computação",
                   location="Montes Claros, Brasil",).save()

skills = [Skill(type=0, name="Git"),
          Skill(type=1, name="Python"),
          Skill(type=1, name="JavaScript"),
          Skill(type=2, name="Django"),
          Skill(type=3, name="React Native")]
for s in skills:
    s.save()
    profile.skill_set.add(s)
profile.save()

Skill(type=3, name="DevOps").save()
Skill(type=0, name="Docker").save()
