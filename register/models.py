from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

GENDER = (
(None, 'Choose your gender'),
('male', 'male'),
('female', 'female'),
('custom', 'custom'),
('Prefer Not To Say', 'Prefer Not To Say'),
)

class Path(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return "{}".format(self.name)

class Student(models.Model):
    full_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True, region="US")
    mail = models.EmailField(verbose_name="Email")
    gender = models.CharField(max_length=50, choices=GENDER, verbose_name="gender", blank=True)
    student_number = models.IntegerField(blank=True, null=True)
    path=models.ForeignKey(Path, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "image/", default= "profil.jpg") 

    def __str__(self):
        return f"{self.full_name}"

    
