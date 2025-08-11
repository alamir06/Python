food_items=input("Please enter your food item?:")
# def get_food_items(food_items):
#     if food_items == "pizza":  
#         print("The price of pizza is $10")
#     elif food_items == "burger":
#         print("The price of burger is $5")  
#     elif food_items == "pasta":
#         print("The price of pasta is $7")
#     elif food_items == "salad":
#         print("The price of salad is $4")   
#     else:
#         print("The food item is not available")     

# get_food_items(food_items)

# instead of using a function, we can use a dictionary to map food items to their prices
food_prices = {
    "pizza": 200,
    "burger": 150,
    "pasta": 120,
    "salad": 400
}
def get_food_items(food_items):
    return food_prices.get(food_items,0)

# Call the function and print the result
print(get_food_items(food_items))