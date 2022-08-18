# django-chinook-api
Rest ful API with Django for Chinook Database

# Installation

1. Clone project. 
```bash
git clone https://github.com/antoniogmzstat/django-chinook-api.git
```

2. Situate into project folder

```bash
cd ./django-chinook-api/
```

3. Create virtual env for install packages
```bash
python -m virtualenv venv
```

4. Activate virtual env
```bash
source ./venv/bin/activate
```

5. Install list of packages from file requeriments.txt
```bash
pip install -r requirements.txt
```

6. Copy chinook.db into project from url https://www.sqlitetutorial.net/sqlite-sample-database/ after unzip downloaded file

7. Make migrations for the application

```bash
python manage.py makemigrations api
```
```bash
python manage.py migrate
```

8. Set Up Server
```bash
python manage.py runserver
```

9. Access to http://127.0.0.1:8000/api/v.1.0/