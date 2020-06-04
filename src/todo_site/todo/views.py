from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Item

def index(request):
    context = {
        "items": Item.objects.order_by('-pub_date')
    }
    return render(request, 'todo/base.html', 'context')

class ItemListView(ListView):
    model = Item
    template_name = "todo/list.html"
    context_object_name = "items"
    ordering = ["-date"]