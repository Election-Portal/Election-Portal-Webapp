[Election Portal Web App]
=========================

.. contents ::

Election Portal Web App
-----------------------
The Project Name is [Election Portal Web App]
[PROJECT_URL]

Prerequisites
-------------

Installing Python
~~~~~~~~~~~~~~~~~


This is a django app. Django is written in 100% pure Python code, so you’ll need to install Python on your system. Django requires Python 2.3 or higher.
If you’re on Linux or Mac OS X, you probably already have Python installed.

Type python at a command prompt (or in Terminal). If you see something like below, then Python is installed::


    > python
    Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
    [GCC 6.3.0 20170118] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
Otherwise, if you see an error such as "command not found", you’ll have to download and install `Python`_ 

.. _Python: http://www.python.org/download/
to get started. The installation is fast and easy.

Creating an isolated Python environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


A virtual environment (also called a virtualenv) is like a private box where we can stuff useful computer code into for a project
we're working on It is recommended that you use virtualenv to create isolated Python environments, so you can use different package versions for different projects, which is far more practical than installing Python packages system wide.

++++++
Linux
++++++

To install virtualenv::

    pip install virtualenv

After you install virtualenv, create an isolated environment with the following command::

    virtualenv myenvironment

Note: Here **myenvironment** can by any valid name you like.

Now, You created a virtual environment let's activate it:

To Activate::

    source myenvironment/bin/activate

Congratz, You created a new virtualenv.

Requirements.txt
~~~~~~~~~~~~~~~~~

This file consist all the dependencies of this app, for eg: django, pytz, PIL etc. To install all the dependencies, just type::
    
    pip install -r requirements.txt

Make Sure You have **active internet connection**

Now, All our dependencies are fullfilled.

#. In your terminal, Change Directory to the Base Directory of our website. i.e the folder which consist manage.py::

    cd ElectionPortalWebapp
#. Then::

    python manage.py collectstatic
    python manage.py makemigrations
    python manage.py migrate


#. To Run The Server::

    python manage runserver

#. `Click Here To Check If All Things Are Ready
.. _Click Here To Check If All Things Are Ready: http://127.0.0.1:8000/

This will install all the dependencies in your virtualenv. You can check this at site-packages folder of your virtualenv.



Product directory
-----------------

    TODO
