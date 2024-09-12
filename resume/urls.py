from django.urls import path
from .views import ResumeExtractorView,resume_list,resume_detail,download_resumes_csv,delete_resume

urlpatterns = [
    path('extract_resume/', ResumeExtractorView.as_view(), name='extract_resume'),
     path('resumes/', resume_list, name='resume_list'),
     path('resume/<int:resume_id>/', resume_detail, name='resume_detail'),
      path('download/resumes/', download_resumes_csv, name='download_resumes'),
          path('delete/<int:resume_id>/', delete_resume, name='delete_resume'),

]

