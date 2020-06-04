from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Item
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

def index(request):
    all_items = Item.objects.order_by('-pub_date')
    context = {
        'items': all_items
    }
    return render(request, 'todo/base.html', context)

class ItemListView(ListView):
    model = Item
    template_name = "todo/list.html"
    context_object_name = "items"
    ordering = ["-date"]

@csrf_exempt
def save_item(request):
    current_date = timezone.now()
    submitted_content = request.POST["content"]
    item = Item()
    item.content = submitted_content
    item.date = current_date
    item.save()
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_item(request, item_id):
    Item.objects.get(id=item_id).delete()
    return HttpResponseRedirect("/")