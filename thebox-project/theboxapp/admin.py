from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class DonatedAdmin(admin.ModelAdmin):
    readonly_fields = ('donatedTime',)


class TheBoxAdmin(admin.ModelAdmin):
    readonly_fields = ('creationTime',)


# Register your models here.
admin.site.register(DonatedMealSwipe, DonatedAdmin)
admin.site.register(TheBox, TheBoxAdmin)
admin.site.register(Feedback)

# class AccountInline / CustomizedUserAdmin: just conventions...


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'


class CustomizedUserAdmin(UserAdmin):
    # override inlines field of UserAdmin
    inlines = (AccountInline,)


# Re-register the existing user admin panel
admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

# could also show account on the panel - MAYBE NO NEED
admin.site.register(Account)
