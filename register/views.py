from django.shortcuts import redirect, render
from register.forms import StudentForm

from register.models import Student
from django.contrib import messages

def about(request):
    return render(request, "register/about.html")

#read
def student_list(request):
    students  = Student.objects.all()
    print("request print :", request.FILES)
    context = {
        'students': students,
    }
    return render(request, 'register/student_list.html', context)

#create

def student_add(request):
    # login olmayan kullanıcıları engellemek için :
    if not request.user.is_authenticated:
        messages.error(request, "Please login to access this page.")
        return redirect("list")

    form = StudentForm() # boş form render edeceğiz
    if request.method == 'POST':          
        # print(request.POST)				   
        form = StudentForm(request.POST)   
        if form.is_valid():				   
            student = form.save()
            print("request print :", request.FILES)
            if 'image' in request.FILES:
                student.image = request.FILES.get('image')
                student.save()
            messages.success(request, "student created succesfully!")
            return redirect("list")					   
    context = {
        'form' : form
    }
    return render(request, 'register/register.html', context)

#update

def student_update(request, id):
    # login olmayan kullanıcıları engellemek için :
    if not request.user.is_authenticated:
        messages.error(request, "Please login to access this page.")
        return redirect("list")

    student =Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method== "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student =  form.save()
            print("print : ", request.FILES)
            print("image : ", student.image)
            # student.image.delete()
            if 'image' in request.FILES:
                student.image = request.FILES.get('image')
                student.save()
            messages.success(request, "student update succesfully!")
            return redirect("list")   
    context = {
        'form':form,
    }
    return render(request, 'register/student_update.html', context)

#delete
def student_delete(request, id):
    # login olmayan kullanıcıları engellemek için :
    if not request.user.is_authenticated:
        messages.error(request, "Please login to access this page.")
        return redirect("list")

    # student = get_object_or_404(Student, id=id)
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        messages.success(request, "student delete succesfully!")
        return redirect("list")
    return render(request, "register/student_delete.html") 

#detail

def student_detail(request, id):
    # login olmayan kullanıcıları engellemek için :
    if not request.user.is_authenticated:
        messages.error(request, "Please login to access this page.")
        return redirect("list")
    messages.success(request, "student delete succesfully!")  
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'register/student_detail.html', context)
