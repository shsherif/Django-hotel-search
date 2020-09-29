from django.urls import path
from blog.views import all_posts, single_post,new_post,edit_post, PostList, PostDetail, PostUpdate


app_name='blog'

urlpatterns = [
    path('', all_posts, name='blog_list'),
    path('new', new_post, name='new_post'),
    path('<int:id>', single_post, name='blog_detail'),
    path('<int:id>/edit', edit_post, name='post_edit'),
    
    path('cbv', PostList.as_view()),
    path('cbv/<int:pk>', PostDetail.as_view()),
    path('cbv/<int:pk>/edit', PostUpdate.as_view()),


]


