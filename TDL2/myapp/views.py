from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from myapp.models import Todo
from myapp.forms import TodoForm
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if task:
            Todo.objects.create(task=task)
            messages.success(request, 'New task added successfully.')
        else:
            messages.error(request, 'Task is empty.')
        return HttpResponseRedirect(request.path_info)
    else:
        todo_list_not_completed = Todo.objects.filter(is_completed=False)
        todo_list_completed = Todo.objects.filter(is_completed=True)
        return render(request, 'myapp/index.html', {
            'todo_list_not_completed': todo_list_not_completed,
            'todo_list_completed': todo_list_completed,
        })


def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New task added successfully.')
            return redirect('index')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = TodoForm()
    return render(request, 'myapp/create.html', {'form': form})


def update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)  # 모델 인스턴스를 가져온다
            todo.is_completed = 'is_completed' in request.POST  # is_completed 값을 설정한다
            todo.save()  # 모델 인스턴스를 저장한다
            messages.success(request, 'Task updated successfully.')
            return redirect('index')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'myapp/update.html', {'form': form})


def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    messages.success(request, 'Task deleted successfully.')
    return redirect('index')


def change_status(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed
    todo.save()
    messages.success(request, 'Task status changed successfully.')
    return redirect('index')
