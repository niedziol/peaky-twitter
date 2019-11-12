# peaky-twitter

Django app inspired by Twitter for academic purposes.

To run this app you should:
* clone this repo
```
git clone git@github.com:niedziol/peaky-twitter.git      # ssh
git clone https://github.com/niedziol/peaky-twitter.git  # https
```

* activate virtual environment
```
virtualenv -p python3 venv
. venv/bin/activate
```

* install requirements
```
pip install -r requirements.txt
```

* navigate to project folder
```
cd peaky_twitter
```

* create a secret key
```
echo "itsasecretdontlook" > secret.txt
```

* run migrations
```
python manage.py migrate
```

* run server
```
python manage.py runserver
```

* go to [this url](http://127.0.0.1:8000/tweets/) to see the results