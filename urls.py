from django.urls import path
from LibApp import views
urlpatterns=[
    path('libaray/',views.libaray,name='libaray'),
    path('addbook/',views.add_book,name='add_book'),
    path('book_details/',views.book_details,name='book_details'),
    path('save_book/',views.save_book,name='save_book'),
    path('delete_book/<int:book_id>/',views.delete_book,name='delete_book'),
    path('edit_book/<int:book>/',views.edit_book,name='edit_book'),
    path('update_book/<int:book>/',views.update_book,name='update_book'),
    path('add_user',views.add_user,name='add_user'),
    path('user_details',views.user_details,name='user_details'),
    path('save_user',views.save_user,name='save_user'),
    path('user_detail',views.user_detail,name='user_detail'),


]