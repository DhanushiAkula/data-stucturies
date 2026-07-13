basket1={"apple","banana","mango","apple","grape"}
basket2={"apple","kiwi","banana","kiwi"}
print("basket1:",basket1)
print("basket2:",basket2)
basket1.add("orange")
print("basket1 after adding orange:",basket1)
common_fruits=basket1.intersection(basket2)
print("fruits in the both baskets:",common_fruits)

import array as arr
fruit_count=arr.array("i",[3,5,2,4])
print("fruit counts array:",fruit_count)
fruit_count.insert(0,1)
fruit_count.append(6)
count_of_4=fruit_count.count(4)
print("number of times4 appears:",count_of_4)
fruit_count.reverse()
print("")
print("===== CLASS FRUIT BASKET ORGANIZER =====")
print("basket1:",basket1)
print("basket2:",basket2)
print("shared fruits:",common_fruits)
print("================================")
