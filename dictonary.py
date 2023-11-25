#DICTONARY represented using {} ,but contain values in kay(pair of values)
# ordered and mutable
# duplicates not allowed
#clear,copy,get,po,popitems

dict={"brand":"BMW","model":"M3 series","cost":"8500000"}
print(dict)

x=dict["model"]
print(x)

y=dict["cost"]
print(y)

dict["color"]="Matte Black"
print(dict)

dict["cost"]="9000000"
print(dict)

dict["propeller"]="Hydraulic ENs"
print(dict)

dict.pop("propeller")
print(dict)

dict["height"]="1.2"
print(dict)

dict.clear()


