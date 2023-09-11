from django.db import models

# Create your models here.
import uuid
from django.urls import reverse
from django.contrib.auth import get_user_model

class Books(models.Model):
    id = models.UUIDField( # new
    primary_key=True,
    default=uuid.uuid4,
    editable=False)

    title = models.CharField(max_length=64)
    auth = models.CharField(max_length=64)
    ratings = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='covers/' )
    discreption = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detalis" , args=[str(self.id)])


class Review(models.Model):
    
    book = models.ForeignKey(Books , on_delete=models.CASCADE , related_name="review")
    review = models.CharField(max_length=255)
    auth = models.ForeignKey(get_user_model(), on_delete=models.CASCADE )
    rating = models.DecimalField(max_digits=1, decimal_places=1 , null=True , blank=True)

    def __str__(self) -> str:
        return self.review

