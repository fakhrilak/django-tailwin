from django.shortcuts import render
import tweepy
from .forms import Country,Tweet
consumer_key = "HNPoEf2wfLgr8BLNvELQ57QBx"
consumer_secret = "LwNnY7F3R5cDQXl8F0jvWWWjiuB9LLT2yGfYjcnNmohghiVyYL"
access_token = "1431351007825444864-ZYg7cRy8FTjxVEABGeDhSWReyHvkAe"
access_token_secret = "4J2uw8OsWHKWf2r13Skn59CfrMscJbRtjMiRIPvNzYk6y"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tranding = [
      ["req trending", "/twitter?type=trending&place=indonesia"], 
      ["res not availabe route", "html response, back to '/' route"], 
      ["res not available place", {
        "message": "not found", 
        "status": 400}], 
      ["res success ",{
        "data": "response data tranding twitter", 
        "message": "response Message", 
        "status": "response status"
      }]
    ]

user= [
      ["req user","/twitter?type=user&name=jokowi"], 
      ["res not found user",{
        "message": "Not found user", 
        "status": 500}], 
      ["res success",{
        "data": "response data profile twitter", 
        "message": "response message", 
        "status": 200
      }]
    ]
tweet = [
      ["req tweet", "/twitter?type=tweet&tweet=vcs&length=50"], 
      ["res fail",{
        "message": "response message", 
        "status": 500
      }], 
      ["res success",{
        "data": "array tweet dengan panjang, berdasarkan length. jika legth kotong default 10, max = 100", 
        "messages": "response message", 
        "status": 200
      }]
]

tweetId = [
      ["req tweetby id","/twitter?type=tweet&id=1438491648699236357"], 
      ["res fail",{
        "message": "response message", 
        "status": 500
      }], 
      ["res success",{
        "data": "data tweet by id", 
        "message": "response message", 
        "status": 200
      }]
]
# Create your views here.
def index(request):
    context={
        "twitter" : [
            {
            "value" : tranding,
            "name" : "Get Tranding Twitter"
            },
            {
            "value" : user,
            "name" : "Get User Twitter"
            },
            {
                "value" : tweet,
                "name"  : "Get Tweet Twitter"
            },
            {
                "value" : tweetId,
                "name"  : "Get Tweet by ID"
            }
        ]
    }
    return render(request,"twitter/index.html",context)

def tranding(request):
  context = {
    "country_form" : Country
  }
  x = api.trends_available()
  context["tranding"] = x
  if request.method == "POST":
    country = request.POST["country"]
    country = country.title()
    for i in x:
      if(i["name"] == country):
        y = api.trends_place(i["woeid"])
        print(i["woeid"])
        context["country"] = y
  return render(request,"twitter/tranding.html",context)

def tweet(request):
  context={
    "tweet_form" : Tweet
  }
  if request.method == "POST":
    tweet = request.POST["tweet"]
    tw = tweepy.Cursor(api.search,
                        q=tweet,
                        lang="in",
                        ).items(100)
    data = []
    for i in tw:
      print("========================================")
      data.append(i._json)
    context["tweet"] = data
  return render(request,"twitter/tweet.html",context)