# Edit Dojo

## Local Setup
1. Clone this repository into local system and change the directory.
   
```sh
git clone https://github.com/jhkim105/django-editdojo.git
cd django-editdojo/
```
2. Install pip3 and pipenv.

```sh
pip3 install pipenv
```
3. Go into the virtual environment: 
   
```sh
pipenv install
pipenv shell
```
4. Apply migrations
   
```sh
python manage.py makemigrations
python manage.py migrate
```
