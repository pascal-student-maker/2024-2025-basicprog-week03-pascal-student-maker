def change_order(dict_basket:Dict[str,int],list_promotion_products: list[str]):
    
    for product in list_promotion_products:
        if product in dict_basket.keys():
           amount_ordered = dict_basket[product]    
           promotion_amount = amount_ordered *2  
           dict_basket[product]      = promotion_amount
           dict_basket[product] = promotion_amount
print("\n This is my order:") 
dict_order = {"apples":10, "pears":6, "oranges":4, "kiwies":3}     
print(dict_order)

print("\nIn promotion : apples & kiwies: amount gets doubled!") 
promotion_products = ["apples","kiwies","bananas"]
change_order(dict_order,promotion_products)
print(dict_order)    
