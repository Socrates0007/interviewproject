from django.db import models

# Create your models here.
class Template(models.Model):
    template_name=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    body=models.TextField()

    class Meta:
        ordering= ("-id",)

    def __str__(self):
        return self.template_name
