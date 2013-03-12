from django import forms
from django.forms import ModelForm
from registration.forms import RegistrationForm

class RegistrationFormWithName(RegistrationForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

from .models import Entry,Rsvp,ATTENDING_CHOICES,Stats


class EntryForm(forms.ModelForm):
    """allow entry of title and text for a post

    because required fields are missing from this form (author, pub_date),
    we will need to save the form without committing the object and then 
    set those values manually
    """

    class Meta:
        model = Entry
        fields = ('title', 'text', )

class RSVPForm(forms.ModelForm):
    """
    Form for Rsvp model - allows to a user to Rsvp. this Form is accessible only to active users
    who are logged in. The Rsvp event is stored for the active user.
    """
    class Meta:
        model = Rsvp
        fields = ('attending_status', 'number_of_guests','comment' )
        exclude = ('user',)

class StatsForm(forms.ModelForm):
    """
    Form for adding stats for user. This From is only accessible for users with admin privileges.
    Admins have to be logged in to access this form.
    """
    class Meta:
        model = Stats
        fields = ('gifts_recieved', 'comment', )