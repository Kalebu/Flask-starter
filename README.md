# [Flask-Starter](#)

**Flask-starter** is a Minimal starter for your flask project that implement some boiler plate code for you so as you could focus on the core functionality of your project.

<img src="flask.webp" width="300" height="200">

## Features to Implemented

- Backend
  - [x] Flask-Blueprint
  - [x] Flask-SQLAlchemy
  - [x] Flask-Migrate
  - [ ] Flask-Login
  - [ ] Flask-MarshMallow

- User Interface(UI)
  - [ ] Home page
  - [ ] Signup page
  - [ ] Signin Page
  - [ ] Sample CMS Page

## How to run

```bash
git clone https://github.com/Kalebu/Flask-starter
cd Flask-starter
Flask-starter-> pip install -r requirements.txt
Flask-starter-> python route.py
```


## Migrating database 
Once you modified the models codebase to mirror the change to the database without deleting it, use *flask migrate*, but before we do that we need to tell flask where entry script is located;

### For window user do this

```bash
set FLASK_APP = route.py
flask db migrate
flask db upgrade
```
### Linux Users do this instead

```bash
export FLASK_APP = route.py
flask db migrate
flask db upgrade
```

## Contributions

This is an open source project therefore I welcome all contributors to adding and modifying the starter to make it more friendly and elegant. Just Fork it !!

## Credits

All the credits to [Kalebu](https://github.com/kalebu) and other future contributors
