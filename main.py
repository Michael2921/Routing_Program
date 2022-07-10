import datetime
from CSVReader import display_map
import Packages


# Michael Samuel
# 009458036

class Main:
    # Beginning of interface
    print('WGUPS PACKAGE TRACKING PROGRAM')
    print('\n')
    print('Current Route was completed in', "{0:.2f}".format(Packages.overall_distance(), 2), 'miles. ')
    options = input("""
    Please type 'search' to find package info by package ID, or type 'times' to display all package info based on time given.
    Type 'close' to exit the WGUPS package tracking program:
     """)
    # time complexity of O(N)
    while options != 'close':
        # if 'times is entered', user is prompted for a time and all package info at or close to that time are displayed
        if options == 'times':
            try:
                given_time = input('Please enter the time in the format (HH::MM:SS) i.e 11:59:59 ')
                (hrs, mins, secs) = given_time.split(':')
                change_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                # time complexity of O(n^2)
                for count in range(1, 41):
                    try:
                        Time1 = display_map().get(str(count))[9]
                        Time2 = display_map().get(str(count))[10]
                        (hrs, mins, secs) = Time1.split(':')
                        change_time1 = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                        (hrs, mins, secs) = Time2.split(':')
                        change_time2 = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                    except ValueError:
                        pass

                    # compares all package to time to determine if they have left the hub
                    if change_time1 >= change_time:
                        display_map().get(str(count))[10] = 'At Hub'
                        display_map().get(str(count))[9] = 'Leaves at ' + Time1

                        print('Package ID:', display_map().get(str(count))[0], '   Street address:',
                              display_map().get(str(count))[2], display_map().get(str(count))[3],
                              display_map().get(str(count))[4], display_map().get(str(count))[5],
                              '  Required delivery time:', display_map().get(str(count))[6],
                              ' Package weight:', display_map().get(str(count))[7], '  Truck status:',
                              display_map().get(str(count))[9], '  Delivery status:',
                              display_map().get(str(count))[10])

                        # global again below
                    elif change_time1 <= change_time:
                        if change_time < change_time2:
                            display_map().get(str(count))[10] = 'In transit'
                            display_map().get(str(count))[9] = 'Left at ' + Time1
                            print('Package ID:', display_map().get(str(count))[0], '   Street address:',
                                  display_map().get(str(count))[2], display_map().get(str(count))[3],
                                  display_map().get(str(count))[4], display_map().get(str(count))[5],
                                  '  Required delivery time:', display_map().get(str(count))[6],
                                  ' Package weight:', display_map().get(str(count))[7], '  Truck status:',
                                  display_map().get(str(count))[9], '  Delivery status:',
                                  display_map().get(str(count))[10])

                        # goes through packages that have been delivered and outputs time it was delivered
                        else:
                            display_map().get(str(count))[10] = 'Delivered at ' + Time2
                            display_map().get(str(count))[9] = 'Left at ' + Time1
                            print('Package ID:', display_map().get(str(count))[0], '   Street address:',
                                  display_map().get(str(count))[2], display_map().get(str(count))[3],
                                  display_map().get(str(count))[4], display_map().get(str(count))[5],
                                  '  Required delivery time:', display_map().get(str(count))[6],
                                  ' Package weight:', display_map().get(str(count))[7], '  Truck status:',
                                  display_map().get(str(count))[9], '  Delivery status:',
                                  display_map().get(str(count))[10])

            except IndexError:
                print(IndexError)
                exit()


            except ValueError:
                print("Incorrect entry!")
                exit()


        # if search is selected, user is told to enter a package ID,  then prompted to enter a time. user is then
        # given the total package info of that particular package at that particular time
        elif options == 'search':
            try:
                count = input('Please enter a package ID to search: ')
                try:
                    val = int(count)
                except ValueError:
                    print("Incorrect entry!")
                    exit()

                Time1 = display_map().get(str(count))[9]
                Time2 = display_map().get(str(count))[10]
                given_time = input('Please enter a time in the HH:MM:SS format: ')
                (hrs, mins, secs) = given_time.split(':')
                change_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, min, secs) = Time1.split(':')
                change_time1 = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = Time2.split(':')
                change_time2 = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                # checks if the package has left the hub yet

                if change_time1 >= change_time:

                    display_map().get(str(count))[10] = 'At Hub'
                    display_map().get(str(count))[9] = 'Leaves at ' + Time1
                    print('Package ID:', display_map().get(str(count))[0], '   Street address:',
                          display_map().get(str(count))[2], display_map().get(str(count))[3],
                          display_map().get(str(count))[4], display_map().get(str(count))[5],
                          '  Required delivery time:', display_map().get(str(count))[6],
                          ' Package weight:', display_map().get(str(count))[7], '  Truck status:',
                          display_map().get(str(count))[9], '  Delivery status:',
                          display_map().get(str(count))[10])

                elif change_time1 <= change_time:
                    # checks if packages have left but have not yet beem delivered
                    if change_time < change_time2:
                        display_map().get(str(count))[10] = 'In transit'
                        display_map().get(str(count))[9] = 'Left at ' + Time1
                        print('Package ID:', display_map().get(str(count))[0], '   Street address:',
                              display_map().get(str(count))[2], display_map().get(str(count))[3],
                              display_map().get(str(count))[4], display_map().get(str(count))[5],
                              '  Required delivery time:', display_map().get(str(count))[6],
                              ' Package weight:', display_map().get(str(count))[7], '  Truck status:',
                              display_map().get(str(count))[9], '  Delivery status:',
                              display_map().get(str(count))[10])

                    # if package has been delivered, display the time
                    else:
                        display_map().get(str(count))[10] = 'Delivered at ' + Time2
                        display_map().get(str(count))[9] = 'Left at ' + Time1
                        print('Package ID:', display_map().get(str(count))[0], '   Street address:',
                              display_map().get(str(count))[2], display_map().get(str(count))[3],
                              display_map().get(str(count))[4], display_map().get(str(count))[5],
                              '  Required delivery time:', display_map().get(str(count))[6],
                              ' Package weight:', display_map().get(str(count))[7], '  Truck status:',
                              display_map().get(str(count))[9], '  Delivery status:',
                              display_map().get(str(count))[10])


            except ValueError:
                print('Incorrect entry!')
                exit()

        elif options == 'close':
            exit()

        else:
            print('Incorrect entry!')
            exit()
