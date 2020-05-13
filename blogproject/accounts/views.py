from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
    
        if fullname =='' or email == '' or password1 == '' or password2 =='':
            error = "Please enter all fields"
            return render(request,"signup.html",{'name':'Sign Up','error':error})
        else:  
            try:                              
                if password1==password2:            
                    User.objects.create_user(fullname,email,password1)
                    return redirect("login")
                else:
                    error = "passwords does not match"
                    return render(request,"signup.html",{'name':'Sign Up','error':error})
            except Exception as e:
                return render(request,"signup.html",{'name':'Sign Up','error':str(e)})
    else:
        return render(request,"signup.html",{'name':'Sign Up'})


def login(request):
    if request.method == 'POST':
        error = ''
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username = username,password = password)
            print(user)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                error = "Please enter correct username and password"
                return render(request,"login.html",{'name':'Log In','error':error})
        except Exception as e:
            return render(request,"login.html",{'name':'Log In','error':str(e)})
    else:
        return render(request,"login.html",{'name':'Log In'})

    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')