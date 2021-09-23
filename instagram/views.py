from django.shortcuts import render
from .forms import User
import requests
import re
import json
user = [
        ["note", "untuk page 0 tidak membutuhkan token, page selanjutnya ditentukan oleh req sebelumnya. token berada di resPage_info.end_cursor, di fild ini juuga menentukan untuk request nextnya dapat dilakukan atau tidak dari keterangan resPage_info.has_next_page. jika tidak true maka postingan hanya sampai di situ"], 
        ["req_user", "/instagram?type=user&name=jokowi&page=0"], 
        ["res_fail_not_available_paginate", {
            "message": "losing paginate", 
            "status": 400
        }],
        ["res_fail_not_available_user",{
            "message": "Not found User", 
            "status": 500
        }], 
        ["res_success",{
            "id": "user ID Instagram", 
            "message": "response Message", 
            "resPage_info": "jika resPage_info menyatakan bisa di lakukan next, maka parameters harus dirubah /instagram?type=user&name=jokowi&page=1&token=resPade_info.end_cursor", 
            "resPost": "post in page query", 
            "resProfile": "InfoProfile", 
            "status": 200
        }]
    ]

# Create your views here.
def instagram(request):
    context={
        "instagram" : [
            {
            "value" : user,
            "name" : "Route get User",
            "route": "user/"
            },
        ]
    }
    return render(request,"instagram/index.html",context)
def detailPost(request,id):
    context = {
        "id":id
    }
    end_cursor = ''
    urlCommand = ''
    with requests.session() as s:
        s.headers['user-agent'] = 'Mozilla/7.0'
        url = "https://www.instagram.com/p/"+id
        r    = s.get(url, params={'max_id': end_cursor})
        data = re.search(
                r'window._sharedData = (\{.+?});</script>', r.text).group(1)
        data =  json.loads(data)
        # headers = {'User-Agent': 'Chrome'}
        # xx =  requests.request('GET','https://www.instagram.com/graphql/query/?query_hash=bc3296d1ce80a24b1b6e40b1e72903f5&variables={"shortcode":"CUE8D8ch_0u","first":12}',headers=headers)
        print(data["entry_data"])
        # command = json.loads(command.text)
        # context["token"] = command["data"]["shortcode_media"]["edge_media_to_parent_comment"]["page_info"]["end_cursor"],
        # context["commandCount"] = command["data"]["shortcode_media"]["edge_media_to_parent_comment"]["count"]
        # context["likeCount"] = data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_preview_like"]["count"]
        # context["captions"] = data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_to_caption"]["edges"][0]["node"]["text"]
        # context["pict"] =  data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["display_resources"][2]["src"]
        # context["detailCommand"] = command["data"]["shortcode_media"]["edge_media_to_parent_comment"]["edges"]
    # if request.method == "POST":
    #     token = request.POST["token"]
    return render(request,"instagram/detailPost.html",context)
def getUser(request):
    firstPage = "d4d88dc1500312af6f937f7b804c68c3"
    nextPage = "8c2a529969ee035a5063f2fc8602a0fd"
    postCode = []
    context ={
        "user" : User
    }
    if request.method == "POST":
        name = request.POST["name"]
        token = request.POST["token"]
        print(token,"ini token")
        url = "https://www.instagram.com/"+name
        with requests.session() as s:
            s.headers['user-agent'] = 'Mozilla/7.0'
            end_cursor = ''
            tol=""
            global j,x,profile,postingan
            r    = s.get(url, params={'max_id': end_cursor})
            data = re.search(
                r'window._sharedData = (\{.+?});</script>', r.text).group(1)
            j = json.loads(data)
            x = j["entry_data"]["ProfilePage"][0]["graphql"]["user"]
            if len(token) > 0:
                tol = f'https://www.instagram.com/graphql/query/?query_hash='+nextPage+'&variables={"id":'+x["id"]+',"first":12,"after":"'+token+'"}'
            else :
                tol = f'https://www.instagram.com/graphql/query/?query_hash='+nextPage+'&variables={"id":"'+x["id"]+'","first":12}'
            headers = {'User-Agent': 'Mozilla'}
            postingan = requests.get(tol,headers=headers)
            xxx = json.loads(postingan.text)
            xnxx = xxx["data"]["user"]["edge_owner_to_timeline_media"]["edges"]
            token = xxx["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"]
            for i in xnxx:
                postCode.append({"postcode":i["node"]["shortcode"],"thumbnail":i["node"]["display_url"],
                "commandCount":i["node"]["edge_media_to_comment"]["count"],"captions":i["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"],
                "like":i["node"]["edge_media_preview_like"]["count"]
                })
            context["userId"] = x['id']
            context["message"] = x['id']
            context["postCode"] = postCode
            context["pageInfo"]= xxx["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]
    return render(request,"instagram/getUser.html",context)