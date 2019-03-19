from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Credit, Item, UserData, Cleared, Remaining
import requests
from .serializers import UserDataSerializer, CreditSerializer, ItemSerializer, UserCreditSerializer, RemainingSerializer
 

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
		paid_all = []
		for i in Item.objects.all():
			if i.item_name == item_name:
				item = i.id
				item_price = i.price
		for i in UserData.objects.all():
			if i.name == username:
				userdata = i.id
		quantity = request.data['quantity']
		paid_amt = request.data['paid_amt']
		item = Item.objects.get(pk=item)
		current_user = UserData.objects.get(pk=userdata)
		user_credits = current_user.credit_set.all()
		_paid_amt = []
		_total_amt = []
		for i in user_credits:
			_paid_amt.append(i.paid_amt)
			_total_amt.append(i.total_amt)
		# print(_paid_amt)
		total_paid_amt = int(paid_amt) + sum(_paid_amt)
		# print(total_paid_amt)
		current_total = Credit.total(item_price, quantity)
		current_remaining = current_total - int(paid_amt)
		total_amt = current_total + sum(_total_amt)
		user_remaining_update = current_user.remaining_set.all()
		print(len(user_remaining_update))
		if len(user_remaining_update) != 0:
			for i in user_remaining_update:
				print("fjfj", i.remaining_amt_total, i.paid_amt_total)
				i.remaining_amt_total = i.remaining_amt_total + current_remaining
				i.paid_amt_total += int(paid_amt)
				i.save()
		else: 
			root = Remaining()
			root.userdata = current_user
			root.remaining_amt_total = total_amt - total_paid_amt
			root.paid_amt_total = total_paid_amt
			root.save()
		soot = Credit()
		soot.total_amt = current_total
		soot.paid_amt = int(paid_amt)
		soot.userdata = current_user
		soot.item = item
		soot.quantity = quantity
		soot.remaining_current = current_total - int(paid_amt)
		if int(paid_amt) == 0:
			soot.is_paid = False
		else:
			soot.is_paid = True
		soot.save()
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

class RemainingView(APIView):
	def get(self, request):
		username = request.GET.get('username')
		for i in UserData.objects.all():
			if i.name == username:
				user_id = i.id
		user = UserData.objects.get(pk=user_id)
		user_remaining = user.remaining_set.all()
		serializer = RemainingSerializer(user_remaining, many=True)
		return Response(serializer.data)


class UserRemainingView(APIView):
	def get(self, request, pk=None):
		user = UserData.objects.get(pk=pk)
		user_remaining = user.remaining_set.all()
		serializer = RemainingSerializer(user_remaining, many=True)
		return Response(serializer.data)


class PaidView(APIView):

	def post(self,request):
		id_ = request.data['id']
		paid_amt = request.data['paid_amt']
		total_amt = request.data['total_amt']
		print(type(id_), type(int(paid_amt)) , type(total_amt))
		user = UserData.objects.get(pk=id_)
		user_credit = user.credit_set.all()
		user_remaining = user.remaining_set.all()
		for i in user.remaining_set.all():
			i.remaining_amt_total -= int(paid_amt)
			i.paid_amt_total += int(paid_amt)
			i.save()
		for i in user.remaining_set.all():
			total_paid = i.paid_amt_total
			total_remain = i.remaining_amt_total

		if total_amt == total_paid:
			user_credit.delete()
			user_remaining.delete()
			print("All cleared")
		else:
			print("Not cleared")
		for i in user.remaining_set.all():
			remaining = i.remaining_amt_total
		if total_amt == total_paid:
			echo_all("Name : " + user.name + ' | ' +"Status : Cleared" + ' | ' +"Total Amt : "+ str(total_amt) + ' | ' +"Paid amt : "+str(total_paid))
			
		else:
			echo_all("Name : " + user.name + ' | ' +"Status : Uncleared" + ' | ' + "Total Amt : "+ str(total_amt) + ' | ' +"Paid amt:" + str(total_paid) + ' | ' + "Remaining : " + str(remaining))

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