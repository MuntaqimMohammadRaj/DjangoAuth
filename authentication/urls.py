
from django.contrib import admin
from django.urls import path,include
from authentication.core import views

urlpatterns = [
    path('',views.home,name='home'),
    path('content/',views.content,name='content'),
    path('signup/',views.signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
