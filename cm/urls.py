from django.urls import path
from.import views

urlpatterns = [
   
    path('home',views.homepage,name='home'),

    path('signup',views.signuppage,name='signup'),
    path('login',views.loginpage,name='login'),
    path('user_complaint',views.file_complaint,name='user_complaint'),
    path('complaint_status',views.status,name='complaint_status'),
    path('delete/<int:id>',views.delete_complaint,name='delete'),
    path('update/<int:id>/',views. update_complaint,name='update')
]

