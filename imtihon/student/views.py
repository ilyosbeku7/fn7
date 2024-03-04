from django.shortcuts import render, get_object_or_404
from .models import Cities, Category, AirWays

# Create your views here.
def index(request):
    model=Cities
    cities=Cities.objects.all().order_by('name')
    categories=Category.objects.all()
    airs=AirWays.objects.all()
    data={
        'cities': cities,
        'categories': categories,
        'airs': airs
    }
    return render(request, 'student/index.html', context=data)

def category(request, id):
    category=get_object_or_404(Category, pk=id)
    categories=Category.objects.all()
    cities=Cities.objects.filter(cat=category).order_by('name')
    airwayss=AirWays.objects.all()
    data={
        'airwayss': airwayss,
        'categories':categories,
        'cities':cities,
        'category': category
    }
    return render(request, 'student/Category.html', context=data)

def about(request, id):
    categories=Category.objects.all()
    cities=get_object_or_404(Cities, pk=id)
    airs=AirWays.objects.all()
    airvays=get_object_or_404(AirWays, pk=id)
    data={
        'categories':categories,
        'airs':airs,
        'cities':cities,
        'airvays':airvays,
    }
    return render(request, 'student/about.html', context=data)

def airways(request, id):
    airvays=get_object_or_404(AirWays, pk=id)
    airs=AirWays.objects.all()
    airwayss=Cities.objects.filter(air=airvays).order_by('name')
    
    data={
        
        'airvays':airvays,
        'airwayss':airwayss,
        'airs':airs,
      

    }
    return render(request, 'student/Airways.html', context=data)

def contact(request):
     categories=Category.objects.all()
     data={
        'categories':categories,
        }
     return render(request, 'student/contact.html', context=data)
