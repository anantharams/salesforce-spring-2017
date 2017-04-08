python
====

For this class (and Python use in general), your life will be much easier if you aren't mucking around with your system Python installation. The folks in the open source community have come up with a great solution: virtual Python environments. 

This is accomplished via [`virtualenv`](https://virtualenv.readthedocs.org/en/latest/) and augmented with [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.org/en/latest/).  

Advantages:

* No more destroying your system Python just to get a single project to work
* Easily allow different projects to have differnt versions of libraries and coexist peacefully
* Easy command line tools to create, switch, and destory `virtualenv`s

Additionally, `virtualenv` plays very nice with Python's package installer, `pip`.

Let's start by getting you up and running with Python & `pip`.

# Installation

Start by pulling down the repository, either using git or downloading the ZIP. 

Next, use the section appropriate for your OS for the installation. After you're finished, you'll move to setting up environments.  

## Mac OS X Installation

You will need Python 2.7.x. If this command doesn't work:

	$ python --version

You'll need to install it. [Simply download and install from here](https://www.python.org/downloads/).

There's a good chance you already have `pip` installed, check with:

	$ pip --version

Visit the `pip` [website for instructions](https://pip.pypa.io/en/stable/installing/). Most likely you'll download a Python script and run it:

	$ python get-pip.py

Now you should have working Python 2.7.x and `pip` installed. Skip to below to setup `virtualenv`s.

## `virtualenv` & `virtualenvwrapper` Setup

Install virtualenv libs at system level:

	$ sudo pip install virtualenv
	$ sudo pip install virtualenvwrapper

This should be the last time you ever use `sudo pip ...`!

Put into your `~/.bash_profile` (Mac OSX) or `~/.bashrc` (Linux):

     # for virtuallenvwrapper
     export WORKON_HOME=$HOME/.virtualenvs
     source /usr/local/bin/virtualenvwrapper_lazy.sh
	
Then initialize it:

	$ source ~/.bash_profile
	$ workon

This ensures whenever you start a new shell, you'll be able to get up and running with virtual environments if you want to. Then to create an environment:

	$ mkvirtualenv temp
	$ workon # should now display our env!
	temp
	$ workon temp
	(temp)$ pip install requests # now we’re in!
	(temp)$ python
	>>> import requests  # it worked!
	(temp)$ deactivate
	$ python
	>>> import requests
	ImportError: No module named requests  # we're not in our environment anymore!
	$ rmvirtualenv temp
	removing...

Great, you can now create new environments, destroy old ones, and manage existing ones! 

## Installing packages

Let's create the environment specific to this class. 

	$ cd /path/to/this/repo
	$ mkvirtualenv di
	$ workon di
	(di)$ pip install -r /path/to/requirements.txt

And if you don't see any errors, you're ready to go!
