
from django.http.response import HttpResponse
from django.utils import translation
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator

from user_profile.models import UserProfile


@method_decorator(xframe_options_exempt, name='dispatch')
class ResumeView(TemplateView):
    template_name = "resume.html"

    def get_context_data(self,
                         username: str = None,
                         language: str = None,
                         *args,
                         **kwargs) -> HttpResponse:
        context = super().get_context_data(**kwargs)

       # print("ResumeView:", self.request.GET)

        if username:
            profile = UserProfile.objects.get(username=username)
            # print(profile)
            context['profile'] = profile

        context['nopic'] = 'nopic' in self.request.GET
        
        if language:
            if translation.check_for_language(language):
                print('lang', language)
                translation.activate(language)
            else:
                context['error'] = _(f'"{language}" is not a valid language code')


        return context
