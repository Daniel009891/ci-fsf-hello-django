from django.shortcuts import render

# Create your views here.
def get_todo_list(request):
    return render(request, '/workspaces/ci-fsf-hello-django/todo/templates/todo_list.html')
