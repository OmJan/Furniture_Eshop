# from django.db import models
# from django.contrib.auth.models import User
# from .customer import Customer


# class Profile(models.Model):
#     MALE = 1
#     FEMALE = 2
#     OTHERS = 3
#     GENDER_CHOICE = (
#         (MALE, "Male"),
#         (FEMALE, "Female"),
#         (OTHERS, "Other"),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     ddress = models.TextField(blank=True)
#     birthdate = models.DateTimeField(null=True, blank=True)
#     gender = models.PositiveBigIntegerField(
#         choices=GENDER_CHOICE, null=True, blank=True
#     )
#     #image = models.ImageField(upload_to="upload/users")

#     def __str__(self):
#         return self.user.first_name + self.user.last_name
