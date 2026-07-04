from django.db import models


# # Create your models here.

class ServiceCategory(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)


class ServiceProduct(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    variation_code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Variation(models.Model):
    service = models.ForeignKey(ServiceProduct, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


# class Transaction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     service = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20)

#     amount_paid = models.FloatField()      # 200 (what user sees)
#     supplier_cost = models.FloatField()    # 150 (hidden)
#     profit = models.FloatField()           # 50 (YOUR GAIN)

#     status = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)




# from django.db import models
# from django.contrib.auth.models import User


# class Wallet(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wallet")
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     # def __str__(self):
#     #     return f"{self.user.username} - {self.balance}"
    

# class Transaction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     reference = models.CharField(max_length=200)
#     amount = models.DecimalField(max_digits=12, decimal_places=2)
#     status = models.CharField(max_length=20)

#     email = models.EmailField(blank=True, null=True)
#     # def __str__(self):
#     #     return f"{self.user.username} - {self.amount} - {self.status}"
    



#     class Transaction(models.Model):
#         user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE
#     )

#     reference = models.CharField(
#         max_length=200,
#         unique=True
#     )

#     amount = models.DecimalField(
#         max_digits=12,
#         decimal_places=2
#     )

#     status = models.CharField(
#         max_length=50
#     )

#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )

#     # def __str__(self):
#     #     return f"{self.user.username} - {self.amount}"
    
#     email = models.EmailField(blank=True)
# gateway = models.CharField(max_length=50, blank=True)

from django.contrib.auth.models import User

    # class LoginDevice(models.Model):
    #     user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_agent = models.TextField()
    # ip_address = models.GenericIPAddressField()
    # last_login = models.DateTimeField(auto_now=True)



from django.conf import settings
from django.db import models

    


class LoginDevice(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    user_agent = models.TextField()
    ip_address = models.GenericIPAddressField()
    last_login = models.DateTimeField(auto_now=True)