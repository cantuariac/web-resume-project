from django.http.response import HttpResponse
from django.utils import translation
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator

from user_profile.models import UserProfile
from web_resume import settings


@method_decorator(xframe_options_exempt, name='dispatch')
class ResumeView(TemplateView):
    template_name = "resume.html"

    def get_context_data(self,
                         username: str = None,
                         language: str = None,
                         *args,
                         **kwargs) -> HttpResponse:
        context = super().get_context_data(**kwargs)

        if username:
            profile = UserProfile.objects.get(username=username)
            # print(profile)
            context['profile'] = profile

        context['nopic'] = 'nopic' in self.request.GET

        if len(settings.LANGUAGES) > 1:
            context['languages'] = [{
                'name': lang[1],
                'url': f'{lang[0]}'
            } for lang in settings.LANGUAGES]

        if language:
            if translation.check_for_language(language):
                translation.activate(language)
            else:
                context['error'] = _(f'"{language}" is not a valid language code')

        return context
