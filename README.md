# Django_Social_Project
Django Twitter API project

This application will show the logged in user timeline and auto update it by auto page refreshing at the rate of every specified(USER_TIMELINE_AUTO_UPDATE_PERIOD in settings) minutes. We can tweet from this application on clicking the tweet button in home page. we can also delete the selected tweet(s) from this application with the usage of Delete Tweets.

The application would be best viewed in 1024x768 (or) 1036x768 resolution

Requirements/Dependencies:
 
    Django==1.7.1
    python-social-auth==0.2.1
    tweepy==3.3.0

Twitter Authentication Keys

Create a new application at https://apps.twitter.com/app/new and make sure to use a callback url of http://127.0.0.1:8000/complete/twitter.

In the “django_social_project” directory, edit a file called config.py. Grab the Consumer Key (API Key) and the Consumer Secret (API Secret) from Twitter under the “Keys and Access Tokens” tab and add them to the config file like so:


SOCIAL_AUTH_TWITTER_KEY = 'update me'
SOCIAL_AUTH_TWITTER_SECRET = 'update me'

Please Follow these steps to run this project

1. Create and activate a virtualenv
2. Download, extract files.
3. Edit settings.py 
    give the value for USER_TIMELINE_AUTO_UPDATE_PERIOD by default, it would be 10 mts(600000ms),
    set the value for ALLOW_AUTO_UPDATE to either True or False to allow auto update(by default, it would be True)
4. Edit settings.py for your database settings
4. Edit config.py to add your twitter app Consumer Key and Consumer Secret
5. python manage.py migrate
6. python manage.py makemigrations 
7. Run python manage.py runserver
