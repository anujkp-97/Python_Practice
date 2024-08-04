import csv

f = open('C:\\Users\\anuj\\Desktop\\radhe.csv', 'r')

ro = csv.reader(f, delimiter=',')
sumpercent =0
n=0
ls = list(ro)
# print(ls)
for d in ls:
    if len(d) > 0:

        sumpercent += float(d[-1])  
        n = n+1

print(f'Sum of percentage : {sumpercent}')  
print(f'Average of percent: {sumpercent/n}')  


f.close()
