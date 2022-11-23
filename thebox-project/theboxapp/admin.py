from django.contrib import admin
from .models import DonatedMealSwipe
from .models import TheBox

class DonatedAdmin(admin.ModelAdmin):
    readonly_fields = ('donatedTime',)

class TheBoxAdmin(admin.ModelAdmin):
    readonly_fields = ('creationTime',)

# Register your models here.
admin.site.register(DonatedMealSwipe, DonatedAdmin)
admin.site.register(TheBox, TheBoxAdmin)
