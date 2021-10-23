from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields.related import ForeignKey
from django.utils.translation import ugettext_lazy as _
from django.utils.text import format_lazy
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class Profile(models.Model):

    user = models.OneToOneField(User,
                                verbose_name=_("User"),
                                on_delete=models.CASCADE)

    display_name = models.CharField(_("Name"), max_length=100)
    title = models.CharField(_("Title"), max_length=100, blank=True)
    contact_email = models.EmailField(_("Contact email"),
                                      max_length=254,
                                      blank=True)
    contact_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    location = models.CharField(_("Location"), max_length=100, blank=True)
    website = models.URLField(_("Website"), max_length=256, blank=True)
    birthday = models.DateField(_("Birthday"), blank=True)

    picture = models.ImageField(_("Profile picture"),
                                upload_to="profile_pictures/",
                                blank=True)

    summary = models.TextField(_("Summary"), blank=True)

    skill_set = models.ManyToManyField("resume.Skill",
                                       verbose_name=_("skills"),
                                       through="resume.UserSkill",
                                       blank=True)
    socialmedia_set = models.ManyToManyField(
        "resume.SocialMedia",
        through="resume.UserSocialLink",
        verbose_name=_("Social media links"),
        blank=True)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return f'{self.display_name}'

    def get_absolute_url(self):
        return reverse("profiles", kwargs={"pk": self.pk})
    
    def get_skills(self):
        return Skill.objects.filter(jobexperience__profile=self).distinct()


class SocialMedia(models.Model):

    name = models.CharField(_("Name"), max_length=100)
    base_url = models.URLField(_("Base URL"))
    icon_color = models.CharField(_("Color"), max_length=6)
    bi_icon = models.CharField(_("Icon"), max_length=100)

    class Meta:
        verbose_name = _("Social media")
        verbose_name_plural = _("Social medias")

    def __str__(self):
        return self.name

    def get_color(self):
        return "#%s" % (self.icon_color)


class UserSocialLink(models.Model):
    """Model definition for UserSocialLink."""

    # class SocialNetworks(models.IntegerChoices):
    #     choices = list(enumerate(['GitHub', 'LinkedIn']))

    profile = models.ForeignKey(Profile,
                                verbose_name=_("User profile"),
                                on_delete=models.CASCADE)
    socialmedia = models.ForeignKey(SocialMedia,
                                    verbose_name=_("Social media"),
                                    on_delete=models.CASCADE)
    username = models.CharField(_("Username or link"), max_length=100)
    link = models.URLField(_("Link"), max_length=200, blank=True)

    def get_link(self):
        if self.username in self.link and self.socialmedia.base_url in self.link:
            return self.link
        else:
            self.link = self.socialmedia.base_url + self.username
            self.save()
            return self.link

    class Meta:
        """Meta definition for SocialLink."""

        verbose_name = _("User's social media link")
        verbose_name_plural = _("User's social media links")

    def __str__(self):
        """Unicode representation of SocialLink."""
        return f'{self.username}@{self.socialmedia}'


date_format = "b Y"

from django.utils import translation
from django.template.defaultfilters import date as date_filter

class TimelineEvent(models.Model):

    profile = models.ForeignKey(Profile,
                                verbose_name=_("User profile"),
                                on_delete=models.CASCADE)

    description = models.TextField(_("Description"))
    location = models.CharField(_("Location"), max_length=100)

    start_date = models.DateField(_("Start date"))
    end_date = models.DateField(_("End date"), blank=True, null=True)

    class Meta:
        ordering = ["start_date", "end_date"]
        abstract = True

    def period(self):
        if self.end_date:
            return _('from %(start_date)s to %(end_date)s') % {
                'start_date': date_filter(self.start_date, date_format),
                'end_date': date_filter(self.end_date, date_format)
            }
        else:
            return _('since %(start_date)s') % {
                'start_date': date_filter(self.start_date, date_format)
            }


class JobExperience(TimelineEvent):
    """Model definition for JobExperience."""

    company = models.CharField(_("Company"), max_length=100)
    role = models.CharField(_("Role"), max_length=100)
    skills_applied = models.ManyToManyField("resume.Skill",
                                            verbose_name=_("Skills applied"),
                                            blank=True)

    class Meta:
        """Meta definition for JobExperience."""

        verbose_name = _("Job experience")
        verbose_name_plural = _("Job experiences")

    def __str__(self):
        """Unicode representation of JobExperience."""
        return f'{self.role} at {self.company} ' + self.period()


class AcademicExperience(TimelineEvent):
    """Model definition for Academic experience."""

    school = models.CharField(_("School"), max_length=100)
    course = models.CharField(_("Course"), max_length=100)

    class Meta:
        """Meta definition for Education."""

        verbose_name = _("Academic experience")
        verbose_name_plural = _("Academic experiences")

    def __str__(self):
        """Unicode representation of Education."""
        return f'{self.course} at {self.school} ' + self.period()


class SkillType(models.IntegerChoices):
    (SOFTWARE, PROGRAMING_LANGUAGE, PROGRAMING_TOOL, SOFTWARE_FRAMEWORK,
     ARCHITECTURE_PARADIGM, LANGUAGE, SOFT_SKILL) = enumerate([
         _("Software"),
         _("Programing language"),
         _("Programing tool"),
         _("Software framework"),
         _("Architecture / Paradigm"),
         _("Language"),
         _("Soft skill"),
     ])


class Skill(models.Model):

    type = models.IntegerField(_("Skill type"),
                               choices=SkillType.choices,
                               blank=True,
                               null=True)

    name = models.CharField(_("Name"), max_length=100)

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")
        ordering = ["type", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("skills", kwargs={"pk": self.pk})


class UserSkill(models.Model):

    profile = models.ForeignKey(Profile,
                                verbose_name=_("User profile"),
                                on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill,
                              verbose_name=_("Skill"),
                              on_delete=models.CASCADE)
    level = models.IntegerField(
        _("Proficiency level"),
        choices=enumerate([
            _("Novice"),
            _("Beginner"),
            _("Competent"),
            _("Proficient"),
            _("Expert")
        ]),
        default=2,
    )

    class Meta:
        verbose_name = _("users' skill")
        verbose_name_plural = _("users' skills")

    def __str__(self):
        return str(self.skill)

    def get_absolute_url(self):
        return reverse("userskills", kwargs={"pk": self.pk})


class Certificate(models.Model):

    profile = models.ForeignKey(Profile,
                                verbose_name=_("User profile"),
                                on_delete=models.CASCADE)

    name = models.CharField(_("Name"), max_length=100)
    skill = models.ForeignKey(Skill,
                              verbose_name=_("Skill"),
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    link = models.URLField(_("Certificate link"), max_length=200, blank=True)
    file = models.FileField(_("Certificate file"),
                            upload_to="storage/portfolio",
                            blank=True)

    class Meta:
        verbose_name = _("certificate")
        verbose_name_plural = _("certificates")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("certificates", kwargs={"pk": self.pk})


class PortfolioEntry(models.Model):

    profile = models.ForeignKey(Profile,
                                verbose_name=_("User profile"),
                                on_delete=models.CASCADE)

    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"), blank=True)
    cover = models.ImageField(_("Cover image"),
                              upload_to="portfolioentries",
                              blank=True)
    link = models.URLField(_("Link"), max_length=200, blank=True)
    date = models.DateField(_("Date"), blank=True, null=True)

    type = models.IntegerField(
        _("Entry type"),
        choices=enumerate([
            _("Side project"),
            _("Client project"),
            _("Product"),
            _("Publication")
        ]),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("portfolio entries")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolioentries", kwargs={"pk": self.pk})
