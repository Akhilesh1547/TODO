from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from todo.models import TODO

# Signup View
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        my_user = User.objects.create_user(username=username, email=email, password=password)
        my_user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_page')
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, 'login.html')

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')

# ToDo Page View
def todo(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to add tasks!")
        return redirect('login')

    tasks = TODO.objects.filter(user=request.user).order_by('-date')  # Fetch tasks for the logged-in user
    return render(request, 'todo.html', {'tasks': tasks})

# AJAX-Based Task Addition
def add_task(request):
    if request.method == 'POST' and request.user.is_authenticated:
        title = request.POST.get('title')
        category = request.POST.get('category', 'Personal')
        priority = request.POST.get('priority', 'Medium')
        due_date = request.POST.get('due_date')

        if title.strip():
            task = TODO.objects.create(
                title=title,
                user=request.user,
                category=category,
                priority=priority,
                due_date=due_date
            )
            return JsonResponse({'success': True, 'task': {
                'id': task.id, 'title': task.title, 'category': task.category,
                'priority': task.priority, 'due_date': str(task.due_date), 'completed': task.completed
            }})
        return JsonResponse({'success': False, 'error': 'Task cannot be empty!'})

    return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)

# Mark Task as Completed
def complete_task(request):
    if request.method == "POST" and request.user.is_authenticated:
        task_id = request.POST.get('task_id')
        try:
            task = TODO.objects.get(id=task_id, user=request.user)
            task.completed = True
            task.save()
            return JsonResponse({'success': True})
        except TODO.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found!'})
    return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)


