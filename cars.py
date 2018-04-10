import os
import csv


class CarBase:
    """General class describes car types"""
    def __init__(self, car_type, brand, carrying: float, photo_file_name):
        """Init general class"""
        self.car_type = car_type
        self.brand = brand
        self.carrying = carrying
        self.photo_file_name = photo_file_name

    def get_photo_file_ext(self):
        """Method to get extension of photo file"""
        return os.path.splitext(self.photo_file_name)[1]



class Car(CarBase):
    """Class describes cars"""
    def __init__(self, car_type, brand, carrying, photo_file_name, passenger_seats_count: int):
        """Init car class"""
        super().__init__(car_type, brand, carrying, photo_file_name)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    """Class describes trucks"""
    def __init__(self, car_type, brand, carrying, photo_file_name, body_width: float, body_height: float, body_length: float):
        """Init truck class"""
        super().__init__(car_type, brand, carrying, photo_file_name)
        self.body_width = body_width
        self.body_height = body_height
        self.body_length = body_length

    def get_body_volume(self):
        """Method to get body volume of truck"""
        return self.body_width*self.body_height*self.body_length


class SpecMachine(CarBase):
    """Class describes special machines"""
    def __init__(self, car_type, brand, carrying, photo_file_name, extra):
        """Init special machine class"""
        super().__init__(car_type, brand, carrying, photo_file_name)
        self.extra = extra


def get_car_list(csv_filename):
    """Function parse CSV file and create list of objects based on it"""
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            if len(row) != 7 or row[0] == '' or row[1] == '' or row[3] == '' or row[5] == '':
                print('1: Unexpected list of values ', row)
            else:
                car_type = row[0]
                brand = row[1]
                photo_file_name = row[3]
                try:
                    carrying = float(row[5])
                except Exception:
                    print('Unexpected type of value')
                    continue
                if row[0] == 'car':
                    if row[2] == '' or row[4] != '' or row[6] != '':
                        print('2: Unexpected list of values ', row)
                    else:
                        try:
                            passenger_seats_count = int(row[2])
                        except Exception:
                            print('Unexpected type of value')
                            continue
                        car = Car(car_type, brand, carrying, photo_file_name, passenger_seats_count)
                        car_list.append(car)
                elif row[0] == 'truck':
                    if row[2] != '' or row[6] != '':
                        print('3: Unexpected list of values ', row)
                    else:
                        if row[4] == '':
                            body_width = 0.00
                            body_heigh = 0.00
                            body_length = 0.00
                        else:
                            tmp = row[4].split('x')
                            if len(tmp) == 3:
                                try:
                                    body_width = float(tmp[0])
                                    body_heigh = float(tmp[1])
                                    body_length = float(tmp[2])
                                except Exception:
                                    print('Unexpected type of value')
                                    continue
                            else:
                                print('Unexpected number of value')
                                continue
                        car = Truck(car_type, brand, carrying, photo_file_name, body_width, body_heigh, body_length)
                        car_list.append(car)
                elif row[0] == 'spec_machine':
                    if row[6] == '' or row[2] != '' or row[4] != '':
                        print('4: Unexpected list of values ', row)
                    else:
                        extra = row[6]
                        car = SpecMachine(car_type, brand, carrying, photo_file_name, extra)
                        car_list.append(car)
                else:
                    print('Unexpected car type', row)
    return car_list
