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
	quantity = models.IntegerField(default=0)
	remaining_current = models.IntegerField(default=0)
	total_amt = models.IntegerField(default=0)

	def __str__(self):
		return self.userdata.name

	def check_complete_payment(total_amt, amount_paid):
	
		if total_amt == int(amount_paid):
			return True
		elif total_amt > int(amount_paid):
			return False

	def total(price, quantity):
		return int(price) * int(quantity)



class Cleared(models.Model):
	name = models.CharField(max_length=200)
	paid_amt = models.IntegerField(default=0)

	def __str__ (self):
		return self.name


class Remaining(models.Model):
	userdata = models.ForeignKey(UserData, on_delete=models.CASCADE)
	remaining_amt_total = models.IntegerField(default=0)
	paid_amt_total = models.IntegerField(default=0)

	def __str__(self):
		return self.userdata.name





