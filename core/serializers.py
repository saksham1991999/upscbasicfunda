from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from quiz.models import *
from . import models


from quiz.serializers import *

import datetime
from datetime import datetime,timedelta
from pytz import timezone



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('email', 'username', 'password', 'mobile', 'profile_pic', 'first_name', 'last_name')


class CustomRegisterSerializer(RegisterSerializer):
    mobile = serializers.CharField(allow_blank = True, allow_null=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField(allow_blank = True, allow_null=True)
    email = serializers.EmailField(allow_blank = True, allow_null=True)


    class Meta:
        model = models.User
        fields = ('email', 'username', 'password', 'mobile', 'first_name', 'last_name')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'mobile': self.validated_data.get('mobile', ''),

        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.mobile = self.cleaned_data.get('mobile')
        user.save()
        adapter.save_user(request, user, self)
        return user


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ('key', 'user')

class TeamMemberSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="team-members-detail")

    class Meta:
        model = models.TeamMember
        fields = ['id', 'image', 'name', 'designation']

class TeamFormSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="team-form-detail")

    class Meta:
        model = models.TeamForm
        fields = ['id', 'full_name', 'email', 'mobile', 'cv', 'other_document']

class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ContactUs
        fields = ['id', 'full_name', 'email', 'mobile', 'message']

class FeedbackSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="feedback-detail")

    class Meta:
        model = models.Feedback
        fields = ['id', 'experience', 'message', 'is_bug']

class FAQSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="faqs-detail")

    class Meta:
        model = models.FAQ
        fields = ['id', 'question', 'answer']

class ArticleSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="articles-detail")

    class Meta:
        model = models.Article
        fields = ['id', 'title', 'image', 'date', 'content']

class NewsSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="news-detail")

    class Meta:
        model = models.News
        fields = ['id', 'title', 'image', 'date', 'content']


class NewsletterSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="newsletter-detail")

    class Meta:
        model = models.Newsletter
        fields = ['id', 'email']

class CategorySerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="core:category-detail")

    class Meta:
        model = models.Category
        fields = ['id', 'name']

class SubCategorySerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="core:sub-category-detail")

    class Meta:
        model = models.SubCategory
        fields = ['id', 'name']


class PDFSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="core:pdf-detail")
    sub_category = SubCategorySerializer(many=False, read_only = True)
    type = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = models.PDF
        fields = [ 'id', 'name', 'file', 'price', 'sub_category', 'type']

    def get_type(self, obj):
        return "pdf"

class PDFListSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="core:pdf-detail")
    sub_category = SubCategorySerializer(many=False, read_only = True)
    type = serializers.SerializerMethodField(read_only = True)
    file = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.PDF
        fields = ['id', 'name', 'price', 'sub_category', 'file', 'type']

    def get_type(self, obj):
        return "pdf"

    def get_file(self,obj):

        if obj.price<1:
            file =self.context['request'].build_absolute_uri(obj.file.url)
            # return obj.file.url
            return file
        
        user = self.context['request'].user
        if user.id is not None:
            sub = models.UserSubscriptions.get(user = user)
            if obj in sub.pdfs.all():
                file =self.context['request'].build_absolute_uri(obj.file.url)
                # return obj.file.url
                return file
        else:
            return None

class MCQSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="core:mcq-detail")
    sub_category = SubCategorySerializer(many=False, read_only = True)
    type = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = models.MCQ
        fields = ['id', 'name', 'file', 'price', 'sub_category', 'image', 'preview_file', 'description', 'type']

    def get_type(self, obj):
        return "mcq"

class MCQListSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="core:mcq-detail")
    sub_category = SubCategorySerializer(many=False, read_only = True)
    type = serializers.SerializerMethodField(read_only = True)
    file = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.MCQ
        fields = [ 'id', 'file', 'name', 'price', 'sub_category', 'image', 'preview_file', 'description', 'type', "file"]

    def get_type(self, obj):
        return "mcq"

    def get_file(self,obj):

        if obj.price<1:
            file =self.context['request'].build_absolute_uri(obj.file.url)
            # return obj.file.url
            return file
        
        user = self.context['request'].user
        if user.id is not None:
            sub = models.UserSubscriptions.objects.get(user = user)
            if obj in sub.mcqs.all():
                file =self.context['request'].build_absolute_uri(obj.file.url)
                # return obj.file.url
                return file
        else:
            return None

class SummarySerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="core:summary-detail")
    sub_category = SubCategorySerializer(many=False, read_only = True)
    mcq = MCQSerializer(many=True, read_only = True)
    type = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = models.Summary
        fields = ['id', 'name', 'file', 'price', 'sub_category', 'description','mcq', 'image', 'preview_file', 'type']

    def get_type(self, obj):
        return "summary"

class SummaryListSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="core:summary-detail")
    sub_category = SubCategorySerializer(many=False, read_only = True)
    mcq = MCQListSerializer(many=True, read_only = True)
    type = serializers.SerializerMethodField(read_only = True)
    file = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Summary
        fields = ['id', 'name', 'price', 'sub_category', 'description','mcq',  'image', 'preview_file', 'type',"file"]

    def get_type(self, obj):
        return "summary"
    
    def get_file(self,obj):

        if obj.price<1:
            file =self.context['request'].build_absolute_uri(obj.file.url)
            # return obj.file.url
            return file
        
        user = self.context['request'].user
        if user.id is not None:
            sub = models.UserSubscriptions.objects.get(user = user)
            if obj in sub.summaries.all():
                file =self.context['request'].build_absolute_uri(obj.file.url)
                # return obj.file.url
                return file
        else:
            return None

class SessionSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="core:session-detail")
    type = serializers.SerializerMethodField(read_only = True)
    upcoming = serializers.SerializerMethodField(read_only = True)
    
    class Meta:
        model = models.Session
        fields = ['id', 'name', 'image', 'price', 'date', 'video','youtube_link', 'type', 'upcoming', 'demo']

    def get_type(self, obj):
        return "session"

    def get_upcoming(self, obj):
        if obj.date > datetime.date.today():
            return True
        else:
            return False

class SessionListSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="core:session-detail")
    type = serializers.SerializerMethodField(read_only = True)
    upcoming = serializers.SerializerMethodField(read_only = True)
    file = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.Session
        fields = ['id', 'name', 'image', 'price', 'date','youtube_link', 'type', 'upcoming', 'demo',"file"]

    def get_type(self, obj):
        return "session"

    def get_upcoming(self, obj):
        if obj.date > datetime.date.today():
            return True
        else:
            return False
    
    def get_file(self,obj):

        if obj.price<1:
            file =self.context['request'].build_absolute_uri(obj.file.url)
            # return obj.file.url
            return file
        
        user = self.context['request'].user
        if user.id is not None:
            sub = models.UserSubscriptions.objects.get(user = user)
            if obj in sub.sessions.all():
                file =self.context['request'].build_absolute_uri(obj.file.url)
                # return obj.file.url
                return file
        else:
            return None

class UserSubscriptionsSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="core:user-subscription-detail")
    user = UserSerializer(many=False, read_only = True)
    pdfs = PDFSerializer(many=True, read_only = True)
    mcqs = MCQListSerializer(many=True, read_only = True)
    summaries = SummaryListSerializer(many=True, read_only = True)
    sessions = SessionListSerializer(many=True, read_only = True)
    tests = QuizListSerializer(many=True, read_only = True)

    class Meta:
        model = models.UserSubscriptions
        fields = ['id', 'user', 'pdfs', 'mcqs', 'summaries', 'sessions', 'tests']

class SearchSerializer(serializers.Serializer):

    # pdfs = PDFListSerializer(many=True, read_only = True)
    # mcqs = MCQListSerializer(many=True, read_only = True)
    # summaries = SummarySerializer(many=True, read_only = True)
    # sessions = SessionSerializer(many=True, read_only = True)
    # tests = QuizListSerializer(many=True, read_only = True)

    pdfs = serializers.SerializerMethodField('get_pdfs')
    mcqs = serializers.SerializerMethodField('get_mcqs')
    summaries = serializers.SerializerMethodField('get_summaries')
    sessions = serializers.SerializerMethodField('get_sessions')
    tests = serializers.SerializerMethodField('get_tests')

    class Meta:
        fields =["pdfs","mcqs","summaries","sessions","tests"]

    def get_pdfs(self,obj):
        serializer_context = {'request': self.context.get('request') }
        queryset = obj.pdfs
        serializer = PDFListSerializer(queryset, many=True, context=serializer_context)
        return serializer.data

    def get_mcqs(self,obj):
        serializer_context = {'request': self.context.get('request') }
        queryset = obj.mcqs
        serializer = MCQListSerializer(queryset, many=True, context=serializer_context)
        return serializer.data

    def get_summaries(self,obj):
        serializer_context = {'request': self.context.get('request') }
        queryset = obj.summaries
        serializer = SummaryListSerializer(queryset, many=True, context=serializer_context)
        return serializer.data

    def get_sessions(self,obj):
        serializer_context = {'request': self.context.get('request') }
        queryset = obj.sessions
        serializer = SessionListSerializer(queryset, many=True, context=serializer_context)
        return serializer.data

    def get_tests(self,obj):
        serializer_context = {'request': self.context.get('request') }
        queryset = obj.tests
        serializer = QuizListSerializer(queryset, many=True, context=serializer_context)
        return serializer.data
class GeneralNotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GeneralNotification
        fields = '__all__'

class PersonalNotification(serializers.ModelSerializer):

    class Meta:
        model = models.PersonalNotification
        fields = '__all__'

class Personalnotif(serializers.ModelSerializer):

#    quiz = QuizMInSerializer(many=True)
    quizinfo = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    class Meta:

        model = models.PersonalNotification
        fields = '__all__'
    
    def get_quizinfo(self,obj):

        now = datetime.now(timezone("Asia/Calcutta"))
        quiz = Quiz.objects.get(id=obj.quiz_id)

        quizSlot =  QuizSlot.objects.filter(quiz=quiz)
        for slot in quizSlot:
            if now>=slot.start_datetime and now<=(slot.start_datetime+quiz.duration):
                data={
                    "date":(slot.start_datetime+timedelta(hours=5,minutes=30)).strftime("%b %d %Y"),
                    "time":(slot.start_datetime+timedelta(hours=5,minutes=30)).strftime("%H:%M:%S")
                }
                return data
            elif now<slot.start_datetime and now<(slot.start_datetime+quiz.duration):
                data={
                    "date":(slot.start_datetime+timedelta(hours=5,minutes=30)).strftime("%b %d %Y"),
                    "time":(slot.start_datetime+timedelta(hours=5,minutes=30)).strftime("%H:%M:%S")
                }
                return data

    def get_duration(self,obj):
        quiz = Quiz.objects.get(id=obj.quiz_id)

        return (str(quiz.duration))














