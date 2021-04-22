from django.shortcuts import render
from AddUserApp import models


def index(request):
    added_users = models.Adduser.objects.all()

    context = {
        'added_users': added_users,
    }

    return render(
        request=request,
        template_name='AddUser/delete.html',
        context=context,
    )


def delete_user(request, user_id):
    added_users = models.Adduser.objects.all()
    for user in added_users:
        if user.id == user_id:
            context = {
                'username': user.username,
            }
            user.delete()

    return render(
        request=request,
        template_name='AddUser/delete.html',
        context=context,
    )


def edit_user(request, user_id):
    if request.method == 'POST':
        adduser = models.Adduser(
            id=user_id,
            username=request.POST['username'],
            email=request.POST['email'],
        )

        adduser.save()

        context = {
            'username': adduser.username,
            'email': adduser.email,
        }

        return render(
            template_name='AddUser/added.html',
            request=request,
            context=context,
        )
    added_users = models.Adduser.objects.all()
    for user in added_users:
        if user.id == user_id:
            context = {
                'username': user.username,
                'email': user.email,
            }
    return render(
        template_name='AddUser/edit_form.html',
        request=request,
        context=context,
    )


def get_user(request, user_id):
    added_users = models.Adduser.objects.all()
    for user in added_users:
        if user.id == user_id:
            context = {
                'username': user.username,
                'email': user.email,
            }
    return render(
        template_name='AddUser/added.html',
        request=request,
        context=context,
    )


def add_user(request):
    if request.method == 'POST':
        adduser = models.Adduser(
            username=request.POST['username'],
            email=request.POST['email'],
        )

        adduser.save()

        context = {
            'username': adduser.username,
            'email': adduser.email,
        }

        return render(
            template_name='AddUser/added.html',
            request=request,
            context=context,
        )

    return render(
        template_name='AddUser/form.html',
        request=request,
    )
