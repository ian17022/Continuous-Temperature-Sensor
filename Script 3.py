f = open("Results.txt","a+") # Change this to the name of the text file to write to. (Remember to change it in Script 2 too)
f.write("Temperature [C]\tTimestamp\tHeight [cm]\n")
f.close()
for i in range(8): # Change the number of times 
	exec(open('Script 1_copy.py').read())
	exec(open('Script 2.py').read())

