from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.decorators.http import require_GET


@require_GET
def home(request):
    return render(
        request=request,
        template_name='home/home.html',
        context={'title': _('Hello World!')},
    )
