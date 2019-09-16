def avg(name,*grades):
    if len(grades)>0:
        av=sum(grades)/len(grades)
        print(name,", your average grade is: ",av)


avg("Hovo")