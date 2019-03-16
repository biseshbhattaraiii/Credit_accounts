from django.db import models

class UserData(models.Model):
	name = models.CharField(max_length=23)

	def __str__ (self):
		return self.name

class Item(models.Model):
	item_name = models.CharField(max_length=244)
	price = models.IntegerField(default=0)


	def __str__ (self):
		return self.item_name

class Credit(models.Model):
	userdata = models.ForeignKey(UserData, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	is_paid = models.BooleanField(default=False)
	given_date = models.DateTimeField(auto_now_add=True)
	paid_date  = models.DateTimeField(auto_now=True)
	paid_amt = models.IntegerField(default=0)
	complete_payment = models.BooleanField(default=False)

	def __str__(self):
		return self.userdata.name

	def check_complete_payment(quantity , paid ,price, amount_paid):
		total_amt = quantity * price
		if paid == True:
			if total_amt == amount_paid:
				return True
			elif total_amt > amount_paid:
				return False







