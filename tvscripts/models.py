from django.db import models

# Create your models here.


class Script_Tag(models.Model):
    tag_name = models.CharField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return str(self.tag_name)

class Script(models.Model):
    scripts = models.CharField(max_length=500,unique=False)
    position = models.CharField(blank=True,null=True,max_length=500,unique=False)
    epi_number = models.IntegerField()
    season = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    show_name = models.CharField(max_length=500,unique=False)
    footnote = models.TextField(blank=True,null=True,unique=False)
    tags = models.ManyToManyField(Script_Tag,blank=True)

    def __str__(self):
        return str(self.scripts)
