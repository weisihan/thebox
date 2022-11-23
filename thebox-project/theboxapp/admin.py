from django.contrib import admin
from .models import DonatedMealSwipe

class DonatedAdmin(admin.ModelAdmin):
    readonly_fields = ('donatedTime',)

# Register your models here.
admin.site.register(DonatedMealSwipe, DonatedAdmin)
