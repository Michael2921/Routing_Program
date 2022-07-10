import TruckDistance
import CSVReader

Delivery1 = []
Delivery2 = []
Delivery3 = []

Truck1_Distance = []
Truck2_Distance = []
Truck3_Distance = []

# times that Truck1, 2 and 3 leave the hub
FirstTime = ['8:00:00']
SecondTime = ['9:10:10']
ThirdTime = ['11:00:00']

# sets delivery start to first leave time for Truck1's packages
for index, result in enumerate(CSVReader.delivery1()):
    CSVReader.delivery1()[index][9] = FirstTime[0]
    Delivery1.append(CSVReader.delivery1()[index])

# compare truck1 address to address list
for index, outer in enumerate(Delivery1):
    for inner in TruckDistance.get_location_address():
        if outer[2] == inner[2]:
            Truck1_Distance.append(outer[0])
            Delivery1[index][1] = inner[0]

# sort packages for Truck1
TruckDistance.find_quickest_route(Delivery1, 1, 0)
SumDistance1 = 0

# finds distance of Truck1 and distance of each package
for index in range(len(TruckDistance.truck1_index())):
    try:
        SumDistance1 = TruckDistance.calculate_distance(int(TruckDistance.truck1_index()[index]),
                                                        int(TruckDistance.truck1_index()[index + 1]), SumDistance1)

        deliver_package = TruckDistance.calculate_time(
            TruckDistance.calculate_current_distance(int(TruckDistance.truck1_index()[index]),
                                                     int(TruckDistance.truck1_index()[index + 1])), FirstTime)
        TruckDistance.truck1_list()[index][10] = (str(deliver_package))
        CSVReader.display_map().insert(int(TruckDistance.truck1_list()[index][0]), Delivery1)
    except IndexError:
        pass

# sets delivery start to second leave time for Truck2's packages

for index, result in enumerate(CSVReader.delivery2()):
    CSVReader.delivery2()[index][9] = SecondTime[0]
    Delivery2.append(CSVReader.delivery2()[index])

# compares Truck2 addresses to address list

for index, outer in enumerate(Delivery2):
    for inner in TruckDistance.get_location_address():
        if outer[2] == inner[2]:
            Truck2_Distance.append(outer[0])
            Delivery2[index][1] = inner[0]

# sort packages for second truck
TruckDistance.find_quickest_route(Delivery2, 2, 0)
SumDistance2 = 0

# finds total distance of Truck2 and distance of each package
for index in range(len(TruckDistance.truck2_index())):
    try:
        SumDistance2 = TruckDistance.calculate_distance(int(TruckDistance.truck2_index()[index]),
                                                        int(TruckDistance.truck2_index()[index + 1]), SumDistance2)

        deliver_package = TruckDistance.calculate_time(
            TruckDistance.calculate_current_distance(int(TruckDistance.truck2_index()[index]),
                                                     int(TruckDistance.truck2_index()[index + 1])), FirstTime)
        TruckDistance.truck2_list()[index][10] = (str(deliver_package))
        CSVReader.display_map().insert(int(TruckDistance.truck2_list()[index][0]), Delivery2)
    except IndexError:
        pass

# sets delivery start to third leave time for Truck3's packages

for index, result in enumerate(CSVReader.delivery3()):
    CSVReader.delivery3()[index][9] = ThirdTime[0]
    Delivery3.append(CSVReader.delivery3()[index])

# compares Truck2 addresses to address list

for index, outer in enumerate(Delivery3):
    for inner in TruckDistance.get_location_address():
        if outer[2] == inner[2]:
            Truck3_Distance.append(outer[0])
            Delivery3[index][1] = inner[0]

TruckDistance.find_quickest_route(Delivery3, 3, 0)
SumDistance3 = 0

# sort packages for second truck

for index in range(len(TruckDistance.truck3_index())):
    try:
        SumDistance3 = TruckDistance.calculate_distance(int(TruckDistance.truck3_index()[index]),
                                                        int(TruckDistance.truck3_index()[index + 1]), SumDistance3)

        deliver_package = TruckDistance.calculate_time(
            TruckDistance.calculate_current_distance(int(TruckDistance.truck3_index()[index]),
                                                     int(TruckDistance.truck3_index()[index + 1])), ThirdTime)
        TruckDistance.truck3_list()[index][10] = (str(deliver_package))
        CSVReader.display_map().insert(int(TruckDistance.truck3_list()[index][0]), Delivery3)
    except IndexError:
        pass


# calculates distance of all packages
def overall_distance():
    return SumDistance1 + SumDistance2 + SumDistance3
