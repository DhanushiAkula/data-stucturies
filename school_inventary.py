items=["pencil","eraser","notebook","sharpener","glue"]
stock_count=[12,0,8,5,3]
inventory={items:count for items,count in zip(items,stock_count)}
print("full inventory:",inventory)
in_stock_items=[items for items in items if inventory[items]>0]
print("items in stock:",in_stock_items)
chosen_items=input("which items do you want to buy?")
if chosen_items not in inventory or inventory[chosen_items]==0:
    print(chosen_items,"is out of stock! stopping tge checker.")
    exit()
prices=[10,5,40,15,20]
markup =int(input("enter the markup amount to add to every price:"))
marked_up_prices=list(map(lambda p:p+markup,prices))
print("marked up prices:",marked_up_prices)
item_index=items.index(chosen_items)
chosen_price=marked_up_prices[item_index]
print("print of",chosen_items,"after markup:",inventory[chosen_items])
inventory[chosen_items]=inventory[chosen_items]-1
print(chosen_items,"purchased!remaining stock:",inventory[chosen_items])
print("")
print("==== SCHOOL STORE INVENTORY CHECKER====")
print("ITEMS BOUGHT:",chosen_items)
print("price paid:",chosen_items)
print("updated inventory:",inventory)
print("=============================")