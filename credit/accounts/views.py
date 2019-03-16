from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Credit, Item, UserData
import requests
from .serializers import UserDataSerializer, CreditSerializer, ItemSerializer
 

TOKEN = '665426202:AAE1zzsXrjos9NO6zflZbDzA8iQZyIAIHvY'
URL = "https://api.telegram.org/bot{}/".format(TOKEN)




class ListUsers(APIView):

	def get(self ,request):
		users = UserData.objects.all()
		serializer = UserDataSerializer(users, many=True)
		return Response(serializer.data)


	def post(self, request, format=None):

		serializer = UserDataSerializer(data=request.data)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ListItems(APIView):

	def get(self, request):
		items = Item.objects.all()
		serializer = ItemSerializer(items, many=True)
		return Response(serializer.data)


	def post(self, request, format=None):
		serializer = ItemSerializer(data=request.data)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		



class getUserCredit(APIView):

	def get(self, request, pk=None):
		user = UserData.objects.get(pk=pk)
		user_credit = user.credit_set.all()
		serializer = CreditSerializer(user_credit, many=True)
		return Response(serializer.data)



class getItemCredit(APIView):
	def get(self, request, pk=None):
		item = Item.objects.get(pk=pk)
		item_credit = item.credit_set.all()
		serializer = CreditSerializer(item_credit, many=True)
		return Response(serializer.data)


class ListCredit(APIView):

	def get(self, request):
		credits = Credit.objects.all()
		serializer = CreditSerializer(credits, many=True)
		return Response(serializer.data)


	def post(self, request, format=None):
		serializer = CreditSerializer(data=request.data)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def list_users(request):
	users = UserData.objects.all()
	items = Item.objects.all()
	return render(request, 'accounts/index.html', {'users':users, 'items':items})




def list_user_credit(request, pk=None):
	user = UserData.objects.get(pk=pk)
	user_credit = []
	for i in user.credit_set.all():
		user_credit.append(i)
	return render(request, 'accounts/detail.html', {'user_credit':user_credit})

def list_item_credit(request , pk=None):
	item = Item.objects.get(pk=pk)
	item_credit = item.credit_set.all()
	return render(request, 'accounts/item_detail.html',{'item_credit':item_credit})


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content



def send(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def echo_all(message):
        try:
        	send(message, 639871483)
        	print("hhjj")
        except Exception as e:
            print(e ,"This is the error")

def paid(request, pk=None):
	user = UserData.objects.get(pk=pk)
	item_credit = user.credit_set.all()
	for i in item_credit:
		if i.is_paid == False:
			i.is_paid = True
			if Credit.check_complete_payment(2 , True, 10, 20):
				i.complete_payment = True
				i.delete()
				echo_all("Thank you for paying your debt")
			else:
				i.save()
				echo_all("Please pay complete money within 7 days")
			return redirect('/items')
		else:
			return redirect('/items')
	return render(request , 'accounts/index.html')