from modeltranslation.translator import register, TranslationOptions

from .models import UserProfile, JobExperience, AcademicExperience, Certificate, PortfolioEntry


@register(UserProfile)
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


@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(PortfolioEntry)
class PortfolioEntryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
