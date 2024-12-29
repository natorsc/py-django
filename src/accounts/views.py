from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from . import forms


def profile(request):
    return render(request, template_name='accounts/profile.html')


@login_required
def update(request, pk, username):
    form = forms.UserForm(
        data=request.POST or None,
        instance=get_object_or_404(get_user_model(), pk=pk, username=username),
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('accounts:profile'))
    return render(
        request=request,
        template_name='accounts/update.html',
        context={'form': form, 'title': 'Atualizar'},
    )


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
