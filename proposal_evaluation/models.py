from django.db import models

class Proposal(models.Model):
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to='proposals/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    evaluated = models.BooleanField(default=False)

    def __str__(self):
        return self.title
