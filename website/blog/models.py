from django.db import models

class ContactFormSubmission(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    inquiry_type = models.CharField(max_length=50)
    message = models.TextField()
    preferred_contact_method = models.CharField(max_length=50, null=True, blank=True)
    preferred_contact_time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name}"
