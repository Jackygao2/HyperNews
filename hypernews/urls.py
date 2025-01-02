"""hypernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from news.views import news_list, news_create, coming_soon, news_detail

from django.contrib import admin
from django.urls import path
from news.views import news_list, news_create, coming_soon, news_detail

from django.contrib import admin
from django.urls import path
from news.views import news_list, news_create, coming_soon, news_detail

from django.contrib import admin
from django.urls import path
from news.views import news_list, news_create, coming_soon, news_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', coming_soon, name='coming_soon'),  # Root URL for coming soon page
    path('news/', news_list, name='news_list'),
    path('news/create/', news_create, name='news_create'),
    path('news/<int:article_id>/', news_detail, name='news_detail'),  # Use <int:article_id> for integer-based links
]
