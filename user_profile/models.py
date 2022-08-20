from uuid import uuid4

from django.db import models
from django.utils.translation import ugettext as _
from django.urls import reverse
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import date as date_filter

from resume.models import Skill, SocialMedia

date_format = "b Y"
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'.")


def profile_picture_file_path(user, filename: str):
    ext = filename.split('.')[-1]
    return f'profile_pictures/{uuid4()}.{ext}'


class UserProfile(AbstractUser):
    display_name = models.CharField(_("Display name"), max_length=100)
    title = models.CharField(_("Title"), max_length=100, blank=True)
    contact_email = models.EmailField(_("Contact email"),
                                      max_length=254,
                                      blank=True)
    contact_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    location = models.CharField(_("Location"), max_length=100, blank=True)
    website = models.URLField(_("Website"), max_length=256, blank=True)
    birthday = models.DateField(_("Birthday"), blank=True, null=True)

    picture = models.ImageField(_("Profile picture"),
                                upload_to=profile_picture_file_path,
                                blank=True)

    summary = models.TextField(_("Summary"), blank=True)

    skill_set = models.ManyToManyField("resume.Skill",
                                       verbose_name=_("skills"),
                                       through="user_profile.UserSkill",
                                       blank=True)
    socialmedia_set = models.ManyToManyField(
        "resume.SocialMedia",
        through="user_profile.UserSocialLink",
        verbose_name=_("Social media links"),
        blank=True)

    class Meta:
        verbose_name = _("user profile")
        verbose_name_plural = _("user profiles")

    def __str__(self):
        return f'{self.username}'

    def get_absolute_url(self):
        return reverse("profiles", kwargs={"pk": self.pk})

    def get_skills(self):
        return UserSkill.objects.filter(user=self).distinct()


class UserSocialLink(models.Model):
    """Model definition for UserSocialLink."""

    user = models.ForeignKey(UserProfile,
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


class TimelineEvent(models.Model):
    user = models.ForeignKey(UserProfile,
                             verbose_name=_("User profile"),
                             on_delete=models.CASCADE)

    description = models.TextField(_("Description"))
    location = models.CharField(_("Location"), max_length=100)

    start_date = models.DateField(_("Start date"))
    end_date = models.DateField(_("End date"), blank=True, null=True)

    class Meta:
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
    skills_applied = models.ManyToManyField("user_profile.UserSkill",
                                            verbose_name=_("Skills applied"),
                                            blank=True)

    class Meta:
        """Meta definition for JobExperience."""

        verbose_name = _("Job experience")
        verbose_name_plural = _("Job experiences")
        ordering = ["-start_date"]

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
        ordering = ["-start_date"]

    def __str__(self):
        """Unicode representation of Education."""
        return f'{self.course} at {self.school} ' + self.period()


class UserSkill(models.Model):
    user = models.ForeignKey(UserProfile,
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
        return self.skill.name

    def label(self):
        return _("%(p)s is %(l)s in %(s)s" % {'p': self.profile, 'l': self.get_level_display(), 's': self.skill})

    def get_absolute_url(self):
        return reverse("userskills", kwargs={"pk": self.pk})


def certificate_file_path(certificate, filename: str):
    ext = filename.split('.')[-1]
    return f'certificates/{certificate.user.username}/{uuid4()}.{ext}'


class Certificate(models.Model):
    user = models.ForeignKey(UserProfile,
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
                            upload_to=certificate_file_path,
                            blank=True)

    class Meta:
        verbose_name = _("Certificate")
        verbose_name_plural = _("Certificates")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("certificates", kwargs={"pk": self.pk})


class PortfolioEntry(models.Model):
    user = models.ForeignKey(UserProfile,
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
            _("Publication"),
            _("POC")
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
