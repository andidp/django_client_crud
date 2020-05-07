## Develop and Tests

```shell
$ python -m venv venv
$ . venv/Scripts/activate
$ pip install -r requirements.txt
$ pytest
```

## Run in browser

```shell
$ py ./manage.py makemigrations
$ py ./manage.py migrate
$ py ./manage.py createsuperuser
$ py ./manage.py runserver
```
