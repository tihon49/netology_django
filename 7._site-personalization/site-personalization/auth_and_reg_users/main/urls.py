from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

import auth.views

urlpatterns = [
    path('', auth.views.home, name='home'),
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', auth.views.signup, name='signup'),
    path('thanks/', auth.views.thanks, name='thanks')
]
