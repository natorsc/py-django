from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from . import forms


@login_required
def profile(request):
    return render(
        request=request,
        template_name="accounts/profile.html",
    )


@login_required
def update(request):
    form = forms.UserForm(data=request.POST or None, instance=request.user)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("accounts:profile")
    return render(
        request=request,
        template_name="core/form.html",
        context={
            "form": form,
            "title": "Atualizar cadastro",
        },
    )


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("accounts:profile")
    template_name = "core/form.html"
    title = "Criar conta"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context
