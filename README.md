# macandang
A shared repo between Mac and Angie McCarthy

Mac and Angie, siblings numbering 2 and 4, are taking MIT's Intro to Python together starting
in January 2021. This is their shared repo. 

# Initial Git Etiquette

1) Work in a branch for yourself, possibly even making your own directory. Within terminal of your choice:
  `git checkout -b ${branch_name}`
  
   - Make changes etc and save
   
   `git status` shows the different changes done.
   
   `git add .` adds all files changed. `git add ${file_name.py}` adds that specific file.
   
   `git commit -m "I made changes. I can say whatever here, whether vague or descriptive"` commits the changes to be pushed up to the repo.
   
   `git push`
   
  
2) This is when the other person merges the changes within the Github GUI. Probably easiest.

3) Now both people pull down those most recent changes.

  `git pull` or `git pull origin main`
  
# on Python Environments...

Read this for more info: https://realpython.com/effective-python-environment/

Personally, I like virtualenv.

1) Within your python project, do `pip install virtualenv`

2) `virtualenv env` declares an environment. Make sure you're running python3 by doing `python --version` in terminal. I get:

```
(base) ➜  macandang git:(unit1) ✗ python --version
Python 3.8.3
```

3) Activate the environment `source ./env/bin/activate` and go ahead and download any packages you want with `pip install ${package_name}`

4) When done, do `deactivate` 


