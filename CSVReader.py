from HashTable import HashMap
import csv

with open('./Michael_CSV_files/Michael_WGUPS Package_File.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    hash_map = HashMap()  # create an hashmap object
    Delivery1 = []  # 1st truck delivery list
    Delivery2 = []  # 2nd truck delivery list
    Delivery3 = []  # 3rd truck delivery list

    # reads values from csv and loads them into key/value pairs of the hashmap
    for rows in csv_reader:
        id = rows[0]
        address = rows[1]
        city = rows[2]
        state = rows[3]
        zipcode = rows[4]
        delivery = rows[5]
        size = rows[6]
        note = rows[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'

        value = [id, address_location, address, city, state, zipcode, delivery, size, note, delivery_start,
                 delivery_status]

        key = id
        value_list = value

        if value_list[6] != 'EOD':
            if 'Must' in value_list[8] or 'None' in value_list[8]:
                Delivery1.append(value_list)

        if 'Can ony be' in value_list[8]:
            Delivery2.append(value_list)

        if 'Delayed' in value_list[8]:
            Delivery2.append(value_list)

        # change wrong address to right address

        if '84104' in value_list[5] and '10:30' not in value_list[6]:
            Delivery3.append(value_list)

        if 'Wrong address listed' in value_list[8]:
            value_list[2] = '410 S State St'
            value_list[5] = '84111'
            Delivery3.append(value_list)

        if value_list not in Delivery1 and value_list not in Delivery2 and value_list not in Delivery3:
            if len(Delivery2) > len(Delivery1):
                Delivery3.append(value_list)
            else:
                Delivery2.append(value_list)

        hash_map.insert(key, value_list)  # adds values in csvs to hash table


    # functions used to grab packages that are loaded into the trucks for Truck1, 2 and 3
    def delivery1():
        return Delivery1


    def delivery2():
        return Delivery2


    def delivery3():
        return Delivery3


    def display_map():
        return hash_map
