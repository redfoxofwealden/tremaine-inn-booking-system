from django.contrib import admin

# Register your models here.

# The following code was copied and modified from
# (https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#extending-user)

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from customeraccount.models import Customer


# Define an inline admin descriptor for Customer model
# which acts a bit like a singleton
class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = "customer"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [CustomerInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
