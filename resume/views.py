from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from resume.serializers import CandidateSerializer
from rest_framework import status
from .utils import parse_resume
from django.core.files.storage import default_storage
import os

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
