from rest_framework import serializers
from .models import UserData, Item , Credit

class CreditSerializer(serializers.ModelSerializer):
	class Meta:
		model = Credit
		fields = ('id', 'userdata', 'item', 'is_paid', 'given_date', 'paid_date', 'paid_amt', 'complete_payment')

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields= ('id','item_name', 'price')

class UserDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserData
		fields = ('id','name')


