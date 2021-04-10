from django.contrib import admin
from testapp.models import Player

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['pno','pname','pruns','pfours','psixes',]

admin.site.register(Player,PlayerAdmin)
