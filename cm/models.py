from django.db import models

PENDING = 0
DONE = 1
STATUS_CHOICES = (
    (PENDING, 'Pending'),
    (DONE, 'Done'),
)

class UserComplaint(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255,null=True)
    complaint = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)
    complaint_image = models.ImageField(null=True, blank=True, upload_to="images/")
    def get_status_display(self):
        return dict(STATUS_CHOICES)[self.status]
    
    
    
    @property
    def imageURL(self):
        try:
            url=self.complaint_image.url
        except:
            url=""
        return url

    def __str__(self): 
        return self.name