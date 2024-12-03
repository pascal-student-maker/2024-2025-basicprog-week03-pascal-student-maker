#exercise10c

int(input("Specify the number of products you wish to enter:>"))
print(input(" What is the category? [V:Vegetable,F:fruit,B:Beverage]>"))
float(input("What is the cost price of the product:>"))

def give_ticket_by_category_vegetable(vegetable: str, sum_of_prices: float, number_of_products: int,average_prices:float) -> str:
    # Example logic: Generate a "ticket" with information
    ticket = (
        f"Category: {vegetable}\n"
        f"Total Price: ${sum_of_prices:.2f}\n"
        f"Number of Products: {number_of_products}"
        f"Average Prices: {average_prices}"
    )
    return ticket

# Example usage:
result = give_ticket_by_category_vegetable("Vegetables", 21.3, 2,10.6)
print(result)


def give_ticket_by_category_fruit(fruit: str, sum_of_prices: float, number_of_products: int,average_prices:float) -> str:
    # Example logic: Generate a "ticket" with information
    ticket = (
        f"Category: {fruit}\n"
        f"Total Price: ${sum_of_prices:.2f}\n"
        f"Number of Products: {number_of_products}"
        f"Average Prices: {average_prices}"

        
    )
    return ticket

# Example usage:
result = give_ticket_by_category_fruit("Fruit", 4.00, 1,4.0)
print(result)

def give_ticket_by_category_beverages(beverages: str, sum_of_prices: float, number_of_products: int,average_prices:float) -> str:
    # Example logic: Generate a "ticket" with information
    ticket = (
        f"Category: {beverages}\n"
        f"Total Price: ${sum_of_prices:.2f}\n"
        f"Number of Products: {number_of_products}"
        f"Average Prices: {average_prices}"

    )
    return ticket

# Example usage:
result = give_ticket_by_category_beverages("Beverages", 30.00, 2,15.0)
print(result)


  





                           

