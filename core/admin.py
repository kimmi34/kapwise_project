from django.contrib import admin
from .models import User,Address,Company,Geo
# Register your models here.

admin.site.register([User,Address,Company,Geo])
