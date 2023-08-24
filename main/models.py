from django.db import models

class Pokedex(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Region(models.Model):
    Pokedex = models.ForeignKey(Pokedex, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Pokemon(models.Model):
    Region = models.ForeignKey(Region, on_delete=models.CASCADE)
    pokemon_id = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    pokemon_type = models.CharField(max_length=100)
    caught = models.BooleanField()
    shiny_caught = models.BooleanField()
    def __str__(self):
        return self.name