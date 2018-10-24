# 

## Before start
Ensure you have installed some python interpreter (**python3** is suggested, and **Anaconda** is quite well for data 
engineering and data science). Also is required having **pip** installed.

## Package management using Pipenv
Usually, python developers use **pip** and put all required dependencies into some **requirements.txt** of directly into
the package python file, **setup.py**. This may lead to some bad habits, mainly due to developers don't want to handle
with different **virtualenvs** for different applications, so that, messy package management related problems happens.

So that, this tutorial is going to introduce **pipvenv**, that is a tool focus on make easy to deal with virtualenvs 
and package management, making easy to introduce to python those developers coming from other languages like *Java* or
*Javascript* (if you really consider it as a programming language). You can read a lot of this tool here: TODO add link 

For install pipenv just run following:

    pip install --user --upgrade pip, pipenv

Then you'll ready to create some new python virtualenv (i.e. python3.6) just running following

    pipenv --python 3.6

Just then, you could see some new *Pipfile* that will include all required virtualenv and packages information

    [[source]]
    url = "https://pypi.org/simple"
    verify_ssl = true
    name = "pypi"
    
    [packages]
    
    [dev-packages]
    
    [requires]
    python_version = "3.6"

Next step is installing those packages required by you application running following:

    pipenv install flask flask-graphql pandas requests

Then, all dependencies will be installed on your virtualenv, and they'll be reflected into the *Pipfile* too:

    [[source]]
    url = "https://pypi.org/simple"
    verify_ssl = true
    name = "pypi"
    
    [packages]
    flask = "*"
    flask-graphql = "*"
    pandas = "*"
    requests = "*"
    
    [dev-packages]
    
    [requires]
    python_version = "3.6"

Another good thing is that we can separate testing and application dependencies just using --dev flag, for instance:
 
     pipenv install --dev behave nose
 
So your *Pipfile* will look like following:
 
    [[source]]
    url = "https://pypi.org/simple"
    verify_ssl = true
    name = "pypi"
    
    [packages]
    flask = "*"
    flask-graphql = "*"
    pandas = "*"
    requests = "*"
    
    [dev-packages]
    nose = "*"
    behave = "*"
    
    [requires]
    python_version = "3.6"

This is really good because we can later dump testing and application dependencies in separated *requirement.txt* files,
that is really useful when you want to create minimal Docker images, or just when you need to run test. For instance:


    # Create application requirements
    pipenv lock -r > requirements.txt

## Creating your first Flask Application.
Initially, flask expect using a common folder structure like following:

    app/
        ->templates/ # All Jinja2 templates will come in this directory
        ->static/    # All static assests will come in this directory
        ->...        # Any other python classes you may require
 
There are several ways of building some *Flask* application, but preferred approach is using some factory method that
will manage all the configuration stuff in order to make it simple. A best place for including the factory method is at
the **__init__.py** file, so, we're going to create the factory there:

    from flask import Flask
    
    def create_app():
        app = Flask(__name__)
        return app  

Now, we have a nice application that does ... nothing, so, let's gonna some functionality, specially some API and some
frontend, so, let's gonna .


## How to run some Flask application.
In case you want to control the environment variables are going to be included in your virtualenv, just add a file named
**.env** at the same place you have created the **Pipfile**. For instance, we will need FLASK_APP variable set in order
to run our Flask application, so that, we will create some **.env** file with this:

    FLASK_APP=app

Other good thing about **pipenv** is that virtualenv is not installed on the folder, so that, your project won't be mess
(that is quite good for that infamous people that like running git add -A and git commit without looking the changes ).
Thus, you can run any installed module installed in the virtualenf just using *pipenv run*. For instance, if we want to
run our BDD test writen with **behave** package, you just need to type:

    pipenv run behave

Other example is running some flask application is as easy as running following:
 
    pipenv run flask run

