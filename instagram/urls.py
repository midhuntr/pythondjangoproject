"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from postupload import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.IndexView.as_view(),name="index"),
    path('register/',views.Signupview.as_view(),name="registration"),
    path('',views.LoginView.as_view(),name="signin"),
    path('addpost/',views.PostuploadView.as_view(),name="addpost"),
    path('post/<int:id>/',views.PostDetailsView.as_view(),name='addcomment'),
    path('post/comment/add/<int:id>/',views.addcomment_view,name='addcmnts'),
    path('post/<int:id>/like/',views.like_view,name='like'),
    path('image/',views.ProfileView.as_view(),name='images'),
    path('search/',views.SearchbarView.as_view(),name='searchbar'),
    path('accounts/logout/',views.signout_view,name='signout'),
    path("post/<int:id>/remove",views.remove_post,name='remove-post')  

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
