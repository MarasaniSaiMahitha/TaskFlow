from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Task


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":

        username = request.POST.get("user_name")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, "register.html")

        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        messages.success(request, "Registration Successful.")
        return redirect("login")

    return render(request, "register.html")


def login(request):
    if request.method == "POST":

        username = request.POST.get("user_name")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")


from datetime import date, timedelta

@login_required(login_url="login")
def dashboard(request):

    all_tasks = Task.objects.filter(
        user=request.user
    )


    # Dashboard counts

    total_tasks = all_tasks.count()


    pending_tasks = all_tasks.filter(
        status="Pending"
    ).count()


    completed_tasks = all_tasks.filter(
        status="Completed"
    ).count()



    # Search

    tasks = all_tasks


    search = request.GET.get("search")

    priority = request.GET.get("priority")
    status = request.GET.get("status")

    if search:

        tasks = tasks.filter(
        title__icontains=search
    )



    if priority:

        tasks = tasks.filter(
        priority=priority
    )
    

    if status:

        tasks = tasks.filter(
        status=status
    )
    # Pagination

    paginator = Paginator(
        tasks,
        5
    )


    page_number = request.GET.get("page")


    tasks = paginator.get_page(page_number)

    # Due date logic

    today = date.today()

    two_days_later = today + timedelta(days=2)


    due_today = all_tasks.filter(
        due_date=today,
        status="Pending"
    ).count()



    due_soon = all_tasks.filter(
        due_date__gt=today,
        due_date__lte=two_days_later,
        status="Pending"
    ).count()



    context = {

        "tasks": tasks,

        "total_tasks": total_tasks,

        "pending_tasks": pending_tasks,

        "completed_tasks": completed_tasks,

        "due_today": due_today,

        "due_soon": due_soon,

    }


    return render(
        request,
        "dashboard.html",
        context
    )


@login_required(login_url="login")
def add_task(request):
    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")
        priority = request.POST.get("priority")
        due_date = request.POST.get("due_date")

        print("Title:", title)
        print("Priority:", priority)
        print("Due Date:", due_date)

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            priority=priority,
            due_date=due_date,
            status="Pending"
        )

        return redirect("dashboard")

    return render(request, "addtask.html")

@login_required(login_url="login")
def edit_task(request, task_id):

    task = Task.objects.get(id=task_id, user=request.user)

    if request.method == "POST":

        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.priority = request.POST.get("priority")
        task.due_date = request.POST.get("due_date")
        task.status = request.POST.get("status")

        task.save()

        return redirect("dashboard")

    return render(request, "edittask.html", {"task": task})

from django.shortcuts import get_object_or_404, render, redirect

@login_required(login_url="login")
def delete_task(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    if request.method == "POST":

        task.delete()

        return redirect("dashboard")

    return render(
        request,
        "delete_task.html",
        {"task": task}
    )

from django.shortcuts import get_object_or_404, redirect
from .models import Task

@login_required(login_url="login")
def complete_task(request, id):

    task = get_object_or_404(
        Task,
        id=id,
        user=request.user
    )

    task.status = "Completed"
    task.save()

    return redirect("dashboard")

@login_required(login_url="login")
def undo_complete(request, id):

    task = get_object_or_404(
        Task,
        id=id,
        user=request.user
    )

    task.status = "Pending"
    task.save()

    return redirect("completed")


@login_required(login_url="login")
def completed(request):

    tasks = Task.objects.filter(
        user=request.user,
        status="Completed"
    )

    return render(request, "completed.html", {"tasks": tasks})

@login_required(login_url="login")
def profile(request):

    tasks = Task.objects.filter(
        user=request.user
    )


    context = {

        "total_tasks": tasks.count(),

        "completed_tasks": tasks.filter(
            status="Completed"
        ).count(),

        "pending_tasks": tasks.filter(
            status="Pending"
        ).count(),

    }


    return render(
        request,
        "profile.html",
        context
    )

@login_required(login_url="login")
def edit_profile(request):

    user = request.user


    if request.method == "POST":

        user.first_name = request.POST.get("first_name")

        user.last_name = request.POST.get("last_name")

        user.email = request.POST.get("email")


        user.save()


        messages.success(
            request,
            "Profile updated successfully."
        )


        return redirect("profile")


    return render(
        request,
        "edit_profile.html"
    )

@login_required(login_url="login")
def change_password(request):

    if request.method == "POST":

        old_password = request.POST.get(
            "old_password"
        )

        new_password = request.POST.get(
            "new_password"
        )

        confirm_password = request.POST.get(
            "confirm_password"
        )


        user = request.user


        if not user.check_password(old_password):

            messages.error(
                request,
                "Old password is incorrect."
            )

            return redirect(
                "change_password"
            )


        if new_password != confirm_password:

            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect(
                "change_password"
            )


        user.set_password(
            new_password
        )

        user.save()


        messages.success(
            request,
            "Password changed successfully. Please login again."
        )


        return redirect(
            "login"
        )


    return render(
        request,
        "change_password.html"
    )


def logout(request):
    auth_logout(request)
    return redirect("home")