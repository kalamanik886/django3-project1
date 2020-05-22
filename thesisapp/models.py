from django.db import models

# Create your models here.

class RegisterModel(models.Model):
    leader_name     = models.TextField()
    leader_id       = models.IntegerField()
    leader_cgpa     = models.DecimalField(decimal_places=2, max_digits=4)
    co_leader_id    = models.IntegerField()
    co_leader_cgpa  = models.DecimalField(decimal_places=2, max_digits=4)
    contact_mail    = models.EmailField(default="ucchash886@gmail.com")


    choice1  = models.TextField()
    choice2  = models.TextField()
    choice3  = models.TextField()
    choice4  = models.TextField()
    choice5  = models.TextField()
    choice6  = models.TextField()
    choice7  = models.TextField()
    choice8  = models.TextField()
    choice9  = models.TextField()
    choice10 = models.TextField()

