from rest_framework import serializers
from core.serializers import *
from . import models
from quiz.serializers import *
import razorpay
from django.conf import settings

class UserCartSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only = True)
    pdfs = PDFSerializer(many=True, read_only = True)
    mcqs = MCQSerializer(many=True, read_only = True)
    summaries = SummarySerializer(many=True, read_only = True)
    sessions = SessionSerializer(many=True, read_only = True)
    tests = QuizListSerializer(many=True, read_only = True)
    order_id = serializers.SerializerMethodField(read_only = True)
    total_amount = serializers.SerializerMethodField(read_only = True)
    final_amount = serializers.SerializerMethodField(read_only = True)
    promo_code = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = models.UserCart
        fields = ['id', 'user', 'pdfs', 'mcqs', 'summaries', 'sessions', 'start_date', 'ordered_date', 'ordered', 'tests','promocode', 'order_id', 'total_amount','final_amount','promo_code']

    def get_order_id(self, obj):
        amount = 0
        for pdf in obj.pdfs.all():
            amount += pdf.price
        for mcq in obj.mcqs.all():
            amount += mcq.price
        for summary in obj.summaries.all():
            amount += summary.price
        for session in obj.sessions.all():
            amount += session.price
        for test in obj.tests.all():
            amount += test.price
        if obj.promocode is not None:
            discount = (obj.promocode.percent * amount)/100
            amount=amount-discount
        data = {
            "amount" : amount*100,
            "currency" : 'INR',
            "receipt" : str(obj.id),
            "payment_capture" : '1',
        }
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        order_id = client.order.create(data = data)
        obj.order_id = order_id["id"]
        obj.save()
        return order_id


    def get_total_amount(self, obj):
        amount = 0
        for pdf in obj.pdfs.all():
            amount += pdf.price
        for mcq in obj.mcqs.all():
            amount += mcq.price
        for summary in obj.summaries.all():
            amount += summary.price
        for session in obj.sessions.all():
            amount += session.price
        for test in obj.tests.all():
            amount += test.price
        return amount
    
    def get_final_amount(self,obj):
        amount = 0
        for pdf in obj.pdfs.all():
            amount += pdf.price
        for mcq in obj.mcqs.all():
            amount += mcq.price
        for summary in obj.summaries.all():
            amount += summary.price
        for session in obj.sessions.all():
            amount += session.price
        for test in obj.tests.all():
            amount += test.price
        if obj.promocode is not None:
            discount = (obj.promocode.percent * amount)/100
            return (amount-discount)
        return amount
        
    def get_promo_code(self,obj):
        if obj.promocode is not None:
            return obj.promocode.code
        return None

class UserBookmarkSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only = True)
    pdfs = PDFSerializer(many=True, read_only = True)
    mcqs = MCQSerializer(many=True, read_only = True)
    summaries = SummarySerializer(many=True, read_only = True)
    sessions = SessionSerializer(many=True, read_only = True)
    tests = QuizListSerializer(many=True, read_only = True)

    class Meta:
        model = models.Bookmark
        fields = ['id', 'user', 'pdfs', 'mcqs', 'summaries', 'sessions', 'tests']


class UserSaveForLaterSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only = True)
    pdfs = PDFSerializer(many=True, read_only = True)
    mcqs = MCQSerializer(many=True, read_only = True)
    summaries = SummarySerializer(many=True, read_only = True)
    sessions = SessionSerializer(many=True, read_only = True)
    tests = QuizListSerializer(many=True, read_only = True)

    class Meta:
        model = models.SaveForLater
        fields = [ 'id', 'user', 'pdfs', 'mcqs', 'summaries', 'sessions', 'tests']