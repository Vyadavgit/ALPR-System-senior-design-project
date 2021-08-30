# ALPR-System-senior-design-project
<b>The University of Texas at Arlington - Fall 2021 CSE4316/4317 Seior Design Project.</b>

<b>Team members:</b><br>
Siddharth Gautam<br>
Vivek Kumar Yadav<br>
Bishal Shrestha<br>
Pranay Shakya<br>
Anil Bhui<br>

<b>Instructions to setup and run this project:</b>
1. Clone the project using the command ***git clone https://github.com/Vyadavgit/ALPR-System-senior-design-project.git***
2. Create virtual environment using command ***python -m venv <name_of_virtualenv>*** and activate it to install project requirements in it.
3. Navigate to requirements.txt file and install all the requirements in the virtual environment using the command ***pip install -r requirements.txt*** (Please make sure to install 'pip' first if it is not already installed in your system.)
4. Install Tesseract-OCR in the 'site-packages' folder of your virtual environment using app installer (using the command line may install Tesseract-OCR somewhere else than your virtual environment) and provide path to it in 'license/views.py' file for the license detection and OCR program to function properly.
5. After installation of cv2 (it may have been already installed while you installed using requirements.txt) in your virtual environment, provide path to CascadeClassifier file 'haarcascade_russian_plate_number' located at "<name_of_virtualenv>/Lib/site-packages/cv2/data/" in your 'license/views.py' file.
6. Uncomment and use default sqlite3 database given in the settings file ( http://127.0.0.1:8000/admin gives you the admin interface for this database. To access it create admin username and password using the command ***python manage.py createsuperuser*** by navigating to manage.py file):



        # sqlite3 database
        DATABASES = {
         'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
         }
        }

OR install the postgres database first on your PC and use it as given in the settings file:
```
# POSTGRES DATABASE LOCAL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '***',
        'USER': '***',
        'PASSWORD': '***',
        'HOST': '***',
        'PORT': '***'
    }
}
```
7. To enable forget you password edit SMTP Configuration inside settings.py      
### Enable Forget password     

```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '___your_email_host__'
EMAIL_PORT = '__port_number__'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '__username__'
EMAIL_HOST_PASSWORD = '__password__'

```

8. Use following program compilation and run commands to run the project: <br>
Migrations command: <br>
***python manage.py makemigrations*** <br>
***python manage.py migrate***<br>
Run server command:  ***python manage.py runserver***


9. Visit server http://127.0.0.1:8000/ to visit the ALPR System web app.
10. Press key 's' to save the recognized license plate.
11. Press key 'd' to terminate the license detection program.


### Info for contributers:

Always use this command before creating a branch/writing your code:  
	***git pull*** :- command to pull the updated source code from the repository.<br />

Always create and work on a new branch if you are working on a new feature:<br />
	***git branch BRANCHNAME*** :- command to create a new branch<br />
	***git checkout BRANCHNAME*** :- command to switch to a different branch<br />

After you are ready to push a new feature/ready to update code follow commands below:<br />
	***git add .*** :- command to add your modifications<br />
	***git commit -m "WRITE A SHORT DESCRIPTION ABOUT MODIFICATIONS/FEATURES YOU ADDED"*** :- command to add short description<br />
	***git push*** :- command to push your code to repo [Please push it to your branch]<br />
	<br />
Other git commands:<br />
	***git checkout master*** :- command to switch to master branch<br />
	***git status*** :- command to check your current status <br />
	***git branch*** :- command to list available branches<br />
	***git branch BRANCHNAME -D*** :- command to delete branch<br />

Create virtual environment: 
***python -m venv <name_of_virtualenv>***
<br>
Create/update requirements.txt: ***pip freeze > requirements.txt***
<br>
Install requirements.txt: ***pip install -r requirements.txt***

Program compilation instructions:
<br><br>
Migrations command: <br>
***python manage.py makemigrations*** <br>
***python manage.py migrate***

Run server command: ***python manage.py runserver***
<br>

***IMPORTANT NOTES:*** 
1. Install Tesseract-OCR in the 'site-packages' folder of your virtual environment and provide path to it in 'license/views.py' file for the license detection and OCR program to function properly.
2. After installation of cv2 in your virtual environment, provide path to CascadeClassifier file 'haarcascade_russian_plate_number' located at "<name_of_virtualenv>/Lib/site-packages/cv2/data/" in your 'license/views.py' file.
3. Press key 's' to save the recognized license plate.
4. Press key 'd' to terminate the license detection program.

***References and Credits:***
1. https://www.youtube.com/watch?v=xv_bwpA_aEA&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO
2. https://www.youtube.com/watch?v=WQeoO7MI0Bs
3. https://bootstrapmade.com/demo/Regna/
