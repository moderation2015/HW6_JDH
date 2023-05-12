import csv
import matplotlib.pyplot as plt
import random

def main():
    f = open('result.csv','w')
    for i in range(0,100,1):
        num = random.randint(1,6)
        f.write(str(num))
        f.write(',')
    f.write('\n')

    for i in range(0,1000,1):
        num = random.randint(1,6)
        f.write(str(num))
        f.write(',')
    f.write('\n')

    for i in range(0,10000,1):
        num = random.randint(1,6)
        f.write(str(num))
        f.write(',')
    f.write('\n')

    for i in range(0,100000,1):
        num = random.randint(1,6)
        f.write(str(num))
        f.write(',')
    f.write('\n')
    f.close()

    f = open('result.csv', 'r' , encoding = "ANSI")
    histo = []
    data = csv.reader(f)
    row = next(data)
    for i in range(0,100,1):
        histo.append(int(row[i]))
    plt.subplot(2,2,1)
    plt.title("100 Dice")
    plt.hist(histo, bins =20)

    data = csv.reader(f)
    row = next(data)
    for i in range(0,1000,1):
        histo.append(int(row[i]))
    plt.subplot(2,2,2)
    plt.title("1000 Dice")
    plt.hist(histo, bins =20)
    

    data = csv.reader(f)
    row = next(data)
    for i in range(0,10000,1):
        histo.append(int(row[i]))
    plt.subplot(2,2,3)
    plt.title("10000 Dice")
    plt.hist(histo, bins =20)
    
    data = csv.reader(f)
    row = next(data)
    for i in range(0,100000,1):
        histo.append(int(row[i]))
    plt.subplot(2,2,4)
    plt.title("100000 Dice")
    plt.hist(histo, bins =20)

    plt.show()
    f.close()

if __name__ == "__main__":
    main()
