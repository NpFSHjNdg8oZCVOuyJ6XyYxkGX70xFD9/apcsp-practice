label = input("Input label: ") #BALLRED0120050N

shape = label[0:4]
color = label[4:7]
size = int(label[7:10])
weight = int(label[10:14])
condition = label[14]

if condition == "D" or size >= 050 or weight >= 2000: 
    print(label, "Sent to INSPECT group")