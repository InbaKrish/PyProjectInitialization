import os
from github import Github
from usercredentials import *

path = os.getcwd() 
un = un 
pwd = pwd
fname  = fname

def remoterepo():

    user = Github(un, pwd).get_user()
    repo = user.create_repo(fname)
    print("\nCreated repository ", fname)
    return str('https://github.com/' + str(un) +chr(47) +str(fname) + '.git')
    
if __name__ == "__main__":
    rem = remoterepo()
    cm = 'git remote add origin '+ str(rem)
    local = os.getcwd() + chr(92) + str(fname)
    os.chdir(os.getcwd())
    os.makedirs(local)
    os.chdir(local)
    print("\nGit initialising your local repo , ",local)
    os.system("git init")
    print("\nCreating README.md file in , ",local)
    os.system("type NUL > README.md")
    print("\nStaging all files")
    os.system("git add .")
    print("\nMaking initial commit...")
    os.system('git commit -m "first commit"')
    print("\nPushing your current local repository to remote repo..",fname)
    os.system(cm)
    os.system("git push -u origin master")
    print("\n\t------------SUCCESSFULLY created Git local & remote repositories--------------")
    print("\n\t\tOPENING VSCODE")
    os.system("code .")
    
