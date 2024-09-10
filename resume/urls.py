from django.urls import path
from .views import ResumeExtractorView

urlpatterns = [
    path('extract_resume/', ResumeExtractorView.as_view(), name='extract_resume')
]
