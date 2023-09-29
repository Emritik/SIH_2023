from django.db import models

class UploadData(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    file = models.FileField(upload_to="static")
    remark = models.TextField(null=True)

    def __str__(self):
        return self.title
    

class ProjectUpdate(models.Model):
    ids = models.IntegerField(null=True, blank=True, unique=True)
    title  = models.CharField(max_length=50, null=True)
    objective = models.TextField()
    completion = models.CharField(max_length=50)    

    def __str__(self):
        return self.objective
        


