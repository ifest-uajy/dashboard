from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import User, RegistrationHandler, ForgotPasswordHandler

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """
    Define admin model for custom user model
    without username, first_name and last_name
    """

    fieldsets = (
        (
            None,
            {'fields': ['full_name', 'email', 'password']}
        ),
        (
            _('Membership Status'),
            {'fields': ['is_confirmed', 'is_staff', 'is_superuser']}
        ),
        (
            _('Membership Information'),
            {'fields': ['last_login', 'date_joined']}
        )
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('full_name', 'email', 'date_joined', 'is_confirmed', 'is_staff')
    search_fields = ('full_name', 'email')
    ordering = ('full_name',)


@admin.register(RegistrationHandler)
class RegistrationHandlerAdmin(admin.ModelAdmin):
    list_display = ['user', 'token', 'is_confirmed', 'sent_at']
    list_filter = ['is_confirmed']
    readonly_fields = ['token', 'sent_at']
    autocomplete_fields = ['user']
    search_fields = ['user__full_name', 'user__email']

    class Meta:
        ordering = ['-sent_at']

@admin.register(ForgotPasswordHandler)
class ForgotPasswordHandlerAdmin(admin.ModelAdmin):
    list_display = ['user', 'token', 'is_confirmed', 'sent_at']
    list_filter = ['is_confirmed']
    readonly_fields = ['token', 'sent_at']
    autocomplete_fields = ['user']
    search_fields = ['user__full_name', 'user__email']

    class Meta:
        ordering = ['-sent_at']