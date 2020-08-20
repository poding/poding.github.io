from django.urls import path

from bookmark.views import *

app_name = 'bookmark'  # 해당 애플리케이션의 네임스페이스명

urlpatterns = [
    # mysite urls에서 북마크 뒤에 북마크 urls가 경로가되는데 빈문자열음 그냥
    # 북마크 목록이 보이는 화면이고 뒤에 인트형식의 기본키가 값이오면(상세값) 그 목록
    # 에 대한 정보로 가는 주소가 된다

    # 클래스 기반
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),

    # Example: /bookmark/add/
    path('add/', BookmarkCreateView.as_view(), name="add"),
    # Example: /bookmark/change/
    path('change/', BookmarkChangeLV.as_view(), name="change"),
    # Example: /bookmark/99/update/
    path('<int:pk>/update/', BookmarkUpdateView.as_view(), name="update"),
    # Example: /bookmark/99/delete/
    path('<int:pk>/delete/', BookmarkDeleteView.as_view(), name="delete"),

    # function-based views
    # path('bookmark/', index, name='index'),
    # path('bookmark/<int:pk>', detail, name='detail')
]
