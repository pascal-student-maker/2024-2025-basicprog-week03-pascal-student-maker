# Initialize counters and sums
count_vegetables = 0
count_fruits = 0
count_beverages = 0
sum_of_vegetables = 0
sum_of_fruits = 0
sum_of_beverages = 0

def give_ticket_by_category(category_name, cost_price):
    global count_vegetables, count_fruits, count_beverages
    global sum_of_vegetables, sum_of_fruits, sum_of_beverages

    if category_name == "V":
        count_vegetables += 1
        sum_of_vegetables += cost_price
    elif category_name == "B":
        count_beverages += 1
        sum_of_beverages += cost_price    
    elif category_name == "F":
        count_fruits += 1
        sum_of_fruits += cost_price
    else:
        print("Invalid category. Please enter V, F, or B.")

# Input for the number of products
number_of_products = int(input("Specify the number of products you wish to enter: "))

for _ in range(number_of_products):
    category_name = input("What is the category? [V: Vegetable, F: Fruit, B: Beverage]: ").upper()
    cost_price = float(input("What is the cost of the product: "))
    give_ticket_by_category(category_name, cost_price)

# Print results with checks to avoid division by zero
if count_beverages > 0:
    print(f"{count_beverages} are in the category beverages\nTotal cost: {sum_of_beverages:.2f}\nAverage price: {sum_of_beverages / count_beverages:.2f}")
else:
    print("No beverages entered.")

if count_fruits > 0:
    print(f"{count_fruits} are in the category fruits\nTotal cost: {sum_of_fruits:.2f}\nAverage price: {sum_of_fruits / count_fruits:.2f}")
else:
    print("No fruits entered.")

if count_vegetables > 0:
    print(f"{count_vegetables} are in the category vegetables\nTotal cost: {sum_of_vegetables:.2f}\nAverage price: {sum_of_vegetables / count_vegetables:.2f}")
else:
    print("No vegetables entered.")
