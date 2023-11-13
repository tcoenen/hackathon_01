# Context is a Hack de Overheid hackathon of 10 november 2023, challange 3.

This repo has a tiny Django app that renders a clientjourney using Mermaid.

## To run the Django server for the first time:
```
python manage.py migrate
python manage.py createsuperuser --username=USERNAME --email=EMAIL
python manage.py generate_klantreis
python manage.py runserver
```
Replace `USERNAME` and `EMAIL` with your desired username and email, type a password at the prompt and press enter.
That last command will create a hardcoded (for expediency) client journey.
Now visit `http://127.0.0.1:8000/core/process_view/1/` (assuming you started with no database). Note you will need an internet connection when you run this because this demo app uses a CDN to access the Mermaid.js Javascript.

The next time you want to start Django the `python manage.py runserver` command will suffice.

## Run test
```
python manage.py test
```


