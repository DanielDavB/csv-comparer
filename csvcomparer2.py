import csv

def compare_csv(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        csv1 = csv.reader(f1)
        csv2 = csv.reader(f2)
        for row1, row2 in zip(csv1, csv2):
            if row1 != row2:
                return False
    return True

if __name__ == '__main__':
    file1 = 'file1.csv'
    file2 = 'file2.csv'
    if compare_csv(file1, file2):
        print("The two csv files are identical.")
    else:
        print("The two csv files are different.")
