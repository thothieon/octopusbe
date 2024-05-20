
#!/bin/sh
python3 manage.py makemigrations
python3 manage.py migrate
sudo rm -r staticfiles
python3 manage.py collectstatic







