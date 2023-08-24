from django.urls import path,reverse,reverse_lazy
from . import views
app_name="tweet_app"


urlpatterns = [
    path("",views.listtweet,name="listtweet"),
    path("add/",views.addtweet,name="addtweet"),
    path("signup/",views.signup.as_view(),name="signup"),
    path("deletetweet/<int:id>",views.delete,name="deletetweet"),
]
