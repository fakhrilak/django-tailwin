from django.shortcuts import render
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