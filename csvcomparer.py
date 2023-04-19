import csv

def count_diff_values(file_name, row1, row2):
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        # convert csv file to a list of rows
        rows = list(csv_reader)

        # get the first and second row
        first_row = rows[row1-1]
        second_row = rows[row2-1]

        # use a set to store the unique values in each row
        first_row_set = set(first_row)
        second_row_set = set(second_row)

        # get the number of unique values in both rows
        diff_values = len(first_row_set.union(second_row_set))

        return diff_values

file_name = 'example.csv'
row1 = 1
row2 = 2
diff_count = count_diff_values(file_name, row1, row2)
print("Hay un total de ", diff_count, "incongruencias en la base de datos")
