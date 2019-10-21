from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class UserDetails(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=8)

    avatar = models.ImageField()

    about = models.CharField(max_length=1000)
    slogan = models.CharField(max_length=500)

    def __str__(self):
        return self.username



class Jobs(models.Model):
    CATEGORY_CHOICES = (
        ("GD", "Graphics & Design"),
        ("DM", "Digital & Marketing"),
        ("VA", "Video & Animation"),
        ("MA", "Music & Audio"),
        ("PT", "Programming & Tech")
    )

    title = models.CharField(max_length=500)
    job_author = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(default=5)
    photo = models.ImageField()
    active_status = models.BooleanField(default=True)
    job_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_job', kwargs={
        'id':self.id
        })
# BDLPH4469M
class Orders(models.Model):
    order_author   = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    job_details    = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    author_offer   = models.CharField(max_length=1000)
    ordered_date   = models.DateTimeField(auto_now_add=True)
    order_deadline = models.DateTimeField()
    order_budget   = models.IntegerField()
    order_status   = models.BooleanField(default=False)

    def __str__(self):
        return self.job_details.title


    def as_dict(self):
        return {'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}
