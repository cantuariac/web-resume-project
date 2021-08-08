from resume.models import *
from faker import Faker
from django.contrib.auth.models import User
import random
from datetime import date

faker: Faker = Faker(locale='pt-br')

User.objects.create_user('admin', password='1q2w', is_superuser = True, is_staff = True).save()

user = User.objects.create_user('caio', password='1234', first_name="Caio", last_name="Cantuária")
user.save()

Profile(user=user, birthday=date(1992, 3, 16), location="Montes Claros, Brasil").save()

JobExperience(user=user, start_date=date(2021, 4, 19), company="OP Soluções Digitais", role="Desenvolvedor de Software").save()
AcademicExperience(user=user, start_date=date(2016, 9, 3), school="IFNMG", course="Ciência da Computação").save()
