# Nested_serilizer




### Installation

1. **Clone the Repository:**

       git clone https://github.com/pavanbalafissionlabs/Django_nested_serilizer.git

2 **Create a Virtual Environment**
  
    virtualenv venv
    source venv/bin/activate

3 **install requirements.txt**
  
      pip install -r requirements.txt

4 **Apply Migrations:**

    python manage.py makemigrations
    python manage.py migrate

5 **Create SuperUser if required**
    
        python manage.py createsuperuser

6 Run the application
 
      python manage.py runserver 
      
7 Endpoint 

       api/resume/


 Payload

       {
    "name": "JOHN",
    "experience": 5,
    "tech_skills": "Python, Django",
    "workplace_location": {
        "city": "HYD",
        "country": "TS"
    },
    "work_experience": [
        {
            "project_name": "Project 1",
            "others": {
                "cetificates": "Aws"
            }
        },
        {
            "project_name": "Project 2",
            "others": {
                "cetificates": "AWS,GCP"
            }
        }
    ]
}



