# Python virtual environments are used to create an isolated environment for Python projects.
# This means that each project can have its own dependencies, regardless of what dependencies every other project has.
#
# Virtual environments are very useful for:
# - Isolating different projects, with different dependencies, on the same machine
# - Isolating different versions of Python on the same machine
# - Isolating packages installed with pip
#
# To create a virtual environment, go to your project folder, and run the venv module:
# python -m venv myenv 
# typically I use
# python -m venv venv
# good idea to add venv to .gitignore
# This will create a folder called myenv, with all the necessary executables to use the packages that a venv contains.
# To start using the virtual environment, it needs to be activated:
# myenv\Scripts\activate
# on Powershell
# myenv\Scripts\Activate.ps1
# Now, any package that you install using pip will be installed in the myenv folder, isolated from the global Python installation.
# To deactivate the virtual environment, simply close the terminal.
# To delete the virtual environment, just delete the myenv folder.
#
# To create a virtual environment with a specific version of Python, use the -p parameter when creating the virtual environment:
# python -m venv myenv -p python3.7
# This will create a virtual environment that uses Python 3.7.

# we will stick with default python version for now.

# To list all the packages installed in the virtual environment, use the pip list command:
# pip list
# To install a package in the virtual environment, use the pip install command:
# pip install camelcase
# To uninstall a package in the virtual environment, use the pip uninstall command:
# pip uninstall camelcase

# To freeze the current state of the virtual environment, and generate a requirements.txt file with all the current packages and their versions, use the pip freeze command:
# pip freeze > requirements.txt
# This will create a file called requirements.txt, containing a list of all the packages installed in the virtual environment, and their version numbers.
# To create a new virtual environment, and install all the packages listed in the requirements.txt file, use the pip install command:
# pip install -r requirements.txt
