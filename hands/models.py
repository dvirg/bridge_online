from django.db import models


class Hand(models.Model):
    subject = models.CharField(max_length=100)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    cards = models.CharField(max_length=200)
    bids = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=300)

    def __str__(self):
        return self.subject
