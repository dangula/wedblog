from django.contrib import messages
from django.views.generic import CreateView,UpdateView
from django.views.generic.base import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.db.models import Sum

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.template import RequestContext

import datetime
from .forms import EntryForm,RSVPForm,StatsForm
from .models import Entry,Rsvp,Stats,ATTENDING_CHOICES
from decimal import Context


class AddEntryView(CreateView):
    """Generic view for creating a new entry

    Django generic views are instantiated with a reference to the current 
    request (self.request).  We can use this to get hold of the currently 
    authenticated user and use that to tie the new entry to a User object
    """
    def form_valid(self, form):
        # saving the form while passing commit=False will ensure that no
        # attempt is made to save the object created by the form.  This allows
        # us to manually set values we need, like the author.  See the model
        # save method to find out how we get pub_date automaticall
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        # we can use the django messages framework to pass information back
        # to the user.  Here we alert the user that their entry was saved.
        msg = "Your post has been published"
        messages.add_message(self.request, messages.INFO, msg)
        return super(AddEntryView, self).form_valid(form)

class HomePageView(TemplateView):

    template_name = "blog/MainPage.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        wedDate = datetime.datetime(2013,7,2,17,30)
        delta = wedDate - datetime.datetime.now()
        context['wedDate'] = wedDate
        context['daysLeft'] = delta.days    
        return context
    
class MapPageView(TemplateView):

    template_name = "blog/MapPage.html"

    def get_context_data(self, **kwargs):
        context = super(MapPageView, self).get_context_data(**kwargs)
        wedDate = datetime.datetime(2013, 05, 05,17,30)
        delta = wedDate - datetime.datetime.now()
        context['wedDate'] = wedDate
        context['daysLeft'] = delta.days       
        return context
    
class StatsPageView(TemplateView):

    template_name = "adminStats/adminStatsMainpage.html"

    def get_context_data(self, **kwargs):
        context = super(StatsPageView, self).get_context_data(**kwargs)
        YesRsvps = Rsvp.objects.filter(attending_status='yes')
        YesRsvpsCount = Rsvp.objects.filter(attending_status='yes').count()
        TotalGuestCount = Rsvp.objects.filter(attending_status='yes').aggregate(Sum('number_of_guests'))
        NoRsvp = Rsvp.objects.filter(attending_status='no')
        NoRsvpCount = Rsvp.objects.filter(attending_status='no').count()
        MayBeRsvp = Rsvp.objects.filter(attending_status='maybe')
        MayBeRsvpCount = Rsvp.objects.filter(attending_status='maybe').count()
        
        context['yesRsvp'] = YesRsvps
        context['yesCount'] = YesRsvpsCount
        context['yesGuests'] = TotalGuestCount  
        context['NoRsvp'] = NoRsvp
        context['NoCount'] = NoRsvpCount 
        context['MayBeRsvp'] = MayBeRsvp
        context['MayBeCount'] = MayBeRsvpCount
           
        return context  

class UserDetailStatsView(TemplateView):
    template_name = "adminStats/userDetail.html"

    def get_context_data(self, **kwargs):
        context = super(UserDetailStatsView, self).get_context_data(**kwargs)
           
        return context  

def RsvpCreateUpdateView(request):
    if request.method == 'GET':
        if not request.user.is_authenticated():
            msg = "Plese login"
            messages.add_message(request, messages.INFO,msg)
            return HttpResponseRedirect('/')          
        try:
            rsvp = Rsvp.objects.get(user=request.user)
        except Rsvp.DoesNotExist:
           rsvp = None 
        form = RSVPForm(instance=rsvp)

    if request.method == 'POST':
        try:
            user = request.user
        except TypeError:
            msg = "Plese login"
            messages.add_message(request, messages.INFO,msg)
            return HttpResponseRedirect('/')  
        try:
            rsvp = Rsvp.objects.get(user=request.user)
        except Rsvp.DoesNotExist:
           rsvp = None
        form = RSVPForm(request.POST, instance=rsvp)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            attendStatus = instance.attending_status
            if attendStatus == u'yes':
                msg = "Thank you for RSVPing - we are glad you can make it to our wedding"
            elif attendStatus == u'no':
                msg = "Thank you for RSVPing - we are Sad you can cannot make it to our wedding"
            else :
                msg = "Thanks You , please RSVP Yes or No by : July 2nd 2013"
            messages.add_message(request, messages.INFO,msg)
            return HttpResponseRedirect('/')

    return render_to_response('rsvp/rsvp_view.html', {
        'form': form
    }, context_instance=RequestContext(request))

def UserDetailView(request,pk):
    
    if request.method == 'GET':
         rsvp = get_object_or_404(Rsvp, pk=pk)
         user =  rsvp.user
         try:
            stats = Stats.objects.get(user=user)            
         except Stats.DoesNotExist:
            stats = None
         try :
            entry = Entry.objects.filter(author=user)
         except Entry.DoesNotExist:
            entry = None
         form = StatsForm(instance=stats)

    if request.method == 'POST':
        rsvp = get_object_or_404(Rsvp, pk=pk)
        user =  rsvp.user
        try:
            stats = Stats.objects.get(user=user)   
        except Stats.DoesNotExist:
                stats = None
        try:
            entry = Entry.objects.filter(author=user)
        except Entry.DoesNotExist:
                 entry = None
        form = StatsForm(request.POST, instance=stats)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user
            form.save()
            return HttpResponseRedirect(reverse('admin_stats'))

    return render_to_response('adminStats/userDetail.html', {
        'form': form,'rsvp':rsvp,'entries':entry
    }, context_instance=RequestContext(request))


