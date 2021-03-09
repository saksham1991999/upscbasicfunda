# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery import shared_task
# from demoapp.models import Widget
#from quiz import models
from django.db.models import Q, Count
from .models import *
import time 
import datetime

#@periodic_task(
#    run_every=(crontab(minute='*/1')),
#    name="auto_sumbit_task",
#    ignore_result=True
#)
@shared_task
def auto_sumbit_task():
        
        quiztakers = QuizTaker.objects.filter(completed=False)

        for i in quiztakers:
            if i.quiz.live==False:
                if datetime.datetime.now()>(i.starttime+i.quiz.duration):
                    quiztaker = QuizTaker.objects.get(id=i.id)
                    quiztaker.complete=1
                    quiztaker.date_finished=datetime.datetime.now()
                    correct_answers = 0

                    for users_answer in UsersAnswer.objects.filter(quiz_taker=quiztaker):
                        answer = Answer.objects.get(question=users_answer.question, is_correct=True)
                        if users_answer.answer == answer:
                            correct_answers += 1

                    quiztaker.score = int(correct_answers / quiztaker.quiz.question_set.count() * 100)

                    aggregate = QuizTaker.objects.filter(quiz_id =quiztaker.quiz.id,score__gt=quiztaker.score).aggregate(ranking=Count('score'))
                    quiztaker.quiz_day_rank = int(aggregate['ranking'] + 1)
                    quiztaker.save()

            if i.quiz.live == True:
                slots = QuizSlot.objects.filter(quiz=i.quiz)
                temp=False
                slot=None
                lastslot=slots[0]
                for j in slots:
                    if j.start_datetime>lastslot.start_datetime:
                        lastslot=j
                    if j.start_datetime>=datetime.datetime.now():
                        temp=True
                        slot=j
                        break 
                if temp == False:
                    if datetime.datetime.now()>(lastslot.start_datetime+quiztaker.quiz.duration):
                        quiztaker = QuizTaker.objects.get(id=i.id)
                        quiztaker.complete=True
                        quiztaker.date_finished=datetime.datetime.now()                      
                        correct_answers = 0

                        for users_answer in UsersAnswer.objects.filter(quiz_taker=quiztaker):
                            answer = Answer.objects.get(question=users_answer.question, is_correct=True)
                            if users_answer.answer == answer:
                                correct_answers += 1

                        quiztaker.score = int(correct_answers / quiztaker.quiz.question_set.count() * 100)

                        aggregate = QuizTaker.objects.filter(quiz_id =quiztaker.quiz.id,score__gt=quiztaker.score).aggregate(ranking=Count('score'))
                        quiztaker.quiz_day_rank = int(aggregate['ranking'] + 1)
                        quiztaker.save()
                else:
                    if datetime.datetime.now()>(slot.start_datetime+i.quiz.duration):
                        quiztaker = QuizTaker.objects.get(id=i.id)
                        quiztaker.complete=True
                        quiztaker.date_finished=datetime.datetime.now()
                        correct_answers = 0
                        for users_answer in UsersAnswer.objects.filter(quiz_taker=quiztaker):
                            answer = Answer.objects.get(question=users_answer.question, is_correct=True)
                            if users_answer.answer == answer:
                                correct_answers += 1

                        quiztaker.score = int(correct_answers / quiztaker.quiz.question_set.count() * 100)

                        aggregate = QuizTaker.objects.filter(quiz_id =quiztaker.quiz.id,score__gt=quiztaker.score).aggregate(ranking=Count('score'))
                        quiztaker.quiz_day_rank = int(aggregate['ranking'] + 1)
                        quiztaker.save()
        return True
@shared_task
def temp_task():
    Tester.objects.create(name="testing")
# from celery.task.schedules import crontab
# from celery.decorators import periodic_task
#
#
# @periodic_task(run_every=(crontab(minute='*/15')), name="some_task", ignore_result=True)
# def some_task():
    # do something


# @shared_task
# def EndQuiz(instance):
#     # datetimes = models.QuizSlot.objects.filter(quiz = quiz, start_datetime__gte = datetime.now())
#     # for start_datetime in datetimes:

#     # quiztakers = models.QuizTaker.objects.filter(quiz = quiz, completed=False)
#     # quiztakers.update(completed=True, date_finished = datetime.now())
#     # for quiztaker in quiztakers:
#     #     correct_answers = 0

#     #     for users_answer in models.UsersAnswer.objects.filter(quiz_taker=quiztaker):
#     #         answer = models.Answer.objects.get(question=users_answer.question, is_correct=True)
#     #         if users_answer.answer == answer:
#     #             correct_answers += 1

#     #     quiztaker.score = int(correct_answers / quiztaker.quiz.question_set.count() * 100)

#     #     aggregate = models.QuizTaker.objects.filter(score__lt=quiztaker.score).aggregate(ranking=Count('score'))
#     #     quiztaker.quiz_day_rank = int(aggregate['ranking'] + 1)

#     #     quiztaker.save()

#     # return True
#     print(instance)
#     print("ok")
#     quiztaker = models.QuizTaker.objects.get(id=instance)
#     print("here")
#     quizid=quiztaker.quiz_id
#     print(quizid)
#     quiz = models.Quiz.objects.get(id=quizid)
#     if quiztaker.completed:
#         print("quiz completed")
#         return True
#     if quiz.live==False:
        
#         time = str(quiz.duration)
#         hh, mm , ss = map(int, time.split(':'))
#         duration = ss + 60*(mm + 60*hh)

#         print(duration)
#         sleep(5)
#         quiztaker.complete=True
#         quiztaker.date_finished=datetime.now()
#         correct_answers = 0

#         for users_answer in models.UsersAnswer.objects.filter(quiz_taker=quiztaker):
#             answer = models.Answer.objects.get(question=users_answer.question, is_correct=True)
#             if users_answer.answer == answer:
#                 correct_answers += 1

#         quiztaker.score = int(correct_answers / quiztaker.quiz.question_set.count() * 100)

#         aggregate = models.QuizTaker.objects.filter(score__lt=quiztaker.score).aggregate(ranking=Count('score'))
#         quiztaker.quiz_day_rank = int(aggregate['ranking'] + 1)
#         print(quiztaker)
#         quiztaker.save()
#         print("quiz over")
#         # data={
#         #     "complete":True,
#         #     "date_finsihed":quiztaker.date_finished,
#         #     "score":quiztaker.score,
#         #     "quiz_day_rank":quiztaker.quiz_day_rank
#         # }
#     return True
