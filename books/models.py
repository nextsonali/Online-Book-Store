from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define 'id'
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='book_covers/', blank=True)

    def __str__(self):
        return self.title
