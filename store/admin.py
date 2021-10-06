from django.contrib import admin
from store.models import *
# Register your models here.

# method - 1] StackedInline --> Size varients for each Tshirt
# method- 2]  TabularInline --> Size varients for each Tshirt

class SizeVarientConfiguration(admin.TabularInline):
    model = SizeVarient

class TshirtConfiguration(admin.ModelAdmin):
    inlines = [SizeVarientConfiguration]

class CartConfiguration(admin.ModelAdmin):
    model = Cart
    
    list_display = ['quantity' , 'size' , 'tshirt' , 'user' , 'username']

    def size(self , obj):
        return obj.sizeVarient.size
    
    def tshirt(self , obj):
        return obj.sizeVarient.tshirt.name 
    
    def username(self , obj):
        return obj.user.first_name

admin.site.register(Tshirt,TshirtConfiguration )
admin.site.register(Occasion)
admin.site.register(IdealFor)
admin.site.register(NeckType)
admin.site.register(Sleeve)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Cart,CartConfiguration)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)


# admin.site.register(SizeVarient)


