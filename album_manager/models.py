from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=50)  
    country = models.CharField(max_length=50)  

    def __str__(self):
        return f"{self.name} - {self.country}"


class Album(models.Model):
    title = models.CharField(max_length=40, null=False)  
    release_year = models.DateField() 
    GENDER = [
        ('ROCK', 'Rock'),
        ('POP', 'Pop'),
        ('RAP', 'Rap'),
        ('JAZZ', 'Jazz'),
        ('BLUES', 'Blues'),
        ('REGGAE', 'Reggae'),
        ('METAL', 'Metal'),
        ('CLÁSICA', 'Clásica'),
        ('ELECTRONICA', 'Electronica'),
        ('OTRO', 'Otro'),
    ]
    gender = models.CharField(max_length=20, choices=GENDER) 
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='album_covers/',null=True, blank=True) 

    def __str__(self):
        return f"{self.title} - {self.artist.name}"