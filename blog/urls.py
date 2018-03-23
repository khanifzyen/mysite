from django.urls import path
from . import views

urlpatterns = [
    #path('',views.post_list,name='post_list'),
    path('',views.PostListView.as_view(),name='post_list'),
    path('<post_id>/share',views.post_share,name='post_share'),
    path('<year>/<month>/<day>/<post>',views.post_detail,name='post_detail')

]