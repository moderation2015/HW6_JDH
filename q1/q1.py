import csv
import matplotlib.pyplot as plt

def main():
    x = list(range(1,13,1))
 
    f= open('전국.csv', 'r', encoding = 'ANSI')
    data = csv.reader(f)
    next(data)
    y= []
    for row in data:
        row[2] = float(row[2])
        y.append(row[2])
    plt.plot(x,y,label = 'Nationwide')
    f.close()

    f= open('대전.csv', 'r', encoding = 'ANSI')
    data = csv.reader(f)
    next(data)
    y= []
    for row in data:
        row[2] = float(row[2])
        y.append(row[2])
    plt.plot(x,y,label = 'Daejeon')
    f.close()

    f= open('서울.csv', 'r', encoding = 'ANSI')
    data = csv.reader(f)
    next(data)
    y= []
    for row in data:
        row[2] = float(row[2])
        y.append(row[2])
    plt.plot(x,y,label = 'Seoul')
    f.close()

    f= open('부산.csv', 'r', encoding = 'ANSI')
    data = csv.reader(f)
    next(data)
    y= []
    for row in data:
        row[2] = float(row[2])
        y.append(row[2])
    plt.plot(x,y,label = 'Busan')
    f.close()

    f= open('제주.csv', 'r', encoding = 'ANSI')
    data = csv.reader(f)
    next(data)
    y= []
    for row in data:
        row[2] = float(row[2])
        y.append(row[2])
    plt.plot(x,y,label = 'Jeju')
    f.close()

    plt.title('2022 Average month temperature difference')
    plt.xlabel('Month')
    plt.ylabel('Celsius')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
