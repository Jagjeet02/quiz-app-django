from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import QuizSession, Question, QuizSessionAnswer

def home(request):
    return render(request, 'quiz/index.html')  # Ensure this template exists

def start_quiz(request):
    """
    Start a new quiz session and return session ID.
    """
    try:
        session = QuizSession.objects.create()
        return JsonResponse({'session_id': session.id})
    except Exception as e:
        return JsonResponse({'error': f'Failed to start quiz: {e}'}, status=500)

def get_question(request, session_id):
    """
    Fetch a random unanswered question.
    """
    try:
        session = get_object_or_404(QuizSession, id=session_id)
        
        # Fetch already answered question IDs
        answered_ids = QuizSessionAnswer.objects.filter(session=session).values_list('question_id', flat=True)

        # Fetch a question not yet answered
        question = Question.objects.exclude(id__in=answered_ids).order_by('?').first()

        if not question:
            return JsonResponse({"message": "No more questions available"}, status=200)

        return JsonResponse({
            "id": question.id,
            "question": question.text,
            "options": question.options
        })
    except Exception as e:
        return JsonResponse({'error': f'Error fetching question: {e}'}, status=500)

def submit_answer(request, session_id, question_id):
    """
    Submit an answer and store it in the database.
    """
    try:
        session = get_object_or_404(QuizSession, id=session_id)
        question = get_object_or_404(Question, id=question_id)

        # Fetch the chosen option
        selected_option = request.GET.get('option')
        if not selected_option:
            return JsonResponse({'error': 'No option selected'}, status=400)

        # Check if the answer is correct
        is_correct = question.correct_option == selected_option

        # Store the answer
        QuizSessionAnswer.objects.create(
            session=session,
            question=question,
            chosen_option=selected_option,
            is_correct=is_correct
        )

        return JsonResponse({'message': 'Answer submitted successfully.'})
    except Exception as e:
        return JsonResponse({'error': f'Error submitting answer: {e}'}, status=500)

def get_summary(request, session_id):
    """
    Return quiz summary for a session.
    """
    try:
        session = get_object_or_404(QuizSession, id=session_id)
        total = QuizSessionAnswer.objects.filter(session=session).count()
        correct = QuizSessionAnswer.objects.filter(session=session, is_correct=True).count()
        incorrect = total - correct

        return JsonResponse({
            "total": total,
            "correct": correct,
            "incorrect": incorrect
        })
    except Exception as e:
        return JsonResponse({'error': f'Error fetching summary: {e}'}, status=500)
