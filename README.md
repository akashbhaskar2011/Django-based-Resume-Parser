
# Django-based Resume Parser

A Django-based Resume Parser application that extracts key details from resumes, such as the candidate's first name, email ID, and mobile number. This project provides a REST API endpoint for extracting these details from uploaded resume files.

## Features

- **Resume Upload**: Upload resumes in various formats.
- **Detail Extraction**: Extract candidate's first name, email ID, and mobile number.
- **API Endpoint**: Access the resume parsing functionality through a REST API endpoint.

## Installation

### Prerequisites

- Python 3.8, 3.9 (Recommended)
- Django 3.x or higher
- Django REST Framework
- Other dependencies listed in `requirements.txt`

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/akashbhaskar2011/Django-based-Resume-Parser.git
   ```

2. **Create a Virtual Environment**

   It's recommended to use Python 3.8 or 3.9 due to compatibility issues with certain packages in Python 3.12.

   If Python 3.9 is not installed, you can install it using Homebrew (on macOS):

   ```bash
   brew install python@3.9
   ```

   Then create and activate the virtual environment:

   ```bash
   python3.9 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Upgrade pip, setuptools, and wheel**

   To ensure compatibility with the dependencies:

   ```bash
   pip install --upgrade pip setuptools wheel
   ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

7. **Access the API**

   Open your browser and navigate to `http://127.0.0.1:8000/api/parse_resume/` to access the resume parsing endpoint.

## Additional Steps for Python 3.12 Users

If you're using Python 3.12, some packages may have compatibility issues. Follow these additional steps:

1. **Manually Update `setuptools` and `wheel`**

   ```bash
   pip install --upgrade setuptools wheel
   ```

2. **Install `numpy` Separately**

   Sometimes installing `numpy` separately can resolve issues:

   ```bash
   pip install numpy==1.23.5
   ```

   Then install the remaining dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Recreate the Virtual Environment** (if needed)

   If the above steps don’t resolve the issues, try recreating the virtual environment:

   ```bash
   rm -rf venv
   python3.9 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip setuptools wheel
   pip install -r requirements.txt
   ```

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

This should now help in resolving potential issues when using newer versions of Python. Let me know if any further changes are needed!
