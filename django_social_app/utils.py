import tweepy

from django.conf import settings


def get_api(user):
    social = user.social_auth.get(provider=settings.SOCIAL_PROVIDER)
    access_token = social.extra_data['access_token']['oauth_token']
    access_token_secret = social.extra_data[
        'access_token']['oauth_token_secret']
    auth = tweepy.OAuthHandler(
        settings.SOCIAL_AUTH_TWITTER_KEY, settings.SOCIAL_AUTH_TWITTER_SECRET)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api
