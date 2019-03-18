from rest_framework import serializers
from .models import UserData, Item , Credit

class CreditSerializer(serializers.ModelSerializer):
	name = serializers.CharField(source='userdata.name', read_only=True)
	item_name = serializers.CharField(source='item.item_name', read_only=True)
	price = serializers.IntegerField(source='item.price', read_only=True)
	class Meta:
		model = Credit
		fields = ('id', 'userdata', 'item', 'item_name', 'quantity', 'total_amt' ,'name','price' ,'remaining','is_paid', 'given_date', 'paid_date', 'paid_amt', 'complete_payment')

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields= ('id','item_name', 'price')

class UserDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserData
		fields = ('id','name')


class UserCreditSerializer(serializers.Serializer):
	userdata = UserDataSerializer()
	item = ItemSerializer()
	is_paid = serializers.BooleanField(default=False)
	given_date = serializers.DateTimeField()
	paid_date  = serializers.DateTimeField()
	paid_amt = serializers.IntegerField(default=0)
	complete_payment = serializers.BooleanField(default=False)
	item_name = serializers.CharField(max_length=244)
	price = serializers.IntegerField(default=0)