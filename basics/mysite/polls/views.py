from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Poll
from django.template import RequestContext,loader	
from django.views import generic
from django.utils import timezone

# Create your views here.

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html') #the pages design is hard-coded in the view - we add this line to change the way the page looks
    context = RequestContext(request, {
	'latest_poll_list' : latest_poll_list,
	})
    return render(request,'polls/index.html',context)
#The render() function is a shortcut to requestcontext/load - it takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument

# View function turned into a class for simplicity/genericity

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
	'''Return the last 5 published polls (not including those set to be published in the future).'''
	return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
## function in views gets called in URL.py
## functions pointing to other pages go here


def detail(request, poll_id):
# long way

#    try:
#	poll = Poll.objects.get(pk=poll_id)
#    except Poll.DoesNotExist:
#	raise Http404

# shortcut
    poll = get_object_or_404(Poll,pk=poll_id)
    return render(request,'polls/detail.html',{'poll':poll})

# detail function turned into a class

class DetailView(generic.DetailView):

    model = Poll
    template_name = 'polls/detail.html'

    def get_queryset(self):
	"""
	Excludes any polls that aren't published yet.
	"""
	return Poll.objects.filter(pub_date__lte=timezone.now())	


def results(request, poll_id):
    poll = get_object_or_404(Poll,pk=poll_id)
    return render(request,'polls/results.html',{'poll':poll})

# results function turned into a class

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

def vote(request, poll_id):
    p = get_object_or_404(Poll,pk=poll_id)
    try:
	selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
	#Redisplay the poll voting form
	return render(request,'polls/details.html',{
		'poll':p,
		'error_message':"You didn't select a choice.",
	})
    else:
	selected_choice.votes += 1
	selected_choice.save()
	# Always return an HttpResponseRedirect after successfully dealing with POST data.
	# This prevents data from being posted twice if a user hits the back button.
    	return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))
	#redirects user to the results page
