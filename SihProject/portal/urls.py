from django.urls import path
from portal import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.login_user, name='login_user'),
    path('register',views.register, name='register'),
    path('logout_user',views.logout_user,name='logout_user'),

    # Views for student

    path('student_home', views.student_home, name="student_home"),
    path('search_data_student',views.search_data_student, name="search_data_student"),
    path('student_tracking',views.student_tracking, name="student_tracking"),
    path('upload_data_student',views.upload_data_student, name='upload_student'),
    path('view_student_data/<id>',views.view_student_data, name='view_student_data'),
    path('back',views.back,name='back'),


    # Views for Staff

    path('staff_home', views.staff_home, name="staff_home"),
    path('search_data_staff',views.search_data_staff, name="search_data_staff"),
    path('staff_tracking',views.staff_tracking, name="staff_tracking"),
    path('upload_data_staff',views.upload_data_staff, name='upload_staff'),
    path('view_staff_data/<id>',views.view_staff_data, name='view_staff_data'),


    # Views for Admin

    path('admin_home', views.admin_home, name="admin_home"),
    path('search_data_admin',views.search_data_admin, name="search_data_sadmin"),
    path('admin_tracking',views.admin_tracking, name="admin_tracking"),
    path('upload_data_admin',views.upload_data_admin, name='upload_admin'),
    path('view_admin_data/<id>',views.view_admin_data, name='view_admin_data'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()
    