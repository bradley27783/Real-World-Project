--PACKAGES NEEDED--
Flask - pip install flask
Flask WTForms - pip install flask-wtf

--Run on Windows--
set FLASK_APP=webapp.py
set FLASK_DEBUG=1
flask run --host=0.0.0.0

--Run on Linux--
export FLASK_APP=webapp.py
export FLASK_DEBUG=1
flask run --host=0.0.0.0
