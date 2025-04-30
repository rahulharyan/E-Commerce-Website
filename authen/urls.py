from django.urls import path
from authen import views

urlpatterns = [
    path('login_',views.login_,name='login_'),
    path('Register',views.Register,name='Register'),
    path('profile',views.profile,name='profile'),
    path('logout_',views.logout_,name='logout_'),
    path('changepassword_',views.changepassword_,name='changepassword_')
]
