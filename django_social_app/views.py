from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from forms import StatusForm
from utils import get_api
import tweepy

# from django.template.context import RequestContext
def login(request):
    auto_update_period_in_min = (
        settings.USER_TIMELINE_AUTO_UPDATE_PERIOD / (1000.0 * 60.0)) % 60.0
    pagedata={
              'auto_update_period_in_min':auto_update_period_in_min
             }
    return render_to_response('login.html',  {'pagedata': pagedata}, context_instance=RequestContext(request))


@login_required(login_url='/')
def home(request):
#    import pdb;pdb.set_trace()
    #trying to get all the friends, followers and tweets of the looged in user
    try: 
        #key to determine whether it's a auto update request or not
        if 'auto_update' in request.GET:
            auto_update = request.GET['auto_update']
        else:
            auto_update = False
        can_auto_update = settings.ALLOW_AUTO_UPDATE
        is_update = False
        api = get_api(request.user)
        user_details = api.get_user(request.user)
        world_wide_trend = get_world_wide_trends(api)
        timeline = get_all_tweets(api, user_details.screen_name)
        followers_count = user_details.followers_count if user_details.followers_count > 0 else 0
        following_count = user_details.friends_count if user_details.friends_count > 0 else 0
        status_count = len(timeline)
        #creating the session variable for the first time when the user logged in
        if 'followers_count' not in request.session:
            request.session['followers_count'] = followers_count
        if 'following_count' not in request.session:
            request.session['following_count'] = following_count
        if 'status_count' not in request.session:
            request.session['status_count'] = status_count
        #determining whether there is update at the interval of auto update frequency mentioned in settings
        if followers_count != request.session['followers_count'] or \
           following_count != request.session['following_count'] or \
           status_count != request.session['status_count']:
            is_update = True
        #if there is a update, updating the session variables to the latest values
        if is_update:
            request.session['followers_count'] = followers_count
            request.session['following_count'] = following_count
            request.session['status_count'] = status_count
        profile_image_url = timeline[0].author.profile_image_url if len(
            timeline) > 0 else user_details.profile_image_url
        pagedata={
                   'can_auto_update':can_auto_update,
                   'auto_update':auto_update,
                   'user_details': user_details,
                   'auto_update_period':settings.USER_TIMELINE_AUTO_UPDATE_PERIOD,
                   'followers_count': followers_count,
                   'friends_count': following_count,
                   'followers': tweepy.Cursor(api.followers, screen_name=request.user).items(),
                   'following': tweepy.Cursor(api.friends, screen_name=request.user).items(),
                   'status': len(timeline),
                   'world_wide_trend':world_wide_trend,
                   'timeline': timeline,
                   'profile_image_url': profile_image_url,
                   'is_update': is_update
                 }
        return render_to_response('home.html',
                                  {
                                   'pagedata':pagedata
                                   },
                                  context_instance=RequestContext(request))
    #if there is error in above try, trying to get the latest 20 friends, 20 followers  which is by default the twitter Api can allow and all tweets
    except tweepy.TweepError as e:
        try:
            pagedata['followers']=user_details.followers()
            pagedata['following']=user_details.friends()
            pagedata['timeline']=timeline[20]
            return render_to_response('home.html',
                                  {
                                   'pagedata':pagedata
                                   },
                                context_instance=RequestContext(request))
        # if again there is error, returns the error page to the users stating the error rason
        except tweepy.TweepError as e:
               error_message = e.message[0]['message']
               error_code = e.message[0]['code']
               return render_to_response('error.html',{'error_message':error_message,'error_code':error_code}, context_instance=RequestContext(request))

                            


@login_required(login_url='/')
def logout(request):
    auth_logout(request)
    return redirect('/')

#@login_required(login_url='/')

def get_world_wide_trends(api):
    #import pdb;pdb.set_trace()
    trends = api.trends_place(1)
    # trends1 is a list with only one element in it, which is a 
    # dict which we'll put in data.
    data = trends[0] 
    # grab the trends
    trends_data = data['trends']
    # grab the name from each trend
    #trend_names = [trend['name'] for trend in trends_data]
    return trends_data
    

def get_all_tweets(api, screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method
    # authorize twitter, initialize tweepy
    # initialize a list to hold all the tweepy Tweets
    alltweets = []
    # make initial request for most recent tweets (200 is the maximum allowed
    # count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    if len(new_tweets) > 0:
        # save most recent tweets
        alltweets.extend(new_tweets)
        # save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        # keep grabbing tweets until there are no tweets left to grab
        # if already grabbed tweets is less than 200, then the total tweets would less than 200 so need to go furhter
        if len(new_tweets) == 200:
            while len(new_tweets) > 0:
                # all subsiquent requests use the max_id param to prevent
                # duplicates
                new_tweets = api.user_timeline(
                    screen_name=screen_name, count=200, max_id=oldest)
                # save most recent tweets
                alltweets.extend(new_tweets)
                # update the id of the oldest tweet less one
                oldest = alltweets[-1].id - 1
    return alltweets


@login_required(login_url='/')
def post_tweet(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = StatusForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            api = get_api(request.user)
            status_to_update = form.cleaned_data['Tweet']
            api.update_status(status=status_to_update)
            return HttpResponseRedirect('/home/')  # Redirect after POST
    else:
        form = StatusForm()  # An unbound form

    return render(request, 'status_update.html', {
        'form': form,
    })


@login_required(login_url='/')
def delete(request):
    if request.method == 'GET':
        delete_tweets = request.GET.get("delete_tweets")
        delete_skill = delete_tweets.split(',')
        api = get_api(request.user)
        for each_tweet in filter(None, delete_skill):
            api.destroy_status(id=each_tweet)
    return HttpResponseRedirect('/home/')
