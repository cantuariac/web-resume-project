from django.contrib import admin
from .models import *

admin.site.register([Profile, SocialLink, JobExperience,
                    AcademicExperience, Skill, UserSkill, Certificate, PortfolioEntry])
