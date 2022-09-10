from django.db import models


  
class BlogManager(models.Manager):
  def blog_validator(self, postData):
    errors = {}
    if len(postData['subject']) < 2:
      errors ['subject'] = "Subject name is too short."
    if len(postData['blog_description']) < 10:
      errors ['blog_description'] = "Blog must be at least 10 characters long."
      
    return errors
  
  
  
  
class Blog(models.Model):
  subject = models.CharField(max_length=250)
  blog_description = models.CharField(max_length=450)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = BlogManager()

def __str__(self):
  return self.name