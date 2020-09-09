from django.urls import path
from . import views

urlpatterns = [
 # .as_view()는 우리가 상속받은 메소드들(ListView, CreateView 등등)에서 default로 저장되어있는 메소드
    path('', views.BlogView.as_view(), name='list'), # path 함수 안에 인자 -> url, 함수, urlpath 이름
    path('newblog/', views.BlogCreate.as_view(), name='new'),
    path('detail/<int:pk>', views.BlogDetail.as_view(), name='detail'),
    path('update/<int:pk>', views.BlogUpdate.as_view(), name='change'),
    path('delete/<int:pk>', views.BlogDelete.as_view(), name='del'),
    
]