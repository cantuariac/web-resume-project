from django.urls import path
from .views import *

urlpatterns = [
    # path("resume/", ResumeView.as_view(), name="resume"),
    path("resume/<username>", ResumeView.as_view(), name="resume"),
    path("resume/<username>/<language>", ResumeView.as_view(), name="resume"),
    path("pdf/<username>", ResumeAsPDF.as_view(), name="pdf"),
    path("pdf/<username>/<language>", ResumeAsPDF.as_view(), name="pdf"),
]
