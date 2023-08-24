from django.contrib import admin
from tweet_app.models import Tweets

# Register your models here.
class Tweetadmin(admin.ModelAdmin):
    pass
admin.site.register(Tweets,Tweetadmin)
