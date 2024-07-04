from django.shortcuts import render
from .models import PortfolioItem

def portfolio(request):
    items = PortfolioItem.objects.all()
    return render(request, 'portfolio/portfolio.html', {'items': items})
