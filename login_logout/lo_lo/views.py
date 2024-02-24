from django.shortcuts import render,redirect

from django.http import HttpResponse
from lo_lo.models import Employee
def home(request):
    if 'user'in request.session:

            current_user = request.session['user']
            param = {'current_user':current_user}
            return render(request,'base.html',param)
    else:

        return redirect('login')
    return render(request,'login.html')
def signup(request):
    if request.method =='POST':
            uname=request.POST.get('uname')
            pwd= request.POST.get('pwd')
            if Employee.objects.filter(employee_name=uname).count()>0:
                    return HttpResponse("username already exist")
            else:

                    user=Employee(employee_name=uname,employee_password=pwd)
                    user.save()
                    return redirect('login')
    else:
            return render(request,'signup.html')
def login(request):

    if request.method =="POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        check_user=Employee.objects.filter(employee_name=uname,employee_password=pwd)
        if check_user:
            request.session['user']=uname
            return redirect('home')
        else:
            return HttpResponse('please provide valid username and password')
    return render(request,'login.html')
def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')



