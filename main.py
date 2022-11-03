# David S, Alejandro M

coffee_prices =[('cappucino', 1.5,),
               ('expresso',1.2),
               ('mocha',1.9)]

#problem #1 retrieve the coffee names and price from the above tuple. Make sure it is in a readable format(hint: f strings)
#Mr Evins example:
#for coffee, price in coffee_prices:
#  print(f"coffee : {coffee} and {prices} ")

# 

print(f" Coffee name: {coffee_prices[0][0]} price: {coffee_prices[0][1]}")
print(f" Coffee name: {coffee_prices[1][0]} price: {coffee_prices[1][1]}")
print(f" Coffee name: {coffee_prices[2][0]} price: {coffee_prices[2][1]}")

#create a function that iterates through the tuple list above and returns the highest priced coffee only. You probably want to create a function that has arguments  
from coffee import coffee

highest_coffee=coffee(coffee_prices)
print(highest_coffee)

def most_expensive_coffee(coffee_prices):
  #establish what the highest prices are
  #my most expensive coffee
  highest_price = 0
  my_most_expensive_coffee = ""
  
  for coffee, price in coffee_prices:
    if price > highest_price:
      highest_price = price
      my_most_expensive_coffee = coffee
    else:
      pass
  return(my_most_expensive_coffee, highest_price)

print(most_expensive_coffee(coffee_prices))