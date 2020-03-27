from django.db import models

from skills.models import Skill
from interests.models import Interest
from courses.models import Course
from users.models import ModifiedUser

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    description = models.TextField()
    date_posted = models.DateField()
    application_src = models.URLField(max_length=200)
    required_skills = models.ManyToManyField(Skill)

class UserJob(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(ModifiedUser, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    is_saved = models.BooleanField(default=False)
    is_qualified = models.BooleanField()    # True if all(skill in user.skills for skill in job.required_skills) == True, else False
    has_applied = models.BooleanField(default=False)