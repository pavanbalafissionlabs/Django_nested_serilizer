
from django.db import models

class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)



class Projects(models.Model):
    project_name=models.CharField(max_length=100)
    others=models.JSONField()

    def __str__(self):
        return self.project_name

class Resume(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField()
    tech_skills = models.TextField()
    workplace_location = models.ForeignKey(Location, related_name='resumes', on_delete=models.CASCADE)
    work_experience = models.ManyToManyField(Projects, related_name='projects')




