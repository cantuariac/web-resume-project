from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'summary',
    )


@register(JobExperience)
class JobExperienceTranslationOptions(TranslationOptions):
    fields = (
        'description',
        'role',
    )


@register(AcademicExperience)
class AcademicExperienceTranslationOptions(TranslationOptions):
    fields = (
        'description',
        'course',
    )


@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(PortfolioEntry)
class PortfolioEntryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')