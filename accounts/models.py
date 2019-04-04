from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'company'),
        (3, 'admin'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1, null=True, blank=True)

class StudentUser(User, models.Model):
    # BRANCH_CHOICES = (
    #     (1, 'ECE'),
    #     (2, 'CSE'),
    # )
    # BATCH_CHOICES = (
    #     (1, '2015-2019'),
    #     (2, '2014-2018'),
    #     (3, '2017-2021'),
    #     (4, '2018-2022'),
    #     (5, '2019-2023'),
    # )
    USERNAME_FIELD = 'roll_no'
    user = models.OneToOneField(User, on_delete=None)
    roll_no = models.CharField(
        primary_key=True, max_length=10,
        unique=True,
    )
    sem = models.PositiveSmallIntegerField()
    branch = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)

class StudentProfile(models.Model):
    roll_no = models.OneToOneField(StudentUser, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='student_profile_pics/')
    email = models.EmailField()
    alternate_email = models.EmailField()
    phone = models.CharField(max_length=12)
    alternate_phone = models.CharField(max_length=12)

    is_tpr = models.BooleanField('TPR Status : Check if User is an TPR', default=False)


# Placement record models
class Placement(models.Model):
    PLACEMENT_OPTIONS = (
        (1, 'On Campus Placement'),
        (2, 'Off Campus Placement'),
    )
    roll_no = models.OneToOneField(StudentUser, on_delete=models.CASCADE)
    placed_thru = models.CharField(choices=PLACEMENT_OPTIONS, max_length=100)
    package = models.PositiveSmallIntegerField()
    company_name = models.CharField(max_length=100)

class OfferedPlacement(models.Model):
    roll_no = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
    package_offered = models.PositiveSmallIntegerField()
    company_name = models.CharField(max_length=100)


# companies models
class CompanyUser(User, models.Model):
    company = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
    company_name = models.CharField(max_length=100)

class CompanyProfile(models.Model):
    company = models.OneToOneField(CompanyUser, on_delete=models.CASCADE)
    company_logo = models.ImageField(upload_to='company_logos/')
    location = models.TextField()
    alternate_email = models.EmailField()
    phone = models.CharField(max_length=12)
    alternate_phone = models.CharField(max_length=12)
    website = models.CharField(max_length=100)
    description = models.TextField()
    purpose = models.CharField(max_length=100)







































