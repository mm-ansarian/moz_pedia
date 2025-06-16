from django.urls import path
from .views import *


urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('account/', Account.as_view(), name='account_page'),
    path('signup/', Signup.as_view(), name='signup_page'),
    path('login/', Login.as_view(), name='login_page'),
    path('logout/', Logout.as_view(), name='logout_page'),
    path('create_article/', CreateArticle.as_view(), name='create_article_page'),
    path('edit_article/<int:pk>/', EditArticle.as_view(), name='edit_article_page'),
    path('list_articles/', ListArticles.as_view(), name='list_articles_page'),
    path('my_articles/', MyArticles.as_view(), name='my_articles_page'),
    path('article/<int:pk>/', ViewArticle.as_view(), name='article_page'),
]
