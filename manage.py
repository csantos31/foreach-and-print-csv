import csv
import print_file

def main():
    input_file_path = "spreadsheet.csv"

    file_groups = list()
    with open(input_file_path, 'r') as cfr:
        csv_reader = csv.reader(cfr)
        next(csv_reader)

        for line in csv_reader:
            if len(line) != 3:
                print("Wrong number of arguments")
                exit()
            name = str(line[0])
            age = str(line[1])
            sign = str(line[2])
            file_groups.append({'name': name,
                                'age': age,
                                'sign': sign})

    #print('[%s]' % ',\n '.join(map(str, file_groups)))   
    for file in file_groups:
        print_file.print_name_age_sign(file["name"],file["age"],file["sign"])
        

if __name__ == '__main__':
    main()
