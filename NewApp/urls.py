from django.urls import path
from NewApp import views
urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('add_book_page/',views.add_book_page,name="add_book_page"),
    path('save_book/',views.save_book,name="save_book"),
    path('display_book/',views.display_book,name="display_book"),
    path('edit_book/<int:dataid>/',views.edit_book,name="edit_book"),
    path('update_book/<int:dataid>/',views.update_book,name="update_book"),
    path('remv_book/<int:dataid>/',views.remv_book,name="remv_book"),
    path('add_details/',views.add_details,name="add_details"),
    path('save_details/',views.save_details,name="save_details"),
    path('display_details/',views.display_details,name="display_details"),
    path('edit_details/<int:dataid>/', views.edit_details, name="edit_details"),
    path('update_details/<int:dataid>/',views.update_details,name="update_details"),
    path('remv_details/<int:dataid>/', views.remv_details, name="remv_details"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('display_contact/',views.display_contact,name="display_contact"),
    path('deletecontact/<int:dataid>/',views.deletecontact,name="deletecontact")





]