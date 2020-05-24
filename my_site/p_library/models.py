from django.db import models


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

class Publisher(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=20)
    adress = models.CharField(max_length=200)

class Book(models.Model):
    def __str__(self):
        return self.title
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, default=None, null=True)
    copy_count = models.IntegerField(default=1)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)


