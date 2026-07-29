from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_GET

from core.views import get_save_redirect

from . import forms, models

CREATE_URL = reverse_lazy("task:create")
UPDATE_URL = reverse_lazy("task:update")
CANCEL_URL = reverse_lazy("task:home")


@require_GET
def home(request):
    q = request.GET.get("q", "").strip()
    queryset = models.Task.objects.all().order_by("title")
    if q:
        queryset = queryset.filter(title__icontains=q)
    paginator = Paginator(queryset, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="task/home.html",
        context={
            "object_list": page_obj.object_list,
            "page_obj": page_obj,
            "paginator": paginator,
            "is_paginated": page_obj.has_other_pages(),
            "q": q,
        },
    )


def create(request):
    form = forms.TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        task = form.save()
        messages.success(request, "Item salvo com sucesso.")
        return get_save_redirect(
            request=request,
            list_url=CANCEL_URL,
            update_url=UPDATE_URL,
            pk=task.pk,
        )
    return render(
        request=request,
        template_name="core/form-edit.html",
        context={
            "form": form,
            "title": "Criar tarefa",
            "cancel_url": CANCEL_URL,
        },
    )


def update(request, pk):
    obj = get_object_or_404(models.Task, pk=pk)
    form = forms.TaskForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        task = form.save()
        messages.success(request, f"Item {task.title} atualizado com sucesso.")
        return get_save_redirect(
            request=request,
            list_url=CANCEL_URL,
            update_url=UPDATE_URL,
            create_url=CREATE_URL,
            pk=task.pk,
        )
    return render(
        request=request,
        template_name="core/form-edit.html",
        context={
            "form": form,
            "title": "Editar tarefa",
            "cancel_url": CANCEL_URL,
            "delete_url": reverse("task:delete", kwargs={"pk": obj.pk}),
        },
    )


def delete(request, pk):
    task = get_object_or_404(models.Task, pk=pk)
    if request.method == "POST":
        task.delete()
        messages.success(request, "Item excluído com sucesso.")
        return redirect("task:home")
    return render(
        request=request,
        template_name="components/confirm-delete.html",
        context={
            "object": task,
            "cancel_url": CANCEL_URL,
        },
    )
