from django.contrib import admin
from polls.models import Poll, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):

    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):

#    fields = ['pub_date','question'] #specifies the order in which fields show on the admin page
    fieldsets = [
	(None,			{'fields':['question']}),
	('Date information',	{'fields':['pub_date'],'classes':['collapse']}),
		]
    list_display	= ('question','pub_date','was_published_recently')
    inlines 		= [ChoiceInline] 

    list_filter		= ['pub_date'] #adds a filter sidebar that lets people filter the list by the 'pub_date' field
    search_fields	= ['question'] #adds a searchbox at the top of the change list


admin.site.register(Poll,PollAdmin)
