
from django import forms
from django.forms import ValidationError
from django.conf import settings
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import CompanyProfile, CompanyUser, StudentUser, StudentProfile, User

class UserCacheMixin:
    user_cache = None

class SignIn(UserCacheMixin, forms.Form):
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if settings.USE_REMEMBER_ME:
            self.fields['remember_me'] = forms.BooleanField(label=_('Remember me'), required=False)

    def clean_password(self):
        password = self.cleaned_data['password']

        if not self.user_cache:
            return password

        if not self.user_cache.check_password(password):
            raise ValidationError(_('You entered an invalid password.'))

        return password


class SignInViaEmailForm(SignIn):
    email = forms.EmailField(label=_('Email'))

    @property
    def field_order(self):
        if settings.USE_REMEMBER_ME:
            return ['email', 'password', 'remember_me']
        return ['email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise ValidationError(_('Either you don\'t an account or the email is invalid '))

        if not user.is_active:
            raise ValidationError(_('This account is not active.'))

        self.user_cache = user

        return email



class CompanySignUpForm(UserCreationForm):
    purpose_choices = (
        (1, "Placements"),
        (2, "Internships"),
        (3, "Both"),
    )
    class Meta(UserCreationForm.Meta):
        model = CompanyUser
        fields = settings.COMPANY_SIGN_UP_FIELDS

    purpose = forms.ChoiceField(choices=purpose_choices)
    first_name = forms.CharField(label=_('First Name'), help_text='Company representer shpuld enter his details here', widget = forms.TextInput(attrs={'placeholder': 'Representer\'s First Name'}))
    last_name = forms.CharField(label=_('Last Name'), help_text='Company representer shpuld enter his details here', widget = forms.TextInput(attrs={'placeholder': 'Respresenter\'s Last Name'}))
    company_name = forms.CharField(label=_('Company Name'), help_text='Enter your Company\'s name ', widget = forms.TextInput(attrs={'placeholder': 'Company Name'}))
    email = forms.EmailField(label=_('Email'), help_text='Enter a valid email address ', widget = forms.TextInput(attrs={'placeholder': 'Email'}))

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('This email already registered with an account, '
                                    'Please Sign in or use another email.'))

        return email


class StudentSignUpForm(UserCreationForm):
    branch_choices = (
        (1, _("CSE")),
        (2, _("ECE")),
    )
    BATCH_CHOICES = (
        (1, '2015-2019'),
        (2, '2014-2018'),
        (3, '2017-2021'),
        (4, '2018-2022'),
        (5, '2019-2023'),
    )

    class Meta:
        model = StudentUser
        fields = settings.STUDENT_SIGN_UP_FIELDS

    first_name = forms.CharField(label=_('First Name'), help_text='enter your details here', widget = forms.TextInput(attrs={'placeholder': 'Student\'s First Name'}))
    last_name = forms.CharField(label=_('Last Name'), help_text='enter your details here', widget = forms.TextInput(attrs={'placeholder': 'Student\'s Last Name'}))
    roll_no = forms.CharField(label=_('Roll No.'), help_text="Enter your Roll no.")
    sem = forms.IntegerField()
    branch = forms.ChoiceField(choices=branch_choices)
    batch = forms.ChoiceField(choices=BATCH_CHOICES)
    email = forms.EmailField(label=_('Email'), help_text='Enter a valid email address ',
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('This email already registered with an account, '
                                    'Please Sign in or use another email.'))

        return email
