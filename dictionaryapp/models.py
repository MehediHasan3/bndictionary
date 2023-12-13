# models.py
from django.db import models
from django.utils import timezone

class chomolokko(models.Model):
    word = models.CharField(max_length=100, unique=True)
    meaning = models.TextField()

    def __str__(self):
        return self.word

class bn(models.Model):
    word = models.CharField(max_length=100, unique=True)
    meaning = models.TextField()

    def __str__(self):
        return self.word

class en(models.Model):
    word = models.CharField(max_length=100, unique=True)
    meaning = models.TextField()

    def __str__(self):
        return self.word

class SearchLog(models.Model):
    ip = models.GenericIPAddressField(verbose_name='IP Address')
    user_agent = models.TextField(verbose_name='User Agent')
    cookies = models.TextField(verbose_name='Cookies')
    query_word = models.CharField(max_length=255, verbose_name='Search Query')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')
    requested_url = models.URLField(blank=True, null=True, verbose_name='Requested URL')
    # Additional fields
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name='Location')
    user_id = models.IntegerField(blank=True, null=True, verbose_name='User ID')
    device_type = models.CharField(max_length=50, blank=True, null=True, verbose_name='Device Type')
    browser_info = models.TextField(blank=True, null=True, verbose_name='Browser Information')
    search_category = models.CharField(max_length=50, blank=True, null=True, verbose_name='Search Category')
    search_results_count = models.IntegerField(blank=True, null=True, verbose_name='Search Results Count')
    search_duration = models.DurationField(blank=True, null=True, verbose_name='Search Duration')

    def __str__(self):
        return f"{self.query_word} - {self.timestamp}"