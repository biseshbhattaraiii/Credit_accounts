from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Credit, Item, UserData, Cleared
import requests
from .serializers import UserDataSerializer, CreditSerializer, ItemSerializer, UserCreditSerializer
 

TOKEN = '665426202:AAE1zzsXrjos9NO6zflZbDzA8iQZyIAIHvY'
URL = "https://api.telegram.org/bot{}/".format(TOKEN)




class ListUsers(APIView):

	def get(self ,request):
		users = UserData.objects.all()
		serializer = UserDataSerializer(users, many=True)
		return Response(serializer.data)


	def post(self, request, format=None):
		name = request.data['name']
		root = UserData()
		root.name = name
		root.save()
		return Response("Saved")




class ListItems(APIView):

	def get(self, request):
		items = Item.objects.all()
		serializer = ItemSerializer(items, many=True)
		return Response(serializer.data)


	def post(self, request, format=None):
		item_name = request.data['item_name']
		price = request.data['price']
		root = Item()
		root.item_name = item_name
		root.price = price
		root.save()
		return Response("Saved")
		



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
		item_name = request.data['item_name']
		username = request.data['username']
		for i in Item.objects.all():
			if i.item_name == item_name:
				item = i.id
				item_price = i.price
		for i in UserData.objects.all():
			if i.name == username:
				userdata = i.id
		quantity = request.data['quantity']
		paid_amt = request.data['paid_amt']
		root = Credit()
		item_  = Item.objects.get(pk=item)
		root.item = item_
		userdata_ = UserData.objects.get(pk=userdata)
		root.userdata = userdata_
		root.quantity = quantity
		root.paid_amt = paid_amt
		root.is_paid = False
		root.complete_payment = False
		total_amt = Credit.total(item_price, quantity)
		root.remaining = total_amt - int(paid_amt)
		root.total_amt = total_amt
		print(root.remaining)
		root.save()
		return Response("Saved")


class SearchUserCredits(APIView):

	def get(self, request):
		username = request.GET.get('username')
		print(username)
		users = []
		credits = []
		for user in UserData.objects.all():
			if user.name == username:
				users.append(user.id)

		if len(users) == 1:
			print(users)
			select_user = UserData.objects.get(pk=users[0])
			credits = select_user.credit_set.all()
			serializer = CreditSerializer(credits, many=True)
			return Response(serializer.data)
		elif len(users) > 1:
			for i in users:
				select_user = UserData.objects.get(pk=i)
				credits = select_user.credit_set.all()
				serializer = CreditSerializer(credits, many=True)
				return Response(serializer.data)

			

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

class PaidView(APIView):

	def post(self,request):
		id_ = request.data['id']
		paid_amt = request.data['paid_amt']
		total_amt = request.data['total_amt']
		print(type(id_), type(int(paid_amt)) , type(total_amt))
		user = UserData.objects.get(pk=id_)
		user_credit = user.credit_set.all()
		for u in user_credit:
			total_paid = u.paid_amt + int(paid_amt)
			if total_paid == total_amt:
				u.is_paid = True
				u.complete_payment = True
				root = Cleared()
				root.name = user.name
				root.paid_amt = total_paid
				root.save()
				u.delete()
			else:
				current_paid = u.paid_amt + int(paid_amt)
				remaining = total_amt - current_paid
				u.remaining = remaining
				u.paid_amt = current_paid
				u.save()
		if total_amt == total_paid:
			echo_all("Name : " + user.name + ' | ' +"Status : Cleared" + ' | ' +"Total Amt : "+ str(total_amt) + ' | ' +"Paid amt : "+str(paid_amt))

		else:
			echo_all("Name : " + user.name + ' | ' +"Status : Uncleared" + ' | ' + "Total Amt : "+ str(total_amt) + ' | ' +"Paid amt:" + str(paid_amt))

		return Response("Worked")

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