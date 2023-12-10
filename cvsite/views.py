from django.shortcuts import render

# Create your views here.
def index_view(request):
    context={'name':'zeinab','family':'ghazaei','brith':'1368/5/25','eduction':'Bachelor of Information Technology',
             'expertise':'Familiarity with C# and PHP programming languages,I did my thesis in PHP and I just started Python and I am currently learning Django.',
             'email':'zghazaei313@gmail.com',
             'phone':'0919*****45'
             }
    return render(request,'cvsite/index.html',context)