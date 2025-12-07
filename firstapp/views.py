from django.shortcuts import render
from firstapp.models import happi
# Create your views here.
def happie(request):
    my_data=happi.objects.all()
    my_dict={'my_data':my_data}
    return render(request, 'html_files/index.html',context=my_dict)