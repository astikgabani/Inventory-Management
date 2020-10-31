from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from employees_api.models import EmployeeModel


class UserCreationForm(forms.ModelForm):
    """A form for creating new users."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = EmployeeModel
        fields = ('email', 'name', 'type', 'is_active', 'is_staff')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    """A form for updating users. """

    class Meta:
        model = EmployeeModel
        fields = ('email', 'password', 'name', 'type', 'is_active', 'is_staff')

    def clean_password(self):
        return self.initial["password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        if not self.cleaned_data["password"].startswith("pbkdf2_sha256"):
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdmin(BaseUserAdmin):

    form = UserUpdateForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'is_staff', 'type', 'is_active')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'is_active')}),
        ('Permissions', {'fields': ('type',)}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'name', 'password1', 'password2', 'type', 'is_active'),
        }),
    )


admin.site.register(EmployeeModel, UserAdmin)
admin.site.unregister(Group)
