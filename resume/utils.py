from pyresparser import ResumeParser
import os
# import spacy
# nlp = spacy.load('en_core_web_sm')
# import nltk
# nltk.download('stopwords')

def parse_resume(file_path):
   
    try:

        data = ResumeParser(file_path).get_extracted_data()
        

        first_name = data.get('name', '').split()[0] if data.get('name') else ''
        email = data.get('email', '')
        mobile_number = data.get('mobile_number', '')


        extracted_data = {
            'first_name': first_name,
            'email': email,
            'mobile_number': mobile_number
        }

        return extracted_data
    
    except Exception as e:
        raise Exception(f"Error parsing resume: {str(e)}")
