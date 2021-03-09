from django.db.models import Q, Count
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from quiz.models import Answer, Question, Quiz, QuizTaker, UsersAnswer
from quiz.serializers import MyQuizListSerializer, QuizDetailSerializer, QuizListSerializer, QuizResultSerializer, UsersAnswerSerializer, QuizLeaderBoardSerializer,QuizListSerializer2
from core import models as coremodels
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import datetime
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime,timedelta
from pytz import timezone
#from quiz.tasks import EndQuiz
from django.core.mail import EmailMessage

class MyQuizListAPI(generics.ListAPIView):
	permission_classes = [
		permissions.IsAuthenticated
	]
	serializer_class = MyQuizListSerializer

	def get_queryset(self, *args, **kwargs):
		queryset = Quiz.objects.filter(quiztaker__user=self.request.user)
		query = self.request.GET.get("q")
		complete = self.request.GET.get("complete")

		if query:
			queryset = queryset.filter(
				Q(name__icontains=query) |
				Q(description__icontains=query)
			).distinct()
		
		return queryset
	
	def list(self,request,*args,**kwargs):
		qs = self.get_queryset()
		serializer = self.serializer_class(qs,context={'request': self.request},many=True)
		complete = request.GET.get("complete")
		data=list()
		data2=list()
		if complete:
			complete=complete.lower()
			for i in serializer.data:
				if i['complete']:
					data.append(i)
				else:
					data2.append(i)
		if complete:
			if complete == 'true':
				return Response(data)
			elif complete == 'false':
				return Response(data2)
		else:
			return Response(serializer.data)


class QuizListAPI(generics.ListAPIView):
	serializer_class = QuizListSerializer2
	permission_classes = [
		permissions.AllowAny,
	]

	def get_queryset(self, *args, **kwargs):
		queryset = Quiz.objects.filter(roll_out=True)
		# .exclude(quiztaker__user=self.request.user)
		query = self.request.GET.get("q")

		if query:
			queryset = queryset.filter(
				Q(name__icontains=query) |
				Q(description__icontains=query)
			).distinct()

		return queryset.order_by("-id")
	
	def list(self,request,*args,**kwargs):
		qs = self.get_queryset()

		serializer = self.serializer_class(qs,many=True)
		live = request.GET.get("live")
		data=list()
		data2=list()
		if live:
			live=live.lower()
			for i in serializer.data:
				if i['islive']:
					data.append(i)
				else:
					data2.append(i)
		if live:
			if live == 'true':
				return Response(data)
			elif live == 'false':
				return Response(data2)
		else:
			return Response(serializer.data)




class QuizDetailAPI(generics.RetrieveAPIView):
	serializer_class = QuizDetailSerializer
	permission_classes = [
		permissions.IsAuthenticated
	]

	def get(self, *args, **kwargs):
		slug = self.kwargs["slug"]
		quiz = get_object_or_404(Quiz, slug=slug)

		subscribed = get_object_or_404(coremodels.UserSubscriptions, user=self.request.user)
		if (quiz not in subscribed.tests.all()) and (quiz.price > 1):
			return Response({"message": "Test Not Purchased"}, status=HTTP_400_BAD_REQUEST)

		last_question = None
		obj, created = QuizTaker.objects.get_or_create(user=self.request.user, quiz=quiz)
		if created:
			# now = datetime.now(timezone("Asia/Calcutta"))
			# current_time = now.strftime("%H:%M:%S")
			# obj.timestart = now
			obj.save()
			for question in Question.objects.filter(quiz=quiz):
				UsersAnswer.objects.create(quiz_taker=obj, question=question)
			# print(created)
			# EndQuiz.delay(created)
		else:
			# print(obj.id)
			# EndQuiz.delay(obj.id)
			last_question = UsersAnswer.objects.filter(quiz_taker=obj, answer__isnull=False)
			if last_question.count() > 0:
				last_question = last_question.last().question.id
			else:
				last_question = None

		return Response({'quiz': self.get_serializer(quiz, context={'request': self.request}).data, 'last_question_id': last_question})

