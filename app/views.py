from django.shortcuts import render, redirect, reverse
from app.models import Link

# Create your views here.
def create(request):
    if request.method == 'GET':
        return render(request, 'app/create.html')
    elif request.method == 'POST':
        url = request.POST.get('url')
        link = Link.shorten(url)
        if link is None:
            return render(request, 'app/create.html', {'invalid_url': True}, status=422)
        else:
            return redirect('app:show', short_code=link.short_code)
    return render(request, 'app/create.html')

def show(request, short_code):
    return render(request, 'app/show.html', {'link': Link.find_by_short_code(short_code)})

def goto(request, short_code):
    link = Link.find_by_short_code(short_code)
    if link is None:
        return redirect('app:create')
    else:
        return redirect(link.original)
