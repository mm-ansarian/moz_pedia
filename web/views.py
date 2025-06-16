from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import HttpResponse
from .forms import *
from .models import CustomUser, Article
from django.shortcuts import render
from markdown import markdown
from django.views import View


def get_user(request):
    if request.user.is_authenticated:
        username = request.user
        return username
    return None


def permission_denied_view(request, exception=None):
    return render(request, 'errors/403.html', status=403)


def not_found_view(request, exception=None):
    return render(request, 'errors/404.html', status=404)


class MainPage(View):
    def get(self, request):
        user = get_user(self.request)
        return render(request, 'main_page.html', {'user': user})
    

class Account(View):
    def get(self, request):
        user = get_user(request)
        if request.user.is_authenticated:
            return render(request, 'account.html', {'user': user})


class Signup(View):
    def get(self, request):
        user = get_user(request)
        if request.user.is_authenticated:
            return render(request, 'wrong.html', {'condition': 'already_signed_in', 'user': user})
        form = SignupForm
        return render(request, 'signup.html', {'form': form, 'user': user})
    
    def post(self, request):
        if not request.user.is_authenticated:
            form = SignupForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                email = form.cleaned_data.get('email')
                password = make_password(form.cleaned_data.get('password'))
                user = CustomUser.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                )
                login(request, user=user)
                return render(request, 'done.html', {'condition': 'signed_in', 'user': user})
            if form.errors:
                return HttpResponse(f"""
                                    <h2>There are some validation errors:</h2>
                                    {form.errors}
                """)
            return render(request, 'wrong.html', {'condition': 'unexpected_error', 'user': user})
        

class Login(View):
    def get(self, request):
        user = get_user(request)
        if request.user.is_authenticated:
            return render(request, 'wrong.html', {'condition': 'already_logged_in', 'user': user})
        form = LoginForm
        return render(request, 'login.html', {'form': form, 'user': user})
    
    def post(self, request):
        if not request.user.is_authenticated:
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(password=password, username=username)
                if user:
                    login(request, user=user)
                    return render(request, 'done.html', {'condition': 'logged_out', 'user': user})
                return render(request, 'wrong.html', {'condition': 'none_user', 'user': user})
            if form.errors:
                return HttpResponse(f"""
                                    <h2>There are some validation errors:</h2>
                                    {form.errors}
                """)
            return render(request, 'wrong.html', {'condition': 'unexpected_error', 'user': user})
        

class Logout(View):
    def get(self, request):
        user = get_user(request)
        if request.user.is_authenticated:
            return render(request, 'logout.html', {'user': user})
        return render(request, 'wrong.html', {'condition': 'not_signed_in', 'user': user})
    
    def post(self, request):
        logout(request)
        return render(request, 'done.html', {'condition': 'logged_out', 'user': None})


class CreateArticle(PermissionRequiredMixin, View):
    permission_required = ['web.add_article']
    raise_exception = True
    def get(self, request):
        user = get_user(request)
        form = ArticleForm
        return render(request, 'create_article.html', {'form': form, 'user': user})
    
    def post(self, request):
        user = get_user(request)
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            content = form.cleaned_data.get('content')
            article = Article.objects.create(
                author=user,
                title=title,
                description=description,
                content=content,
            )
            return render(request, 'done.html', {'user': user})
        if form.errors:
            return HttpResponse(f'''
                <h2>There are some validation errors:</h2>
                {form.errors}
            ''')
        return render(request, 'wrong.html', {'condition': 'unexpected_error', 'user': user})


class EditArticle(View, PermissionRequiredMixin):
    def get(self, request):
        ...
    
    def patch(self, request):
        ...


class ListArticles(View):
    def get(self, request):
        user = get_user(request)
        articles = Article.objects.order_by('-created_at', '-updated_at')
        return render(request, 'list_articles.html', {'articles': articles, 'user': user})


class MyArticles(View):
    def get(self, request):
        user = get_user(request)
        articles = Article.objects.filter(author=user).order_by('-created_at', '-updated_at')
        return render(request, 'my_articles.html', {'articles': articles, 'user': user})


class ViewArticle(View):
    def get(self, request, pk):
        user = get_user(request)
        article = Article.objects.get(id=pk)
        html_article = markdown(article.content)
        return render(request, 'article_page.html', {
            'article': article,
            'article_content': html_article, 
            'user': user
        })
