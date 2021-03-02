from django.shortcuts import render, redirect
from .forms import RecipeForm, UserRegisterForm

from .models import Recipes
from django.views import generic
from django.urls import reverse_lazy


# вывод списка всех офисов
def index(request):
    recipes = Recipes.objects.all()
    context = {
        'recipes': recipes,
        'title': 'Рецепты'
    }
    return render(request, template_name='layouts/index.html', context=context)


# добавление офиса
def image_upload_view(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'layouts/newRecipe.html', {'form': form})


# регистрация
class SignUpView(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('signin')
    template_name = 'registration/signup.html'
