from django.shortcuts import render
from stasiun.forms import stasiun_forms

# Create your views here.
def index(request):
	form = stasiun_forms()
	return render(request, 'stasiun.html', {'form':form})

def stasiun_lists(request):
    return render(request, 'stasiun_lists.html')
