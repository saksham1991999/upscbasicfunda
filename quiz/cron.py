from .models import *
import datetime

def ~():
        
        quiztakers = QuizTaker.objects.filter(completed=False)

        for quiztaker in quiztakers:
            if quiztaker.quiz.live==False:
                if datetime.datetime.now()>(quiztaker.starttime+quiztaker.quiz.duration):
                    quiztaker.complete=True
                    quiztaker.date_finished=datetime.now()
                    correct_answers = 0

                    for users_answer in models.UsersAnswer.objects.filter(quiz_taker=quiztaker):
                        answer = models.Answer.objects.get(question=users_answer.question, is_correct=True)
                        if users_answer.answer == answer:
                            correct_answers += 1

                    quiztaker.score = int(correct_answers / quiztaker.quiz.question_set.count() * 100)

                    aggregate = models.QuizTaker.objects.filter(score__gt=quiztaker.score).aggregate(ranking=Count('score'))
                    quiztaker.quiz_day_rank = int(aggregate['ranking'] + 1)
                    quiztaker.save()

            if quiztaker.quiz.live == True:
                slots = QuizSlot.objects.filter(quiz=quiztaker.quiz)
                temp=False
                slot=None
                for i in slots:
                    if i.start_datetime>=datetime.datetime.now():
                        temp=True
                        slot=i
                        break 
                if temp == False:
                    if datetime.datetime.now()>(quiztaker.starttime+quiztaker.quiz.duration):
                        quiztaker.complete=True
                        quiztaker.date_finished=datetime.now()
                        correct_answers = 0

                        for users_answer in models.UsersAnswer.objects.filter(quiz_taker=quiztaker):
                            answer = models.Answer.objects.get(question=users_answer.question, is_correct=True)
                            if users_answer.answer == answer:
                                correct_answers += 1

                        quiztaker.score = int(correct_answers / quiztaker.quiz.question_set.count() * 100)

                        aggregate = models.QuizTaker.objects.filter(score__gt=quiztaker.score).aggregate(ranking=Count('score'))
                        quiztaker.quiz_day_rank = int(aggregate['ranking'] + 1)
                        quiztaker.save()
                else:
                    if datetime.datetime.now()>(slot.start_datetime+quiztaker.quiz.duration):
                        quiztaker.complete=True
                        quiztaker.date_finished=datetime.now()
                        correct_answers = 0

                        for users_answer in models.UsersAnswer.objects.filter(quiz_taker=quiztaker):
                            answer = models.Answer.objects.get(question=users_answer.question, is_correct=True)
                            if users_answer.answer == answer:
                                correct_answers += 1

                        quiztaker.score = int(correct_answers / quiztaker.quiz.question_set.count() * 100)

                        aggregate = models.QuizTaker.objects.filter(score__gt=quiztaker.score).aggregate(ranking=Count('score'))
                        quiztaker.quiz_day_rank = int(aggregate['ranking'] + 1)
                        quiztaker.save()