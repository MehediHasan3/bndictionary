# views.py
from django.shortcuts import render
from .models import chomolokko, bn, en
from .decorators import log_search

@log_search
def index(request):
    query = request.GET.get('query', '')
    query = query.strip()
    result = None
    
    if query:
        # Use exact match to find words that exactly match the query db table = chomolokko
        try:
            result = chomolokko.objects.get(word__iexact=query)
        except chomolokko.DoesNotExist:
            result = None

    return render(request, 'bntobn.html', {'query': query, 'result': result})

@log_search
def bntoen(request):
    query = request.GET.get('query', '')
    query = query.strip()
    result = None
    
    if query:
        # Use exact match to find words that exactly match the query
        try:
            result = bn.objects.get(word__iexact=query)
        except bn.DoesNotExist:
            result = None

    return render(request, 'bntoen.html', {'query': query, 'result': result})

@log_search
def entobn(request):
    query = request.GET.get('query', '')
    query = query.strip()
    result = None
    
    if query:
        # Use exact match to find words that exactly match the query
        try:
            result = en.objects.get(word__iexact=query)
        except en.DoesNotExist:
            result = None

    return render(request, 'entobn.html', {'query': query, 'result': result})


#Underconstruction
def construction(request):
    return render(request, 'construction.html')


#bnalphabet
def bnalpha(request):
    return render(request, 'bnalpha.html')

#enalphabet
def enalpha(request):
    return render(request, 'enalpha.html')


def custom_401(request, exception=None):
    return render(request, '401.html', status=401)

def custom_403(request, exception=None):
    return render(request, '403.html', status=403)

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

def custom_405(request, exception=None):
    return render(request, '405.html', status=405)
#
# views.py
#from django.shortcuts import render
#from .models import Word

#def word_list(request):
  #  all_words = Word.objects.all().order_by('word')
 #   grouped_words = {}

  #  for word in all_words:
    #    first_char = word.word[0].upper()
#        if first_char not in grouped_words:
     #       grouped_words[first_char] = []
#        grouped_words[first_char].append(word)

  #  return render(request, 'word_list.html', {'grouped_words': grouped_words})
#