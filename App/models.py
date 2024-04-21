from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class Grievance(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(
        max_length=100, blank=True, null=True)  # User's name (optional)

    def __str__(self):
        return self.title


class Suggestion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(
        max_length=100, blank=True, null=True)  # User's name (optional)

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Circular(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Broadcast(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Club(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    details = models.TextField()
    link = models.URLField(default='uvce.ac.in')

    def __str__(self):
        return self.name


class Contribution(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    contribution_type = models.CharField(max_length=100)
    contribution_description = models.TextField()
    contact_preference = models.CharField(
        max_length=10, choices=(('Email', 'Email'), ('Phone', 'Phone')))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
