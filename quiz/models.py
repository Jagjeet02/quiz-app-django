from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    options = models.JSONField()
    correct_option = models.CharField(max_length=1)

    def __str__(self):
        return self.text

class QuizSession(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class QuizSessionAnswer(models.Model):
    session = models.ForeignKey(QuizSession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chosen_option = models.CharField(max_length=1)
    is_correct = models.BooleanField()
