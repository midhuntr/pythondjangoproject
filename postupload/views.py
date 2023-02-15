from django.shortcuts import render,redirect


# Create your views here.

from django.views.generic import View,TemplateView
from postupload.forms import RegistrationForm,LoginForm,PostuploadForm
from django.views.generic import CreateView,FormView,ListView,DetailView
from postupload.models import MyUser,Postuploads,Comments
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout

class IndexView(ListView):
    template_name="home.html"
    model=Postuploads
    context_object_name='addpost'

    def get_queryset(self):
       return Postuploads.objects.all()

    

class PostuploadView(CreateView):  
    template_name="postupload.html"
    model=Postuploads
    form_class=PostuploadForm
    success_url=reverse_lazy("index")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class PostDetailsView(DetailView):
    model=Postuploads
    template_name='commentdetails.html'
    pk_url_kwarg='id'
    context_object_name='post'

def addcomment_view(request,*args,**kwargs):
    pid=kwargs.get('id')
    post=Postuploads.objects.get(id=pid)
    comment=request.POST.get('cmnts')
    Comments.objects.create(user=request.user,comment=comment,post=post)
    return redirect('index')

def like_view(request,*args,**kwargs):
    id=kwargs.get('id')
    pst=Postuploads.objects.get(id=id)
    pst.post_like.add(request.user)
    pst.save()
    return redirect('index')

class ProfileView(ListView):
    model=Postuploads
    template_name='profile.html'
    context_object_name='images'

    def get_queryset(self):
        return Postuploads.objects.filter(user=self.request.user)

    

class Signupview(CreateView):
    model=MyUser
    form_class=RegistrationForm
    template_name='register.html'
    success_url=reverse_lazy("signin")

class LoginView(FormView):
   form_class=LoginForm
   template_name="login.html"
   success_url=reverse_lazy("signin")
   def post(self,request,*args,**kwargs):
       form=LoginForm(request.POST)
       if form.is_valid():
           uname=form.cleaned_data.get("username")
           pwd=form.cleaned_data.get("password")
           usr=authenticate(request,username=uname,password=pwd)
           if usr:
              login(request,usr)
              return redirect("index")
              
           else:
            return render(request,self.template_name,{"form":form})
            
class SearchbarView(ListView):
    model=Postuploads
    template_name="searchbar.html"


def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")
   

def remove_post(request,*args,**kwargs):
    id=kwargs.get('id')
    Postuploads.objects.get(id=id).delete()
    return redirect('index')



    

