from django.contrib import admin
from accounts.models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(StudentUser)
admin.site.register(StudentProfile)
admin.site.register(CompanyUser)
admin.site.register(CompanyProfile)
admin.site.register(Placement)
admin.site.register(OfferedPlacement)



