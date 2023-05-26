
# How to run this project

1. Create virtual env  ```python3 -m venv ./venv```
2. Active venv ```source venv/bin/activate```
3. Install dependencies ```pip install -r requirements.txt```
4. Export .env file  ```export(xargs <.env)```
5. Run ```python manage.py makemigrations```
6. Run ```python manage.py migrate```
7. Run ```python manage.py runserver```


## How to Load data.
```
python manage.py runscript seeders.load_user;
```
Or 
```
bash scripts/load_user.sh
```

## Swagger URL
```
http://127.0.0.1:8000/swagger/
```
