from django.contrib import admin
from django.urls import path,include
# from .views import RegisterView
from .views import register,index,user_login,user_logout,addhouse1,search,passreset,otpverify,deleteacc,myhouses,house_deletion
app_name='signup_login'
urlpatterns = [
    path('',index,name='home'),
    path('register',register, name='register'),
    path('logout',user_logout,name='logout'),
    path('login',user_login,name='login'),
    path('addhouse',addhouse1,name='addhouse'),
    path('search',search,name='search'),
    path('reset-password',passreset,name='passwordreset'),
    path('otp-verify',otpverify,name='otpverify'),
    path('deleteacc',deleteacc,name='deleteacc'),
    path('myhouses',myhouses,name='myhouses'),
    path('deletehouse',house_deletion,name='house_deletion')
]
