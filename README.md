# README

##### Requirements & Installation:

 * Mysql
 * Python 2.7 or higher and python-dev too. Run `sudo apt-get install python-dev`
 * Change the mysql user and password in `settings.py`

##### How to Run:
 * Run `pip install -r requirements.txt`, preferably in a virtual environment. If you get any mysql error, run this `sudo apt-get install libmysqlclient-dev`
 * Create database `signzy` and run `python manage.py migrate`
 * Run `python manage.py insert_in_db`
 * Run `python manage.py runserver`
 * You can test it now on `http://localhost:8000/search/`

If something doesn't work as expected then please feel free to contact me.

#### Note:
If you don't want to do all this, I can show it to you live via localtunnel. Contact me if this is the case.
