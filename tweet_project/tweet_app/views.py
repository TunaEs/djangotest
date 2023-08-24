from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from tweet_app.models import Tweets
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from . import models



# Create your views here.

def listtweet(request):
    all_tweets = Tweets.objects.all()
    tweet_dict = {"tweets":all_tweets}
    return render(request,"tweet_app/listtweet.html",context=tweet_dict)


@login_required(login_url="/login")
def addtweet(request):
    if request.method == "POST":
        
        message = request.POST["message"]
        Tweets.objects.create(username=request.user,message=message)
        return redirect(reverse("tweet_app:listtweet"))
    else:
        return render(request,"tweet_app/addtweet.html")


@login_required
def delete(request,id):
    tweet = models.Tweets.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweets.objects.filter(id=id).delete()
        return redirect(reverse("tweet_app:listtweet"))


class signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("/login")
    template_name = "registration/signup.html"

