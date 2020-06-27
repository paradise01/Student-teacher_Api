from django.urls import path, include 
from classroom import views

app_name = 'classroom'

urlpatterns =[
    path('api/', include('classroom.api.urls')),
    path('signup/',views.SignUp,name="signup"),
    path('signup/student_signup/',views.StudentSignUp,name="StudentSignUp"),
    path('signup/teacher_signup/',views.TeacherSignUp,name="TeacherSignUp"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('student/<int:pk>/',views.StudentDetailView.as_view(),name="student_detail"),
    path('student/<int:pk>/add',views.add_student.as_view(),name="add_student"),
    path('student_added/',views.student_added,name="student_added"),
    path('students_list/',views.students_list,name="students_list"),
    path('teacher/class_students_list',views.class_students_list,name="class_student_list"),
    path('teacher/write_notice',views.add_notice,name="write_notice"),
    path('student/<int:pk>/class_notice',views.class_notice,name="class_notice"),
    path('upload_assignment/',views.upload_assignment,name="upload_assignment"),
    path('class_assignment/',views.class_assignment,name="class_assignment"),
    path('submit_assignment/<int:id>/',views.submit_assignment,name="submit_assignment"),
    path('submit_list/',views.submit_list,name="submit_list"),
    
]
