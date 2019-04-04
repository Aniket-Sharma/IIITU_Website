from django.urls import path

from .views import (
    LogInView, CompanySignUpView, LogOutView, StudentSignUpView,
)

app_name = 'accounts'

urlpatterns = [
    path('log-in/', LogInView.as_view(), name='log_in'),
    path('student-log-in/', LogInView.as_view(), name='student_log_in'),
    path('log-out/', LogOutView.as_view(), name='log_out'),
    path('student_sign_up/', StudentSignUpView.as_view(), name='student_sign_up'),
    path('sign-up/', CompanySignUpView.as_view(), name='sign_up'),

]
