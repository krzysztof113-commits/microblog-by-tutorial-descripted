import os

# abspath is a function that gives like that in default be e.g. /templates or /
# we need a full path so as an argument needs to be name of our project directory, we can use the magic function
# We are using os.path instead of manually typing or most important joining things because there can be different
# paths for windows, linux, macos etc.
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	# An environment variable is a variable whose value is set outside the program,
	# typically through functionality built into the operating system or microservice.
	# Here is cryptographic key that is used by many applications and flask extensions (e.g. tokens or signatures).
	# WTForms uses it to encrypt against Cross-Site Request Forgery (CSRF) attacks. Only admins know the key.
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	# configs for databases - SQLAlchemy
	# I added (...) + '?check_same_thread=False' so I don't have session multithread security errors
	SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')) \
							  + '?check_same_thread=False'
	# this one makes some flask errors or maybe additional steps, warnings if changing databases so we turn it off
	SQLALCHEMY_TRACK_MODIFICATIONS = False
