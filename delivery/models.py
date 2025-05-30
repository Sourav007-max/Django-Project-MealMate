from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=12, default=90)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}, {self.password}"

class Restaurants(models.Model):
    Res_name = models.CharField(max_length=100)
    Food_cat = models.CharField(max_length=200)
    rating = models.FloatField()
    img = models.URLField(default="https://png.pngtree.com/element_our/20190601/ourmid/pngtree-white-refresh-icon-image_1338657.jpg")
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.Res_name
    

class Menu(models.Model):
    res = models.ForeignKey(
        Restaurants,
        on_delete=models.CASCADE
    )
    item_name = models.CharField(max_length=100) # Name of the dish
    description = models.TextField(blank=True, null=True) # Short Description
    price = models.DecimalField(max_digits=6, decimal_places=2) # Price of item
    is_available = models.BooleanField(default=True) # Availability Status
    category = models.CharField(max_length=50) # Type of food 

    def __str__(self):
        return f"{self.item_name} - {self.res.Res_name}"
    
class Cart(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )   
    items = models.ManyToManyField("Menu")

    def total_price(self):
        return sum(item.price for item in self.items.all())
    
    def __str__(self):
        return f"{self.customer.username} {self.total_price()}"
