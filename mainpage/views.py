#-*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Post, Uni, Singsong
from django.contrib.auth.models import User
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
   
    return render(request, 'mainpage/main.html')  
    
def sogae(request):
    return render(request, 'mainpage/sogae.html')  
    
def logged_in(request):
    userid=request.session['userid']
    userinfo=User.objects.filter(email=userid).values('name','email')
    userinfo_list = [entry for entry in userinfo]
    userinfo_dict={}
    for user in userinfo_list:
        for items in user :
           value=user[items]
           userinfo_dict[items]=value
           
    return render(request, 'mainpage/main.html',userinfo_dict)  

    
def notice(request):
    userid=request.session['userid']
    userinfo=User.objects.filter(email=userid).values('name','email')
    userinfo_list = [entry for entry in userinfo]
    userinfo_dict={}
    for user in userinfo_list:
        for items in user :
           value=user[items]
           userinfo_dict[items]=value
     
    
    post_list = Post.objects.all()
    context = {'post_list' : post_list}
    return render(request, 'mainpage/notice.html', context)
    
def raking(request):
    
    return render(request, 'mainpage/ranking.html')
def uni_list(request):
    uni_list = Uni.objects.all()
    context = {'uni_list': uni_list}
    return render(request, 'mainpage/uni_list.html', context)
def event(request):
    return render(request, 'mainpage/event.html')
def add_song(request):
    return render(request, 'mainpage/add_song.html')
def mysong(request):
    return render(request, 'mainpage/mysong.html')
    
def Signup(request) :
    name=request.POST.get('name', False)
    email=request.POST.get('email', False)
    password=request.POST.get('password', False)
    
    try:
        userdata=User.objects.get(name = name,email = email, password=password)
    except:
        userdata=User(name = name,email = email,password = password)
    
    if User.objects.filter(email=email).exists() is False :
        userdata.save()
    
    userdatas=User.objects.all()
    userdatas={'userdatas':userdatas}
    
    if User.objects.filter(email=email).exists() :
        messages.error(request,"이미 존재하는 이메일 입니다.")
        return render(request,'mainpage/signUpPage.html',userdatas) 
    return render(request,'mainpage/login.html',userdatas)

def Signin(request):
    input_email = request.POST.get('email',None)
    input_password=request.POST.get('password',None)
    check_email=User.objects.filter(email=input_email).exists()
    
    if check_email is True :
        check_password=User.objects.filter(email=input_email,password=input_password).exists()
        
        if check_password is True :
            
            projects = User.objects.all()
            request.session['userid']=input_email
            userdatas={'email' :input_email,'password':input_password, 'projects' : projects}
            
            return render(request,'mainpage/main.html',userdatas)
        
        elif check_password is False :
            messages.error(request,"비밀번호가 일치하지 않습니다.")
   
    elif check_email is False: 
        messages.error(request,"존재하지 않는 이메일 입니다.")
    
    userdatas={'email' :input_email,'password':input_password}   
    return render(request,'mainpage/login.html',userdatas)


def Register_song(request) :
    title=request.POST.get('title', False)
    content=request.POST.get('content', False)
    youtubeurl=request.POST.get('youtubeurl', False)
    
    try:
        songdata=Singsong.objects.get(title = title, content = content, youtubeurl = youtubeurl)
    except:
        songdata=Singsong(title = title,content = content, youtubeurl = youtubeurl)
    
    if Singsong.objects.filter(youtubeurl=youtubeurl).exists() is False :
        songdata.save()
    
    songdatas=Singsong.objects.all()
    songdatas={'songdata':songdata}
    
    return render(request,'mainpage/login.html',songdatas)