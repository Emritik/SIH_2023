from django.shortcuts import render, redirect
from .models import UploadData, ProjectUpdate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 


def home(request):
    return redirect('/login')
#Views for login the user
def  login_user(request):
     if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(username,password)

        if user is not None:
            
            try:
                category = username.split('-')[1]
                print(category)
                if category == "student":
                    login(request, user)
                    messages.success(request,"email or Password incorrect")
                    return redirect('/student_home')
            
                elif category == "staff":
                    login(request, user)
                    messages.success(request,"email or Password incorrect")
                    return redirect('/staff_home')
        
                elif category == "admin":
                    login(request, user)
                    messages.success(request,"email or Password incorrect")
                    return redirect('/admin_home')
        
                else:
                    messages.error(request,'Invalid Credentials!')
                    return redirect('/login')
                

            except:
                messages.info(request,'Username is not vilad as per rules!!')
                return redirect('/login')
        else:
            
            return redirect('/login')

                
         
     return render ( request , "login_form.html")

#Views for student registration
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        mobile_no = request.POST['num']
        #print(username, email, password,mobile_no)
        myuser = User.objects.create_user(username, email,  password)
        myuser.mobile_no = mobile_no 
        myuser.save()  
        messages.success(request,"Your Account has been created.")
        return redirect('/login')     
    
    return render(request, "register_form.html")

#logout panel
def logout_user(request):
    logout(request)
    return redirect('/login')

#Student Panel
@login_required(login_url='/login')
def student_home(request):
    return render(request ,'student_home.html' )


#Staff Panel
@login_required(login_url='/login')
def  staff_home(request):
    return render(request ,"staff_home.html" )

#Admin panel
@login_required(login_url='/login')
def admin_home(request):
    return render(request ,"admin_home.html" )

#Views for upload the student data through themself

@login_required(login_url='/login')
def upload_data_student(request):
    if  request.method == "POST":
        myfile=request.FILES.get("file")
        title = request.POST.get("title")
        description = request.POST.get("description")
        #print(title)
        data = UploadData.objects.create(title = title, description = description, file = myfile)
        data.save()
        
    #queryset = UploadData.objects.all()
    

    return render(request, 'upload_student.html')

#Views for upload the student data through admin panel

@login_required(login_url='/login')
def upload_data_staff(request):
    if  request.method == "POST":
        myfile=request.FILES.get("file")
        title = request.POST.get("title")
        description = request.POST.get("description")
        #print(title)
        data = UploadData.objects.create(title = title, description = description, file = myfile)
        data.save()
        
    #queryset = UploadData.objects.all()
    

    return render(request, 'upload_staff.html')


#Views for upload the student data through admin panel

@login_required(login_url='/login')
def upload_data_admin(request):
    if  request.method == "POST":
        myfile=request.FILES.get("file")
        title = request.POST.get("title")
        description = request.POST.get("description")
        #print(title)
        data = UploadData.objects.create(title = title, description = description, file = myfile)
        data.save()
        
    #queryset = UploadData.objects.all()
    return render(request, 'upload_admin.html')


#Views for search the student data through themself

@login_required(login_url='/login')
def search_data_student (request):
    queryset = UploadData.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(title__icontains = request.GET.get('search'))

    context = {'datas':queryset}
    return render(request, 'student_search.html',context)

#Views for search the student data through staff panel

@login_required(login_url='/login')
def search_data_staff (request):
    queryset = UploadData.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(title__icontains = request.GET.get('search'))

    context = {'datas':queryset}
    return render(request, 'staff_search.html',context)

#Views for search the student data through admin panel

@login_required(login_url='/login')
def search_data_admin (request):
    queryset = UploadData.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(title__icontains = request.GET.get('search'))
    context = {'datas':queryset}
    return render(request, 'admin_search.html',context)


#Views for tracking the student data by themself

@login_required(login_url='/login')
def student_tracking(request):
    if request.method == "POST":
        title = request.POST.get("title")
        objective = request.POST.get("objective")
        completion = request.POST.get("completion")

        data = ProjectUpdate.objects.create(title = title,objective = objective, completion=completion) 
        data.save()    
    return render(request, 'student_tracking.html')

#Views for tracking the student data through staff panel

@login_required(login_url='/login')
def staff_tracking(request):
    queryset = ProjectUpdate.objects.all()
    if request.method == 'POST':
        messages.success(request,"Your responce is tracked!!")
        return redirect('/staff_tracking')
    content={"datas":queryset}
    return render(request, 'staff_tracking.html',content)



#Views for tracking the student data through admin panel

@login_required(login_url='/login')
def admin_tracking(request):
    queryset = ProjectUpdate.objects.all()
    if request.method == 'POST':
        messages.success(request,"Your responce is tracked!!")
        return redirect('/admin_tracking')
    content={"datas":queryset}
    return render(request, 'admin_tracking.html',content)

#Views for view the student data through student panel

@login_required(login_url='/login')
def view_student_data(request, id):
    view = UploadData.objects.get(id = id )
    if request.method == 'POST':
        remark = request.POST.get('remark')
        view.remark = remark
        view.save()
        return redirect('/search_data_student')
    context = {'data':view}
    return render(request, 'view_student_data.html',context)

#Views for view the student data through staff panel

@login_required(login_url='/login')
def view_staff_data(request, id):
    view = UploadData.objects.get(id = id)
    if request.method == 'POST':
        remark = request.POST.get('remark')
        view.remark = remark
        view.save()
        return redirect('/search_data_staff')
    context = {'data':view}
    return render(request, 'view_staff_data.html',context)

#Views for view the student data through admin panel
@login_required(login_url='/login')
def view_admin_data(request, id):
    view = UploadData.objects.get(id = id)
    if request.method == 'POST':
        remark = request.POST.get('remark')
        view.remark = remark
        view.save()
        return redirect('/search_data_admin')
    context = {'data':view}
    return render(request, 'view_admin_data.html',context)

@login_required(login_url='/login')
def back(request):
    
    return redirect('/search_data_student')