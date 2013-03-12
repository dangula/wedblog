from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

"""
 Static set of choices for RSVP.
"""
ATTENDING_CHOICES = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('maybe', 'Maybe'),
    ('no_rsvp', 'Hasn\'t RSVPed yet'))


class Entry(models.Model):
    """
    Entry model represents a blog entry. User is the Foreign key 
    so each blog is associated with a user. 
    """
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=4000)
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField()

    class Meta:
        ordering = ['-pub_date', ]
        verbose_name_plural = "entries"

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.pk:
            # this object is new, set pub_date
            self.pub_date = timezone.now()
        super(Entry, self).save()

class Rsvp(models.Model):
    """
     Rsvp Model captures the Rsvp respone for each user. User is the Foreign key.
    """

    attending_status = models.CharField(max_length=32, choices=ATTENDING_CHOICES, default='no_rsvp')
    number_of_guests = models.SmallIntegerField(default=0)
    comment = models.TextField(max_length=255, blank=True, default='')
    user = models.ForeignKey(User)
    created = models.DateTimeField(default=datetime.datetime.now)
    updated = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return u"%s - %s" % (self.attending_status,self.number_of_guests)
    
    def save(self, *args, **kwargs):
        self.updated = datetime.datetime.now()
        super(Rsvp, self).save(*args, **kwargs)

class Stats(models.Model):
    """
    Stats is Model to store extra information per user.
    """
    gifts_recieved= models.TextField(max_length=500, blank=True, default='')
    comment = models.TextField(max_length=255, blank=True, default='')
    user = models.ForeignKey(User)    
    
    def save(self):
        super(Stats, self).save()
    
    
    
    