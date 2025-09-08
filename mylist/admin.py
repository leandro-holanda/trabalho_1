from django.contrib import admin
from .models import MyList


@admin.register(MyList)
class MylistAdmin(admin.ModelAdmin):
    list_display = ('added_at',)
