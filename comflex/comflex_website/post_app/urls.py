from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.all_postings, name="home"),
    path('create_community', views.create_community, name="create-community"),
    path('list_communities', views.list_communities, name="list-communities"),
    path('discover', views.discover, name='discover'),
    path('my_communities', views.my_communities, name="my-communities"),
    path('show_community/<int:community_id>', views.show_community, name="show-community"),
    path('search_communities', views.search_communities, name="search-communities"),
    path('advanced_search', views.advanced_search, name='advanced-search'),
    path('advanced_search_results/', views.advanced_search_results, name='advanced-search-results'),
    path('modify_community/<int:community_id>', views.modify_community, name="modify-community"),
    path('modify_post/<int:posting_id>', views.modify_post, name="modify-post"),
    path('create_post/', views.create_post, name='create-post'),  # No parameter needed here
    path('create_post_form/', views.create_post_form, name='create-post-form'),   
    path('liked_posts', views.my_liked_posts, name="liked-posts"),
    path('my_posts', views.my_postings, name="my-posts"), 
    path('community/<int:community_id>/join/', views.join_community, name='join-community'),
    path('community/<int:community_id>/leave/', views.leave_community, name='leave-community'),
    path('community/<int:community_id>/add_post_type/', views.add_post_type, name='add-post-type'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('dislike_post/<int:post_id>/', views.dislike_post, name='dislike_post'),
    path('community/<int:community_id>/transfer_ownership/', views.transfer_ownership, name='transfer-ownership'),
    path('community/<int:community_id>/members/', views.show_community, {'template_name': 'posts/community_members.html'}, name='community-members'),
    path('community/<int:community_id>/add-moderator/', views.add_moderator, name='add-moderator'),
    path('community/<int:community_id>/remove-moderator/<int:user_id>/', views.remove_moderator, name='remove-moderator'),
    path('community/<int:community_id>/resign-moderator/', views.resign_moderator, name='resign-moderator'),
    path('community/<int:community_id>/dismiss-user/<int:user_id>/', views.dismiss_user, name='dismiss-user'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
