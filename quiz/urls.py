from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/start/', views.start_quiz, name='start_quiz'),
    path('quiz/question/<int:session_id>/', views.get_question, name='quiz_page'),
    path('quiz/answer/<int:session_id>/<int:question_id>/', views.submit_answer, name='submit_answer'),
    path('quiz/summary/<int:session_id>/', views.get_summary, name='summary_page'),
]
