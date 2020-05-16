from django.db import models
from django.shortcuts import reverse
from users.models import Profile
from django.conf import settings
from django.contrib.auth.models import User




class Category(models.Model):
    text = models.CharField(max_length=50)


    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "Categories"



    def get_absolute_url(self):
        return reverse("core:spec_category", kwargs={
            'slug': self.text
        })



class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to = 'photos/', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
        #return reverse("core:product", kwargs={
            #'slug': self.slug
        #})
