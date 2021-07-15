# ALPR-System-senior-design-project

Info for contributers: <br />

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
<br>
Run server command: ***python manage.py runserver***
<br>

***IMPORTANT NOTES:*** 
1. Install Tesseract-OCR in the 'site-packages' folder of your virtual environment and provide path to it in 'license/views.py' file for the license detection and OCR program to work well.
2. After installation of cv2 in your virtual environment, provide path to CascadeClassifier file 'haarcascade_russian_plate_number' located at "<name_of_virtualenv>/Lib/site-packages/cv2/data/" in your 'license/views.py' file.
3. Press key 's' to save the recognized license plate.
4. Press key 'd' to terminate the license detection program.
