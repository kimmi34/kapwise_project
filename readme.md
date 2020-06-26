Clone the project to your system

git clone https://github.com/kimmi34/kapwise_project

Required Installations

1. Install all the required dependencies in your virtual environment using requirements.txt file.

pip install -r requirements.txt


2. Install MySQL

As we are using MySQL as our database, installation of mysql is mandatory.
Run following commands for the same if it is not installed yet:

    sudo apt install mysql-server

In order to use MySQL with our django project,a Python 3 database connector library compatible with Django, is required. So, next we will install the database connector, mysqlclient.

    sudo apt install python3-dev 

    sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev

    pip install mysqlclient

Next, we will create a database in MySQL which will be used by django.


    sudo mysql -u root

    CREATE DATABASE kapwise_database;


Now , we will create our account, set a password, and grant access to the database we created.

    CREATE USER 'kapwise'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
    
    GRANT ALL ON kapwise_database.* TO 'kapwise'@'%';

    FLUSH PRIVILEGES;


3. Finally exit MySQL and run migrations in django project.

    python manage.py makemigrations
    
    python manage.py migrate

4. Run the server

    python manage.py runserver


Display and APIs

http://127.0.0.1:8000/
Above url corresponds to home page which display the results fetched from various APIs.

5 APIs have been made. Their urls are in core/urls.py.
URLs are: 

1. To Fetch data from given api:
http://127.0.0.1:8000/get10usersfromapi/

2. To delete all the users:
http://127.0.0.1:8000/deleteallusers/

3. To delete user with a given id:
http://127.0.0.1:8000/deletegivenuser/2/

4. To retreive user with a given id:
http://127.0.0.1:8000/getgivenuser/id/

5. To post a new user:
http://127.0.0.1:8000/postuser/


Another api to view all users in the database:
http://127.0.0.1:8000/viewallusers/


Important note:

In settings.py, MySQL database is connected to django.
Make sure the name of database, and authentication credentials of user are same as you entered while creating database in mySQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'kapwise_database',
        'USER': 'kapwise',
        'PASSWORD': 'password',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

