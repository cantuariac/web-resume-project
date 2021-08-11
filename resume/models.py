from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields.related import ForeignKey
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Profile(models.Model):

    user = models.OneToOneField(User,
                                verbose_name=_("User"),
                                on_delete=models.CASCADE)

    display_name = models.CharField(_("Name"), max_length=100)
    title = models.CharField(_("Title"), max_length=100, blank=True)
    contact_email = models.EmailField(_("Contact email"),
                                      max_length=254,
                                      blank=True)
    contact_phone = PhoneNumberField(blank=True)
    location = models.CharField(_("Location"), max_length=50, blank=True)
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

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return self.display_name

    def get_absolute_url(self):
        return reverse("profiles", kwargs={"pk": self.pk})


class SocialLink(models.Model):
    """Model definition for SocialLink."""

    # class SocialNetworks(models.IntegerChoices):
    #     choices = list(enumerate(['GitHub', 'LinkedIn']))

    profile = models.ForeignKey(Profile,
                                verbose_name=_("User profile"),
                                on_delete=models.CASCADE)
    social_network = models.IntegerField(_("Social Network"),
                                         choices=enumerate(
                                             ["GitHub", "LinkedIn"]))
    link = models.URLField(_("Link"), max_length=200)

    class Meta:
        """Meta definition for SocialLink."""

        verbose_name = _("Social")
        verbose_name_plural = _("Socials")

    def __str__(self):
        """Unicode representation of SocialLink."""
        return f"{self.profile.display_name}'s {self.get_social_network_display()}"


date_format = "%b %Y"


class TimelineEvent(models.Model):

    profile = models.ForeignKey(Profile,
                                verbose_name=_("User profile"),
                                on_delete=models.CASCADE)

    description = models.TextField(_("Description"), blank=True)
    location = models.CharField(_("Location"), max_length=50, blank=True)

    start_date = models.DateField(_("Start date"))
    end_date = models.DateField(_("End date"), blank=True, null=True)

    class Meta:
        ordering = ["start_date", "end_date"]
        abstract = True

    def period(self):
        return f'from {self.start_date.strftime(date_format)} {f"to {self.end_date.strftime(date_format)}" if self.end_date else "until now"}'


class JobExperience(TimelineEvent):
    """Model definition for JobExperience."""

    company = models.CharField(_("Company"), max_length=50)
    role = models.CharField(_("Role"), max_length=50)

    class Meta:
        """Meta definition for JobExperience."""

        verbose_name = _("Job experience")
        verbose_name_plural = _("Job experiences")

    def __str__(self):
        """Unicode representation of JobExperience."""
        return f'{self.role} at {self.company} from {self.start_date.strftime(date_format)} {f"to {self.end_date.strftime(date_format)}" if self.end_date else "until now"}'


class AcademicExperience(TimelineEvent):
    """Model definition for Academic experience."""

    school = models.CharField(_("School"), max_length=50)
    course = models.CharField(_("Course"), max_length=50)

    class Meta:
        """Meta definition for Education."""

        verbose_name = _("Academic experience")
        verbose_name_plural = _("Academic experiences")

    def __str__(self):
        """Unicode representation of Education."""
        return f'{self.course} at {self.school} from {self.start_date.strftime(date_format)} {f"to {self.end_date.strftime(date_format)}" if self.end_date else "until now"}'  # TODO


class Skill(models.Model):
    SKILL_TYPE = enumerate([
        _("Software tool"),
        _("Programing Language"),
        _("Software framework"),
        _("Architecture / Paradigm"),
        _("Language"),
        _("Soft skill"),
    ])

    type = models.IntegerField(_("Skill type"),
                               choices=SKILL_TYPE,
                               blank=True,
                               null=True)

    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name = _("skill")
        verbose_name_plural = _("skills")
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
        verbose_name = _("userskill")
        verbose_name_plural = _("userskills")

    def __str__(self):
        return str(self.skill)

    def get_absolute_url(self):
        return reverse("userskills", kwargs={"pk": self.pk})


class Certificate(models.Model):

    profile = models.ForeignKey(Profile,
                                verbose_name=_("User profile"),
                                on_delete=models.CASCADE)

    name = models.CharField(_("Name"), max_length=50)
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

    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), blank=True)
    cover = models.ImageField(_("Cover image"),
                              upload_to="images/portfolio",
                              blank=True)
    link = models.URLField(_("Link"), max_length=200, blank=True)
    date = models.DateField(_("Date"), blank=True)

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
        verbose_name = _("portfolio entry")
        verbose_name_plural = _("portfolio entries")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolioentries", kwargs={"pk": self.pk})
