# Create your tasks here

from celery import shared_task
# from demoapp.models import Widget
from quiz import models
from datetime import datetime
from django.db.models import Q, Count

from time import sleep


# from celery.task.schedules import crontab
# from celery.decorators import periodic_task
#
#
# @periodic_task(run_every=(crontab(minute='*/15')), name="some_task", ignore_result=True)
# def some_task():
    # do something


@shared_task
def EndQuiz(instance):
    # datetimes = models.QuizSlot.objects.filter(quiz = quiz, start_datetime__gte = datetime.now())
    # for start_datetime in datetimes:

    # quiztakers = models.QuizTaker.objects.filter(quiz = quiz, completed=False)
    # quiztakers.update(completed=True, date_finished = datetime.now())
    # for quiztaker in quiztakers:
    #     correct_answers = 0

    #     for users_answer in models.UsersAnswer.objects.filter(quiz_taker=quiztaker):
    #         answer = models.Answer.objects.get(question=users_answer.question, is_correct=True)
    #         if users_answer.answer == answer:
    #             correct_answers += 1

    #     quiztaker.score = int(correct_answers / quiztaker.quiz.question_set.count() * 100)

    #     aggregate = models.QuizTaker.objects.filter(score__lt=quiztaker.score).aggregate(ranking=Count('score'))
    #     quiztaker.quiz_day_rank = int(aggregate['ranking'] + 1)

    #     quiztaker.save()

    # return True
    print(instance)
    print("ok")
    quiztaker = models.QuizTaker.objects.get(id=instance)
    print("here")
    quizid=quiztaker.quiz_id
    print(quizid)
    quiz = models.Quiz.objects.get(id=quizid)
    if quiz.live==False:
        
        time = str(quiz.duration)
        hh, mm , ss = map(int, time.split(':'))
        duration = ss + 60*(mm + 60*hh)

        print(duration)
        sleep(duration)

        quiztaker.complete=True
        quiztaker.date_finished=datetime.now()
        correct_answers = 0

        for users_answer in models.UsersAnswer.objects.filter(quiz_taker=quiztaker):
            answer = models.Answer.objects.get(question=users_answer.question, is_correct=True)
            if users_answer.answer == answer:
                correct_answers += 1

        quiztaker.score = int(correct_answers / quiztaker.quiz.question_set.count() * 100)

        aggregate = models.QuizTaker.objects.filter(score__lt=quiztaker.score).aggregate(ranking=Count('score'))
        quiztaker.quiz_day_rank = int(aggregate['ranking'] + 1)

        quiztaker.save()
        print("quiz over")

    return True
