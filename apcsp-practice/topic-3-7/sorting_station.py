label = input("Input label: ") #BALLRED0120050N

shape = label[0:4]
color = label[4:7]
size = int(label[7:10])
weight = int(label[10:14])
condition = label[14]

if condition == "D" or size > 50 or weight > 2000: 
    print(label, "Sent to INSPECT group")

elif color == "RED" and shape == "BALL" and size >= 10:
    print(label, "Sent to group B")

elif shape == "BALL":
    print(label, "Sent to group A")

elif shape == "CUBE" and (color == "BLU" or color == "GRN") and size > 10:
    print(label, "Sent to group C")

elif shape == "CUBE":
    print(label, "Sent to group D")

else:
    print(label, "Sent to group E")