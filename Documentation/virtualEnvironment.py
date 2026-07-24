'''Virtual Environment:
A virtual environment is a tool used to isolate specific python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages withou conflicts. This can be especially useful when you are working on projects that have conflicting packages that are not compatiable with each other.

To create a virtual environment in Python, you can use the venv module that comes with python.
python -m venv myenv 

Activate the virtual environment
.\myenv\Scripts\activate

Once the virtual environment is activated, any packages that you install using pip will be installed in the virtual environment, rather than in the global python environment. This allows to have a seperate set of packages for each projects, without affecting the packages installed in global environment. 

To deactivate virtual environment
deactivate'''

#The "requirement.txt" file
'''In addition to creating and activating a virtual environment, it can be useful to creating a requirement.txt file that lists the packages in the new environment.
To create a requirement.txt file, you can use the pip freeze command, which outputs a list of installed packages and their versions. For example:

Output the list of installed packages and their versions of the file 
pip freeze > requirements.txt 

To install the packages listed in the requirements.txt file, you can use the pip install command with the -r flag
pip install -r requiremets.txt

Using a virtual environment and a requirement.txt file can help you to manage the dependencies for your python projects and ensure that your projects are portable and can be easily set up on a new machine '''