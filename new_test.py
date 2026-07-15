dict={"aliya":45,"dhanushi":56,"sonali":58,"manya":48,"lakshana":58}
sum=0
for score in dict.values():
    sum=+score
average=sum/len(dict)
print("average:",average)
print("max score:",max(dict.values()))
print("min score:",min(dict.values()))
name= input(dict)
print("============================")