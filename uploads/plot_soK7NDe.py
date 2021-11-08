import matplotlib.pyplot as plt

f = open("tcp-example.tr", "r")
t=[]
w=[]

start=[]
end=0
for x in f:
	tokens=x.split(" ")
	tokens2 = tokens[2].split("/")

	
	if not tokens2[2]=="0":
		continue;
	if(x[0]=='+'):
		start.append(float(tokens[1]))
	elif(x[0]=='-'):
		end=float(tokens[1])
		t.append(end)
		w.append(end-start.pop(0))

#print(t)
#print(w)

plt.plot(t,w)
plt.title('t vs w')
plt.xlabel('t')
plt.ylabel('w')
plt.grid()
plt.show()