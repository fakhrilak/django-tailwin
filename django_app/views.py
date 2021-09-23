from django.http import HttpResponse
from django.shortcuts import render

def docs(request):
    print("hello")
    context = {"data" :[
        ["/instagram/","https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/600px-Instagram_icon.png","INSTAGRAM"],
        ["/twitter/","https://cdn-icons-png.flaticon.com/512/124/124021.png","TWITTER"]
    ]}
    return render(request,"Index.html",context)

