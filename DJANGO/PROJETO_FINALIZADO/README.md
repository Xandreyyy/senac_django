# Hello_Django2

Repository for studies & simulations.

## Every projects starts like this

## Start a Django Project

```md
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install django
django-admin startproject project .
```

## Configuring git

```txt
git config --global user.name 'YourName'
git config --global user.email 'your_email@gmail.com'
git config --global init.defaultBranch main
```

## Configuring .gitignore

```txt
git init
git add .
git commit -m 'Message'
git remote add origin https://github.com/jtigik/Hello_Django2.git
git push -u origin main
```

## Migrating Django DB

```txt
python manage.py makemigrations
python manage.py migrate
```

## Creating & modifying Django Super User password

```txt
python manage.py createsuperuser
python manage.py changepassword USERNAME
```
