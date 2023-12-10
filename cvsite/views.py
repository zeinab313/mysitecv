from django.shortcuts import render

# Create your views here.
def index_view(request):
    context={'name':'zeinab','family':'ghazaei'}
    return render(request,'cvsite/index.html',context)