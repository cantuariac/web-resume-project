from django.http.request import HttpRequest, QueryDict
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.utils import translation
from django.views.generic import TemplateView
from .models import *
from django.utils.translation import gettext_lazy as _

class ResumeView(TemplateView):
    template_name = "resume.html"

    def get_context_data(self,
                         username: str = None,
                         *args,
                         **kwargs) -> HttpResponse:
        context = super().get_context_data(**kwargs)

        # print("ResumeView:", self.request.GET)

        if (username):
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)
            # print(profile)
            context['profile'] = profile

        context['nopic'] = 'nopic' in self.request.GET
        
        if 'language' in self.request.GET:
            language = self.request.GET['language']
            if translation.check_for_language(language):
                print("ResumeView:",
                      "language=" + language)
                translation.activate(language)
            else:
                context['error'] = _(f'"{language}" is not a valid language code')


        return context
