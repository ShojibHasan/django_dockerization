from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    roll = models.IntegerField()
    city = models.CharField(max_length=150)

    

    # class Meta:
    #     verbose_name = _("Student")
    #     verbose_name_plural = _("Students")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})
