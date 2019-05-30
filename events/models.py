from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class club(models.Model):

    clubID = models.IntegerField(primary_key=True, unique=True,   null=False)
    name = models.CharField(max_length=50)


class event(models.Model):

    #Primary Info
    eventID = models.IntegerField(unique=True, null=False, primary_key=True)
    name = models.CharField(max_length=100)
    coordinators = models.ManyToManyField(to=User)

    #Venue and Date
    locations = models.CharField(max_length=100)
    dateTime = models.DateTimeField(verbose_name="Date and Time of Event", auto_now=True)

    #Prize Details
    prize = models.TextField(blank=True)

    #Team Member
    minTeam = models.IntegerField(verbose_name="Minimum Size of the Team", validators=[MinValueValidator(0)], default=0)
    maxTeam = models.IntegerField(verbose_name="Maximum Size of the Team", validators=[MinValueValidator(0)], default=0)


    #Detailed Info
    eventType = models.CharField(max_length=30)
    association = models.ForeignKey(to=club, verbose_name="Name of the club/society associated with this event", on_delete=models.CASCADE)
    details = models.TextField(blank=True)
    shortDescription = models.TextField(blank=True, verbose_name="Short Description about event")
    ruleList = models.TextField(blank=True, verbose_name="list of the Rules")

    #Files attached
    poster = models.ImageField(upload_to='Images/events/', null=True)
    rulesPDF = models.FileField(upload_to='PDF/events/', null=True)


