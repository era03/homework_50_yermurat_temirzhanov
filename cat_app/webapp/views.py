from hashlib import new
from django.shortcuts import render
from random import randint
from django.shortcuts import redirect
from webapp.cat import Cat


def index_view(request):
    if request.method == 'GET':
         return render(request, 'index.html')


def cat_view(request):
    if request.method == 'POST':
        new_cat = {
            'name': request.POST.get('name'),
            'age': request.POST.get('age'),
            'satiety': randint(30, 50),
            'mood': randint(30, 50),
            'is_sleeping': False
        }
        Cat.cat.append(new_cat)
        print(Cat.cat)
        context = Cat.cat[0]
        return render(request, 'cat.html', context)
    else:
        context = Cat.cat[0]
        return render(request, 'cat.html', context)

def cat_view_action(request):
    if request.method == "POST":
        context = Cat.cat[0]
        if request.POST.get('action') == 'play':
            Cat().play_with_cat()
            return render(request, 'cat.html', context)
        elif request.POST.get('action') == 'feed':
            Cat().feed_the_cat()
            return render(request, 'cat.html', context)
        elif request.POST.get('action') == 'sleep':
            Cat().put_to_sleep()
            return render(request, 'cat.html', context)