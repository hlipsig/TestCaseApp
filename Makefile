# Makefile 
#show hidden characters to understand syntax
all: pip vsetup von
pip: 
	echo "watch me go"
	easy_install pip3
	pip3 install virtualenv

#Here we're setting up your virtual environment
#Here it's "Touch" but later you'll need to use source
vsetup: 
	virtualenv venv
	virtualenv -p /usr/bin/python3 venv
	touch venv/bin/activate
#Now your virtual environment is on
von: 
	pip install selenium
	pip install nose
	echo "I am a leaf on the wind... Watch how I soar..."
