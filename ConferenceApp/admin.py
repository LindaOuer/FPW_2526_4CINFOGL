from django.contrib import admin
from .models import *

# Register your models here.

class ConferenceAdmin(admin.ModelAdmin):
    list_display= ('name', 'location', 'start_date', 'end_date')
    search_fields = ('name', 'theme', 'location') # Ajout d'un champ de recherche
    list_filter = ('theme', 'location') # Ajout de filtres pour faciliter la navigation
    list_per_page = 1  # Pagination pour afficher 10 conférences par page
    ordering = ('-start_date',)  # Trier par date de début décroissante
    

admin.site.register(Conference, ConferenceAdmin)

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    actions = ['set_payed']
    
    def set_payed(self, request, queryset):
        queryset.update(payed=True)
        self.message_user(request, "Selected submissions have been marked as payed.")
    set_payed.short_description = "Mark selected submissions as payed"
    
    list_display = ('title', 'conference', 'user', 'submission_date', 'status', 'payed')
    search_fields = ('title', 'user__username', 'conference__name')
    list_filter = ('status', 'payed', 'conference__theme')
    list_per_page = 10
    ordering = ('-submission_date', 'title')
    list_editable = ('status',)
    
    # fields = ('title', 'abstract', 'paper', 'keywords', 'status', 'payed', 'conference', 'user')   
    fieldsets = (
        ('Submission Details', {  
            'fields': ('title', 'abstract', 'paper', 'keywords')
        }),
        ('Status Information', {
            'fields': ('status', 'payed')
        }),
        ('Associations', {
            'fields': ('conference', 'user')
        }),
    )
    


admin.site.register(OrganizingCommittee)