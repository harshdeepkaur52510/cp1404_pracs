"""
CP1404
program -> subject_reader
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_data(data)


def get_data():
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)
        print(repr(line))
        line = line.strip()
        parts = line.split(',')
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        data.append(parts)
    input_file.close()
    return data


def display_data(data):
    for data in data:
        print("{} is taught by {:12} and has {:3} students".format(*data))


# print all items for each list in the lists of lists

main()
