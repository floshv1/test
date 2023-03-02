l= [i for i in range(1,11)]
#l=[i for i in range(300) if i % 2 == 1 ]
#n=[i for i in range(1,300,2)]
#m=[i if i%2==1 else None for i in range(300)]
nb = ["one","two","three","four","five","six","seven", "eight", "nine","ten"]

dict = dict(zip(l,nb))
dict2={l[i] : nb[i] for i in range(len(l))}
print(dict2)

