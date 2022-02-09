from django.urls import path
from course import views

urlpatterns = [
    path('all/', views.get_all_courses ),
    path('', views.create_course ),
    path('update/<int:course_id>', views.update_course),
    path('delete/<int:course_id>', views.delete_course)
]