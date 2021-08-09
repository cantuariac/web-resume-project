from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class ResumeView(TemplateView):
    template_name = "resume.html"

    def get_context_data(self,
                         username: str = None,
                         *args,
                         **kwargs) -> HttpResponse:
        context = super().get_context_data(**kwargs)
        if (username):
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)
            print(profile)
            context['profile'] = profile

        return context
