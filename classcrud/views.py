from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy # redirect시켜주는 함수 
from django.views.generic.list import ListView # 데이터 보여주는 클래스 메소드
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import ClassBlog

# 각 클래스 메소드를 상속
class BlogView(ListView): # html 탬플릿 : 블로그 리스트를 담은 html : (소문자모델)_list.html 로 이름을 지어야 한다
    model = ClassBlog # ClassBlog라는 모델로 만들어진 객체들의 목록을 본다

class BlogCreate(CreateView): # html : 입력공간(form)을 갖고있는 html : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list') # 'list'라는 url 이름으로 redirect

class BlogDetail(DetailView): # html : 상세 페이지를 담은 html : (소문자모델)_detail.html
    model = ClassBlog # DetailView에서 상세 작업들을 해준다

class BlogUpdate(UpdateView): # html : 입력공간(form)을 갖고있는 html : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list') # BlogCreate와 같은 원리

class BlogDelete(DeleteView): # html : 정말 지울것인지 확인하는 html : (소문자모델)_confirm_delete.html
    model = ClassBlog
    success_url = reverse_lazy('list')