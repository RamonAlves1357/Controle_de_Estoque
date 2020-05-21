from django.shortcuts import render
from .models import Produto

# Create your views here.

def produto_list(request):
    templete_name = 'produto_list.html'
    objects = Produto.objects.all()
    context = {'object_list' : objects}
    
    return render(request, templete_name, context)