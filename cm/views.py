from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import UserComplaint
# from django.http import HttpResponse
# Create your views here.
# def cm(request):
#     return HttpResponse("my first project")


def homepage(request):
    return render(request,"landing.html")

def signuppage(request):
    return render(request,"signup.html")
def loginpage(request):

    return render(request,"log.html")


def file_complaint(request):
    msg=''
    if request.POST:
        name=request.POST.get('name')
        location=request.POST.get('location')
        complaint=request.POST.get('complaint')
        complaint_image=request.FILES.get('file')
        obj=UserComplaint(name=name,location=location,complaint=complaint,complaint_image=complaint_image)
        obj.save()
        msg = "Complaint Has Been Registered !!"
    return render(request,"file.html",{"msg":msg})
def status(request):
    data=UserComplaint.objects.all()
    for d in data :
        print(d)
    return render(request,"complaint_status.html",{"user_data":data})


#To delete
def delete_complaint(request,id):
    
    obj_to_be_deleted=get_object_or_404(UserComplaint,pk=id)
    obj_to_be_deleted.delete()
    
    return redirect('complaint_status')

#To update
def update_complaint(request,id):
    
    obj_to_be_edited=get_object_or_404(UserComplaint,pk=id)
    if request.POST:
        name=request.POST.get('name')
        location=request.POST.get('location')
        complaint=request.POST.get('complaint')
        complaint_image=request.FILES.get('file')
        
        obj_to_be_edited.name=name
        obj_to_be_edited.location=location
        obj_to_be_edited.complaint=complaint
        obj_to_be_edited.complaint_image=complaint_image
        
        obj_to_be_edited.save()
        return redirect("complaint_status")
    return render(request,"complaint.html",{'obj_to_be_edited':obj_to_be_edited})