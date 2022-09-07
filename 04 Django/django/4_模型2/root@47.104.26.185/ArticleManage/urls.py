"""blog URL Configuration

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

from django.urls import path

from ArticleManage import views
app_name = 'ArticleManage'
urlpatterns = [
    path('delete/<int:aid>/<int:cid>/<int:page>/', views.delete_article, name='delete'),
    path('publish/<int:cid>/',views.publish_article, name='publish'),
    path('update/<int:cid>/<int:aid>/',views.update_article, name='update'),

]
