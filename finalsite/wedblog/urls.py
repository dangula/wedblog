from django.conf.urls import patterns, url,include
from django.views.generic import ListView
from django.views.generic.base import TemplateView



from wedblog.models import Entry,Rsvp,Stats
from wedblog.forms import EntryForm,RSVPForm,StatsForm
from wedblog.views import AddEntryView,HomePageView,MapPageView,StatsPageView,UserDetailStatsView
from django.db.models.query import QuerySet


urlpatterns = patterns('',
    # List view for all posts:
    url(r'^$', HomePageView.as_view(), name="main-view"),
    url(r'^venue/$',MapPageView.as_view(),name="map_view"),
    url(r'^status/$',StatsPageView.as_view(),name="admin_stats"),
    url(r'^(?P<pk>\d+)/$', 'wedblog.views.UserDetailView',name="user_detail"),
    url(r'^blog/$',
        ListView.as_view(
            queryset=Entry.objects.all(),
            context_object_name="entries",
            template_name="blog/entry_list.html"
        ),
        name="entry_list"),
    url(r'^add/$',
        AddEntryView.as_view(
            model=Entry,
            form_class=EntryForm,
            template_name="blog/entry_form.html",
            success_url="/",
        ),
        name="add_entry"),                     
     url(r'^rsvp/$',
        'wedblog.views.RsvpCreateUpdateView',name='rsvp_event_view'),
)