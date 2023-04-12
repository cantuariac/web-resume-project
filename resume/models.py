
from django.db import models
from django.utils.translation import ugettext as _
from django.urls import reverse
from django.core.validators import RegexValidator


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'.")


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
        return "#%s" % self.icon_color


date_format = "b Y"


class SkillType(models.IntegerChoices):
    (SOFTWARE, PROGRAMING_LANGUAGE, PROGRAMING_TOOL, SOFTWARE_FRAMEWORK,
     ARCHITECTURE_PARADIGM, LANGUAGE, SOFT_SKILL) = enumerate(
        [
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
