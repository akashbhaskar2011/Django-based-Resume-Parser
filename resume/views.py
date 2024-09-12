from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from resume.serializers import CandidateSerializer
from rest_framework import status
from .utils import parse_resume
from django.core.files.storage import default_storage
import os
from django.shortcuts import redirect
import csv
from django.http import HttpResponse
from .models import Candidate

class ResumeExtractorView(APIView):

    def post(self, request):
        file_obj = request.FILES.get('file')


        if file_obj is None or not file_obj.name.endswith(('.pdf', '.docx')):
            return Response({"error": "Invalid file format. Please upload a PDF or DOCX file."}, status=status.HTTP_400_BAD_REQUEST)
        

        file_path = default_storage.save(file_obj.name, file_obj)
        
        try:
            extracted_data = parse_resume(file_path)
        except Exception as e:
            os.remove(file_path)
            return Response({"error": f"Failed to parse resume: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        os.remove(file_path)


        serializer = CandidateSerializer(data=extracted_data)
        print(extracted_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def resume_list(request):
    query = request.GET.get('search')
    if query:
        resumes = Candidate.objects.filter(name__icontains=query) | Resume.objects.filter(email__icontains=query)
    else:
        resumes = Candidate.objects.all()
    return render(request, 'resume_list.html', {'resumes': resumes})


def download_resumes_csv(request):
    resumes = Candidate.objects.all()
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="resumes.csv"'

    writer = csv.writer(response)
    writer.writerow(['first_name', 'email', 'mobile_number'])

    for resume in resumes:
        writer.writerow([resume.first_name, resume.email, resume.mobile_number])

    return response


def resume_detail(request, resume_id):
    resume = Candidate.objects.get(id=resume_id)
    return render(request, 'resume_detail.html', {'resume': resume})


def delete_resume(request, resume_id):
    resume = Candidate.objects.get(id=resume_id)
    resume.delete()
    return redirect('resume_list')