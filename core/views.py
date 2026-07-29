from django.shortcuts import redirect


def get_save_redirect(request, *, list_url, create_url=None, update_url=None, pk=None):
    if "_addanother" in request.POST:
        if create_url:
            return redirect(create_url)
        return redirect(request.path)
    if "_continue" in request.POST and update_url and pk:
        return redirect(update_url, pk=pk)
    return redirect(list_url)
