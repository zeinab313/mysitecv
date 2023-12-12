from django.shortcuts import render

# Create your views here.
def index_view(request):
    context={'name':'zeinab','family':'ghazaei','brith':'1368/5/25','eduction':'Bachelor of Information Technology، and has a professional technical Python certificate',
             'expertise':'Familiarity with C# and PHP programming languages,I did my thesis in PHP and I just started Python and I am currently learning Django.',
             'email':'zghazaei313@gmail.com',
             'phone':'0919*****45',
             'project':' submitted my thesis project with PHP, an upload and download site, and for the end of the Python class in professional technology, I presented a project called Hospital with Qty 5 and Python.',
             'abilities':'Familiar with C#, PHP and Python and currently learning Django',
             'python':'Python is an interpreted, object-oriented, high-level programming language .',
             'jango':'WebDjango is a high-level Python web framework t.',
             'english':'English language, a West Germanic language of the Indo-European language family ',
             'react':'WebReact is the library for web .',
             }
    return render(request,'cvsite/index.html',context)