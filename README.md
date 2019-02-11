To run this app all you need is to create python 3 virtual environment like the following:

_virtualenv --python=/usr/local/bin/python3.6 /opt/speaker_env_

Where --python sets the path to the python interpreter in your system. Then you need to activate virtual environment

by running the following:

_source /opt/speaker_env/bin/activate_

Afterwards, you need to change your working directory to the root of this project and run:

_pip install -r requirements.txt_

That would install all the dependencies needed to run this application.

Being in the project's root type the following to start the app:

_python ./web/app.py_

Web instance will be waiting for an incoming GET request to the http://127.0.0.1:8000/api/time url.

You can open this link in a web-browser or use a terminal with the following command:

curl http://127.0.0.1:8000/api/time

It is important to mention that this app is only a PoC and also that WEB API does not suit well 
this kind of application.