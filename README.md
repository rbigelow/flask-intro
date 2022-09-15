# Setup Instructions

This code sample demonstrates how setup a simple Flask application  using application virtualization.

## 1) Install Python and a code editor.

Follow the directions for your operating system here
https://www.python.org/ 

Personally I recommend  Visual Studio Code as a editor but there are also many others.
https://code.visualstudio.com/


## 2) Create a project directory.
 `mkdir MyWebApp` (Mac/Linux) or `md MyWebApp`  (Windows)
 `cd MyWebApp`

## 3) Create the virtual engironment.

`pip3 install pipenv`   This will install the virtual environment package on your computer. 
`pipenv install`        This will create a virtual environment.
`pipenv shell`          This will start the virtual environment. 
`exit`                  This will close (exit) the virtual environment.
`pipenv shell`          You can run this any time to restart the virtual environment. 

```
If you get an error. It could be because you have multiple version of Python installed. If this applies to you try add "python3 -m" to the commands.

`python3 -m  pip3 install pipenv
python3 -m  pipenv install
python3 -m pipenv shell 
```

## 4) Install Flask 

This will install the flask package to the virtual environment.
`pipenv install flask`          
Test the flask command to see if it installed properly.  
`flask`                         


## 4) Build the application.

Create the `app.py` file and in this example the `templates\hello.html` file. 

## 5) Run the application.
    
 Use `flask run` at the command prompt to launch the application.

## 6) Enable debug mode and troubleshooting.

Flask uses a couple of command line environmental variables. The `FLASK_APP` variable sets the name of the python script to run. and `FLASK_ENV` can be used to put Flask into development mode which will provide better debug messages and enable auto-reload when you make file changes. Which means you don't need to stop and start Flask every time you make a change. 


For Linux and Mac users you can set the variables like this. 
```
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run
```

In Windows Powershell

```
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
flask run
```
 
