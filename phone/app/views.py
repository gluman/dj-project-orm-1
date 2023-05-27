from django.shortcuts import render

# Create your views here.

def show_phones(request, phone):
    # count = int(request.GET.get('servings', 1))
    # recipe = calc(bludo, count)
    # context = {'recipe': recipe}
    return render(request, 'recipe.html', context)
