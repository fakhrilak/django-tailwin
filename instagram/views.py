from django.shortcuts import render
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
    value = 0
    context={
        "instagram" : [
            {
            "value" : user,
            "name" : "Route get User"
            },
        ]
    }
    return render(request,"instagram/index.html",context)