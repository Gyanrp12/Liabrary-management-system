"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from myapp.views import RegisterView,LoginView,BookaddView,BookView,BookissuedView,BookcrudView,IssuedbookView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path("add_book/", BookaddView.as_view()),
    path("view_book/", BookView.as_view()),
    path("issued_book/", BookissuedView.as_view()),
    path('delete_book/',BookcrudView.as_view()),
    path('update_book/<int:pk>',BookcrudView.as_view()),
    path('viewissued_book/',IssuedbookView.as_view())
]
