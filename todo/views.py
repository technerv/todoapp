from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from todo.models import Todo

# Create your views here.
def index(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'todo/index.html', {"todo_items":todo_items})

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST['content']
    created_obj = Todo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, id):
    #context = {}
    todo = get_object_or_404(Todo, id = id)
    if request.method == "POST":
        todo.delete()
        return HttpResponseRedirect("/")
