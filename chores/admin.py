from django.contrib import admin

from .models import ChoreList, Chore

# Register your models here.


class ChoreListAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date Info',{'fields': ['due_date'], 'classes':['collapse']}),
    ]


admin.site.register(Chore)
admin.site.register(ChoreList, ChoreListAdmin)