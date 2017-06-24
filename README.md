# COP4710
Database Systems Project 



1. In settings you will need to change:


		DATABASES = {
	    'default': {
	        'ENGINE': "django.db.backends.mysql",
	        'NAME': 'rso_system',					//make sure this database exists on your system 'create database rso_system;'
	        'USER': 'hunter',						//change to a user on your system
	        'PASSWORD': 'password',					//change to the password of the above user
	        'HOST': '',
	        'PORT': '',        
	    }
	}