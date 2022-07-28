from modeltranslation.translator import register, TranslationOptions

from user_profile.models import UserProfile, JobExperience, AcademicExperience, Certificate, PortfolioEntry
from .models import *


@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('name',)

