from django.contrib import admin

from .models import Entry,Rsvp,Stats

class EntryAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'title', 'author', )
    list_display_links = ('pub_date', 'title', )
    ordering = ('-pub_date', )
    date_hierarchy = 'pub_date'
    exclude = ('pub_date', )
    
class RsvpAdmin(admin.ModelAdmin):
    list_display = ('user','attending_status','number_of_guests','comment',)
    
class StatsAdmin(admin.ModelAdmin):
    list_display = ('gifts_recieved','comment','user')


admin.site.register(Entry, EntryAdmin)
admin.site.register(Rsvp, RsvpAdmin)
admin.site.register(Stats,StatsAdmin)


