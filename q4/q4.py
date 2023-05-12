import csv
import matplotlib.pyplot as plt

def main():    
    f = open('traffic.csv', 'r', encoding = "ANSI")
    data = csv.reader(f)
    next(data)
    next(data)
    dic = []
    for row in data:
        dic.append((row[3],int(row[10])+int(row[12])))
    f.close()
    dic.sort(key = lambda x:x[1])
    l = len(dic)
    x=[]
    y=[]
    for i in range(l-30,l,1):
        x.append(dic[i][0])
        y.append(dic[i][1])
    plt.rc('font',family = 'Malgun Gothic', size =7)
    plt.rcParams['axes.unicode_minus'] = False
    ax = plt.subplot(3,1,1)
    ax.set_xticks(range(30))
    ax.set_xticklabels(x, rotation= 10)
    plt.title("Maximum getting on 30 stations")
    plt.ylabel("Number of passenger")
    plt.xlabel("Name of Station")
    plt.bar(range(30),y)
    
    f = open('traffic.csv', 'r', encoding = "ANSI")
    data = csv.reader(f)
    next(data)
    next(data)
    dic = []
    for row in data:
        dic.append((row[3],int(row[11])+int(row[13])))
    f.close()
    dic.sort(key = lambda x:x[1])
    l = len(dic)
    x=[]
    y=[]
    for i in range(l-30,l,1):
        x.append(dic[i][0])
        y.append(dic[i][1])
    ax =plt.subplot(3,1,2)
    ax.set_xticks(range(30))
    ax.set_xticklabels(x, rotation= 10)
    plt.title("Maximum getting off 30 stations")
    plt.ylabel("Number of passenger")
    plt.xlabel("Name of Station")
    plt.bar(range(30),y)
    
    f = open('traffic.csv', 'r', encoding = "ANSI")
    data = csv.reader(f)
    next(data)
    next(data)
    dic = []
    for row in data:
        dic.append((row[3],int(row[10])+int(row[12])+ int(row[11])+int(row[13])))
    f.close()
    dic.sort(key = lambda x:x[1])
    l = len(dic)
    x=[]
    y=[]
    for i in range(l-30,l,1):
        x.append(dic[i][0])
        y.append(dic[i][1])
    ax = plt.subplot(3,1,3)
    ax.set_xticks(range(30))
    ax.set_xticklabels(x, rotation= 10)
    plt.title("Maximum getting on and getting off 30 stations")
    plt.ylabel("Number of passenger")
    plt.xlabel("Name of Station")
    plt.bar(range(30),y)

    plt.show()
if __name__ == "__main__":
    main()
