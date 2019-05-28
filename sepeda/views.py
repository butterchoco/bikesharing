from django.shortcuts import render
from sepeda.forms import sepeda_forms

# Create your views here.
def index(request):
	form = sepeda_forms()
	return render(request, 'sepeda.html', {'form':form})

def sepeda_lists(request):
    return render(request, 'sepeda_lists.html')

# def sepeda_register(request):
    # if (request.method == "POST"):
        # merk = request.POST.get('merk', None)
        # jenis = request.POST.get('jenis', None)
        # status = request.POST.get('status', None)
        # stasiun = request.POST.get('stasiun', None)
        # penyumbang = request.POST.get('penyumbang', None)
        # with connection.cursor() as cursor:
            # cursor.execute("INSERT INTO public.sepeda VALUES(%s, %s, %s, %s, %s)", [
                # merk, jenis, status, stasiun, penyumbang])
        # return HttpResponse("SUCCESS 200")
    # else:
        # return HttpResponse("HTTP 204")

# def register(request):
#     if (request.method == "POST"):
#         form = sepeda_forms(request.POST)
#         if (form.is_valid()):
#             merk = request.POST.get('merk',False)
#             jenis = request.POST.get('jenis',False)
#             status = request.POST.get('status',False)
#             stasiun = request.POST.get('stasiun',False)
#             penyumbang = request.POST.get('penyumbang',False)
#             with connection.cursor() as cursor:
#                 cursor.execute("INSERT INTO public.\"SEPEDA\" VALUES(%s, %s, %s, %s, %s, %s)", [merk, jenis, status, stasiun, penyumbang])
#             return HttpResponseRedirect('')
#         else:
#             return HttpResponse("INVALID 500")
#     else:
#         return HttpResponse("HTTP 204")