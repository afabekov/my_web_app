from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100)
    img = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
