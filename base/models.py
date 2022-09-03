from django.db import models

# Create your models here.


# USER MODEL AND MANAGER
class USER(models.Model):
  username = models.models.CharField(max_length=250)
  email = models.models.CharField(max_length=50)
  password = models.models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()
  
class UserManager(models.Manager):
  
  def reg_validator(self, postData):
    errors = {}
    if len(postData['username']) < 2:
      errors ['username'] = 'Username must be at least 2 characters.'
      
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if len(postData['email'])==0:
      errors ['email'] = "You must enter an email address."
    elif not email_regex.match(postData['email']):
      errors['email'] = "Must be a valid email."
      
    current_users = User.objects.filter(email = postData[email])
    if len(current_users) > 0:
      errors['duplicate'] = "That email is already in use!"
      
    if len(postData['password']) < 6:
      errors['password'] = "Password must be at least 6 characters."
      
    if postData['password'] != postData['confirm_password']:
      errors['match'] = "Passwords do not match."
      
    return errors
  
  def login_validator(self, postData):
    errors = {}
    existing_user = User.objects.filter(email = postData['email'])
    if len(postData['email']) == 0:
      errors['email'] = "Email must be entered."
      
    if len(postData['password']) < 6:
      errors['password'] = "Password must be at least 6 characters."
      
    elif bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
      errors['password'] = "Email and password do not match!"
    
    return errors

class Item(models.Model):
  name = models.CharField(max_length=250)
  created = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name