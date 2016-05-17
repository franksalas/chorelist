from django.contrib import admin

from .models import ChoreList, Chore

# Register your models here.

admin.site.register(Chore)
admin.site.register(ChoreList)