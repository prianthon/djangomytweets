from django.contrib import admin
from models import Tweet

def __unicode__(self):
    return self.text

# Register your models here.
admin.site.register(Tweet)
