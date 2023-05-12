import csv
import matplotlib.pyplot as plt

def main():
    f=  open('Jeju.csv', 'r', encoding = "ANSI")
    data = csv.reader(f)
    next(data)
    row = next(data)
    female = []
    male = []
    for i in range(4,20,4):
        female.append(int(row[i]))
        male.append(int(row[i-1]))    
    f.close()

    x= list(range(2019,2023,1))
    plt.plot(x,male, label ="Male")
    plt.plot(x,female, label="Female")
    plt.xlabel("Year")
    plt.ylabel("Number of people")
    plt.legend()
    plt.title("Number of male and female in Jeju 2019~2022")
    plt.show()


if __name__ == "__main__":
    main()
