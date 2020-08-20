from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

#클래스 기반
class BookmarkLV(ListView):
     model = Bookmark
class BookmarkDV(DetailView):
     model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView):
     model = Bookmark
     fields = ['title', 'url'] # 폼 모델에 사용할 필드  폼 모델 자동 생성
     success_url = reverse_lazy('bookmark:index')
     def form_valid(self, form):
          form.instance.owner = self.request.user
          return super().form_valid(form)

class BookmarkChangeLV(LoginRequiredMixin, ListView):
     template_name = 'bookmark/bookmark_change_list.html'
     def get_queryset(self):
          return Bookmark.objects.filter(owner=self.request.user)

class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
     model = Bookmark
     fields = ['title', 'url'] # 폼 모델에 사용할 필드  폼 모델 자동 생성
     success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
     model = Bookmark
     success_url = reverse_lazy('bookmark:index')

#함수 기반
# def index(request):
#     object_list = Bookmark.objects.all()
#     print(object_list)
#     context = {'bookmark_list':object_list}
#     return render(request, 'bookmark/bookmark_list.html',context)
#
# def detail(request,pk):
#     object = Bookmark.objects.get(pk=pk)
#     context = {'bookmark' : object}
#     return render(request, 'bookmark/bookmark_detail.html',context)