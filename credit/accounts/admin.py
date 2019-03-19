from django.contrib import admin
from .models import UserData, Item, Credit, Remaining

admin.site.register(UserData)
admin.site.register(Item)
admin.site.register(Credit)
admin.site.register(Remaining)
# Register your models here.
