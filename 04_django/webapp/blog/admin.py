from django.contrib import admin
from blog.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
 list_display = ('id', 'title', 'modify_dt', 'tag_list')
 list_filter = ('modify_dt',)
 search_fields = ('title','content')
 #미리 기존에 값을 통해서 확장시키는 필드 그게 슬러그라는 대상이고, 타이틀 값으로 슬러그를 만들어내겠다
 prepopulated_fields = { 'slug' : ('title', )}

 def get_queryset(self, request):
  return super().get_queryset(request).prefetch_related('tags')
 def tag_list(self, obj):
  return ', '.join(o.name for o in obj.tags.all())
 #컴마조인은 뒤에 튜플이든 리스트든 콤마로 묶어라  컴프리핸서형태(o.name for o in obj.tags.all())
