# Auto-GitRepo-Creator&Remover

Automated python script to ease the creation and deletion of local and remote repositories.

### Install:
```bash
git clone https://github.com/InbaKrish/PyProjectInitialization.git
cd PyProjectInitialization
pip install -r requirements.txt
```
Make sure to download chromedriver.exe and having it on the same directory.

### Execute:
```bash
cd PyProjectInitialization
python create.py
```
or
```bash
cd PyProjectInitialization
python remove.py
```
By default,Runs Vscode after repo creation, you can disable by altering create.py

By default it asks username and password for every executions .
You can alter accordingly in usercredentials.py file.
