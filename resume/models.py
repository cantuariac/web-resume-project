from django.db import models
from django.db.models.enums import Choices
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Profile(models.Model):

    user = models.OneToOneField(
        User, verbose_name=_("User"), on_delete=models.CASCADE)

    display_name = models.CharField(
        _("Display name"), max_length=100, blank=True)
    picture = models.ImageField(
        _("Profile picture"), upload_to="images/profiles", blank=True)
    birthday = models.DateField(_("Birthday"))
    location = models.CharField(_("Location"), max_length=50)
    # location = models.ForeignKey(City, verbose_name=_("Location"), on_delete=models.SET_NULL)

    contact_email = models.EmailField(
        _("Contact email"), max_length=254, blank=True)
    contact_phone = PhoneNumberField(blank=True)
    # contact_phone = models.CharField(
    #     _("Phone number"), max_length=15, blank=True)
    website = models.URLField(_("Website"), max_length=256, blank=True)

    skill_set = models.ManyToManyField("resume.Skill", verbose_name=_("skills"))

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("profiles", kwargs={"pk": self.pk})


class SocialLink(models.Model):
    """Model definition for SocialLink."""
    SOCIAL_NETWORKS = enumerate(['GitHub', 'LinkedIn'])

    profile = models.ForeignKey(
        Profile, verbose_name=_("Profile"), on_delete=models.CASCADE)
    social_network = models.IntegerField(
        _("Social Network"), choices=SOCIAL_NETWORKS)
    link = models.URLField(_("Link"), max_length=200)

    class Meta:
        """Meta definition for SocialLink."""

        verbose_name = 'SocialLink'
        verbose_name_plural = 'SocialLinks'

    def __str__(self):
        """Unicode representation of SocialLink."""
        return f'{self.social_network}'


date_format = "%b %Y"


class TimelineEvent(models.Model):

    user = models.OneToOneField(
        User, verbose_name=_("User"), on_delete=models.CASCADE)

    start_date = models.DateField(_("Start date"))
    end_date = models.DateField(_("End date"), blank=True, null=True)

    class Meta:
        ordering = ['start_date', 'end_date']
        abstract = True


class JobExperience(TimelineEvent):
    """Model definition for JobExperience."""

    company = models.CharField(_("Company"), max_length=50)
    role = models.CharField(_("Role"), max_length=50)
    description = models.TextField(_("Description"), blank=True)

    class Meta:
        """Meta definition for JobExperience."""

        verbose_name = 'JobExperience'
        verbose_name_plural = 'JobExperiences'

    def __str__(self):
        """Unicode representation of JobExperience."""
        return f'{self.company} from {self.start_date.strftime(date_format)} {f"to {self.end_date.strftime(date_format)}" if self.end_date else "until now"}'


class AcademicExperience(TimelineEvent):
    """Model definition for Academic experience."""

    school = models.CharField(_("School"), max_length=50)
    course = models.CharField(_("Course"), max_length=50)

    class Meta:
        """Meta definition for Education."""

        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        """Unicode representation of Education."""
        return f'{self.course} from {self.start_date.strftime(date_format)} {f"to {self.end_date.strftime(date_format)}" if self.end_date else "until now"}'  # TODO


class Skill(models.Model):
    SKILL_TYPE = enumerate([_("Software tool"), _("Programing Language"),
                            _("Software framework"), _("Architecture / Paradigm")])

    type = models.IntegerField(
        _("Skill type"), choices=SKILL_TYPE, blank=True, null=True)
    
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name = _("skill")
        verbose_name_plural = _("skills")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("skills", kwargs={"pk": self.pk})
