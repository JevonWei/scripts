print ("--------score---------")
score = int(input("please input you score: "))
if 100 >= score >= 90:
    print ("A")
elif 90 >= score >= 80:
    print ("B")
elif 80 >= score >= 60:
    print ("C")
elif 60 >= score >= 0:
    print ("D")
else:
    print ('input error,please input again')
