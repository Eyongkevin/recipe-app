# Recipe App

 
## Overview
The base for this project was [Achievement #1](https://github.com/DavidJulianGit/Python) of the Python for Web Developers course on Career Foundry. 

The previous version had a very limited, text based UI. This new version is developed using the **Django** framework to offer a more user friendly, modern experience. 


## Features
- User Authentication, for secure user login system.
- Users can create, search, edit and delete recipes.
- Difficulty of a recipe is automatically calculated based on cooking time and number of ingredients.
- Show statistics and visualizations based on trends and data analysis.

## Project structure
This project uses a structure that deviates from the standard Django structure, but for good reason. 
The structure used and information about it can be found on it's [authors repository](https://github.com/Eyongkevin/django-boilerplate).

#### Makefile
In order to use the `Makefile` on a Windows OS, you can install `make` via the `chocolately` package manager.
1. Install chocolately directly with a Python installer or directly via https://chocolatey.org/install
2. Run your terminal (Windows key + cmd) as admin (right lick - run as administrator) and run the command 
    `choco install make`

#### A few hints to making the project structure work for you
1. Make sure you install all dependencies from the requirements files inside the `requirements` folder.
2. Update the Makefile and replace 'config' with the name of your project folder. (It's 'config' in the boilerplate)
3. All apps go into the `apps`folder
4. Inside each apps folder, you can find `apps.py`in which you need to add 'apps.' in front of the apps name so it says `name = 'apps.<app_name>'`
5. Make sure you check `base.py` and `dev.py` to replace 'config' with your '<your_projects_name'> 
6. Created apps are linked to the application/project in `base.py` inside the `CREATED_APP = ['apps.<app_name>']' list
