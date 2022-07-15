from django.shortcuts import redirect, render, HttpResponse
from .models import Result

def hello(request):
    data = Result.objects.all()
    # print(data)
    return render(request,"hello.html",{'data':data})

def add_user(request):
    if request.method == "POST": 
        name = request.POST['uname']
        bday = request.POST['bday']
        gender = request.POST['gender']
        position = request.POST['position']
        age = request.POST['age']
        hobby = request.POST.getlist('hobby')
        img = request.FILES['image']
        address = request.POST['address']

        Result.objects.create(name=name,bday=bday,gender=gender,position=position,age=age,hobby=hobby,img=img,address=address)

        return redirect('hello')    
    return render(request,'add_user.html')

def edit_user(request,uid):
    datas = Result.objects.get(id = uid)
    if request.method == "POST":
        name = request.POST['uname']
        bday = request.POST['bday']
        gender = request.POST['gender']
        position = request.POST['position']
        age = request.POST['age']
        hobby = request.POST.getlist('hobby')
        img = request.FILES['image']
        address = request.POST['address']

        datas.name=name
        datas.bday=bday
        datas.gender=gender
        datas.position=position
        datas.age=age
        datas.hobby=hobby
        datas.img=img
        datas.address=address
        datas.save()
        return redirect('hello')
        
    return render(request,'edit_user.html',{'datas':datas})

def delete_user(request,uid):
    Result.objects.filter(id=uid).delete()
    return redirect('hello')