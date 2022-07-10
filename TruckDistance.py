import csv
import datetime

# Read CSV files
with open('./Michael_CSV_files/Michael_WGUPS Distance_Table.csv') as first_csv:
    distance_table_csv = list(csv.reader(first_csv, delimiter=','))

with open('./Michael_CSV_files/Michael_WGUPS Location_Address.csv') as second_csv:
    location_address_csv = list(csv.reader(second_csv, delimiter=','))


 # get package address

    def get_location_address():
        return location_address_csv


    # calculates total distance from rows and columns
    # time complexity of O(1)
    def calculate_distance(row, column, sum):
        distance_total = distance_table_csv[row][column]
        if distance_total == '':
            distance_total = distance_table_csv[column][row]
        return sum + float(distance_total)


    # calculates current distance from rows and columns
    # time complexity of O(1)

    def calculate_current_distance(row, column):
        distance_current = distance_table_csv[row][column]
        if distance_current == '':
            distance_current = distance_table_csv[column][row]
        return float(distance_current)


    # calculate distance for a truck
    def calculate_time(truck_distance, truck_list):
        new_time = truck_distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        truck_list.append(final_time)
        sum = datetime.timedelta()
        for i in truck_list:
            (hours, minutes, seconds) = i.split(':')  # check if code fails
            sum += datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
        return sum

# sorted trucks list
    Truck1 = []
    Truck1_index = []
    Truck2 = []
    Truck2_index = []
    Truck3 = []
    Truck3_index = []


    # greedy algorithm to find shortest distance
    def find_quickest_route(lists, number, current_location):
        if not len(lists):
            return lists

        lowest_value = 50.0
        location = 0

        for i in lists:
            result = int(i[1])
            if calculate_current_distance(current_location, result) <= lowest_value:
                lowest_value = calculate_current_distance(current_location, result)
                location = result

        for i in lists:
            if calculate_current_distance(current_location, int(i[1])) == lowest_value:
                if number == 1:
                    Truck1.append(i)
                    Truck1_index.append(i[1])
                    lists.pop(lists.index(i))
                    current_location = location
                    find_quickest_route(lists, 1, current_location)

                elif number == 2:
                    Truck2.append(i)
                    Truck2_index.append(i[1])
                    lists.pop(lists.index(i))
                    current_location = location
                    find_quickest_route(lists, 2, current_location)

                elif number == 3:
                    Truck3.append(i)
                    Truck3_index.append(i[1])
                    lists.pop(lists.index(i))
                    current_location = location
                    find_quickest_route(lists, 3, current_location)


    Truck1_index.insert(0, '0')
    Truck2_index.insert(0, '0')
    Truck3_index.insert(0, '0')


    def truck1_index():
        return Truck1_index


    def truck1_list():
        return Truck1


    def truck2_index():
        return Truck2_index


    def truck2_list():
        return Truck2


    def truck3_index():
        return Truck3_index


    def truck3_list():
        return Truck3
