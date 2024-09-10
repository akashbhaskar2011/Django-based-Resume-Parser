
# Django-based Resume Parser

A Django-based Resume Parser application that extracts key details from resumes, such as the candidate's first name, email ID, and mobile number. This project provides a REST API endpoint for extracting these details from uploaded resume files.

## Features

- **Resume Upload**: Upload resumes in various formats.
- **Detail Extraction**: Extract candidate's first name, email ID, and mobile number.
- **API Endpoint**: Access the resume parsing functionality through a REST API endpoint.

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 3.x or higher
- Django REST Framework
- Other dependencies listed in `requirements.txt`

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/akashbhaskar2011/Django-based-Resume-Parser.git

   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

6. **Access the API**

   Open your browser and navigate to `http://127.0.0.1:8000/api/parse_resume/` to access the resume parsing endpoint.

## Usage

1. **Send a POST request** to `http://127.0.0.1:8000/api/parse_resume/` with a resume file attached.

2. **Receive a JSON response** containing the extracted details.

### Example Request

```bash
curl -X POST http://127.0.0.1:8000/api/parse_resume/ -F "resume=@path/to/resume.pdf"
```

### Example Response

```json
{
  "first_name": "John",
  "email": "john.doe@example.com",
  "mobile": "+1234567890"
}
```

## Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework used
- [Django REST Framework](https://www.django-rest-framework.org/) - For building the API
- [Python](https://www.python.org/) - The programming language

---

Feel free to adjust this `README.md` to better fit the specifics of your project or add any additional sections as needed.