class QuizLeaderBoardAPI(generics.RetrieveAPIView):
	serializer_class = QuizLeaderBoardSerializer
	permission_classes = [
		permissions.IsAuthenticated
	]

	def get(self, *args, **kwargs):
		slug = self.kwargs["slug"]
		quiz = get_object_or_404(Quiz, slug=slug)
		return Response(self.get_serializer(quiz, context={'request': self.request}).data)

class SaveUsersAnswer(generics.UpdateAPIView):
	serializer_class = UsersAnswerSerializer
	permission_classes = [
		permissions.IsAuthenticated
	]

	def patch(self, request, *args, **kwargs):


		quiztaker_id = request.data['quiztaker']
		question_id = request.data['question']


		quiztaker = get_object_or_404(QuizTaker, id=quiztaker_id)
		question = get_object_or_404(Question, id=question_id)

		# if answer_id is None:
		# 	answer = get_object_or_404(Answer, id=answer_id)
		# else:
		# 	answer = None
		try:			
			answer_id = request.data['answer']
			answer = get_object_or_404(Answer, id=answer_id)
		except:
			obj = get_object_or_404(UsersAnswer, quiz_taker=quiztaker, question=question)
			obj.answer = None 
			obj.save()
			return Response(self.get_serializer(obj).data)
		if quiztaker.completed:
			return Response({
				"message": "This quiz is already complete. you can't answer any more questions"},
				status=status.HTTP_412_PRECONDITION_FAILED
			)

		obj = get_object_or_404(UsersAnswer, quiz_taker=quiztaker, question=question)
		obj.answer = answer
		obj.save()


		return Response(self.get_serializer(obj).data)

class SubmitQuizAPI(generics.GenericAPIView):
	serializer_class = QuizResultSerializer
	permission_classes = [
		permissions.IsAuthenticated
	]

	def post(self, request, *args, **kwargs):
		quiztaker_id = request.data['quiztaker']
		# question_id = request.data['question']
		# answer_id = request.data['answer']

		quiztaker = get_object_or_404(QuizTaker, id=quiztaker_id)
		# question = get_object_or_404(Question, id=question_id)

		quiz = Quiz.objects.get(slug=self.kwargs['slug'])

		if quiztaker.completed:
			return Response({
				"message": "This quiz is already complete. You can't submit again"},
				status=status.HTTP_412_PRECONDITION_FAILED
			)

		# if answer_id is not None:
		# 	answer = get_object_or_404(Answer, id=answer_id)
		# 	obj = get_object_or_404(UsersAnswer, quiz_taker=quiztaker, question=question)
		# 	obj.answer = answer
		# 	obj.save()

		quiztaker.completed = True
		quiztaker.date_finished = datetime.now()
		correct_answers = 0

		for users_answer in UsersAnswer.objects.filter(quiz_taker=quiztaker):
			answer = Answer.objects.get(question=users_answer.question, is_correct=True)
			if users_answer.answer == answer:
				correct_answers += 1

		quiztaker.score = int(correct_answers / quiztaker.quiz.question_set.count() * 100)

		aggregate = QuizTaker.objects.filter(quiz_id =quiz.id,score__gt=quiztaker.score).aggregate(ranking=Count('score'))
		quiztaker.quiz_day_rank = int(aggregate['ranking'] + 1)

		quiztaker.save()

		email = EmailMessage(subject='Answer Key',body='Dear Student,\n\nThank You for answering the quiz using UpscBasicFunda Site. \n\nThe Answer key is attached along with this mail. Please compare your answers with key. \n\nIf there are any issues in the answer key please free to contact the support team.  \n\nRegards,\nTeam UpscBasicFunda',from_email='testingserver.12307@gmail.com',to=[request.user.email,])

		path= quiz.answerkey.path
		attachment = open(path, 'rb')

		email.attach(path,attachment.read(),'application/pdf')

		email.send()
		return Response(self.get_serializer(quiz).data)



