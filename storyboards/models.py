from django.db import models

class Storyboard(models.Model):

    author = models.CharField(max_length=50,db_index=True)
    title = models.CharField(max_length=50, db_index=True)
    type = models.CharField(max_length=50, db_index=True) #Business or Standard
    category = models.CharField(max_length=50, null=True) #Standard Bucket or Business Bucket, send in group
    tone = models.CharField(max_length=50)
    storyPrompt = models.TextField(blank=False)
    imagePrompt = models.TextField(blank=False)
    isPrivate = models.BooleanField(blank=False)
    storyResult = models.TextField(null=False, blank=False, default="")
    imageUrl = models.TextField(null=False, blank=False, default="")

    class Meta:
        verbose_name_plural = 'Storyboards'

    def __str__(self):
        return self.Title
