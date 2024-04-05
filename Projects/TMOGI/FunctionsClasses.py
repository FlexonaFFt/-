import math
import matplotlib.pyplot as plt

class GeodesyCalculations:


    def __init__(self):
        self.coordinates = []
        self.hord_distances = []
        self.radius = []
        self.betta = 0

    def import_coordinates(self):
        num_ = int(input("Введите количество координат: "))
        for el_ in range(num_):
            lat = float(input(f"Введите широту {el_ + 1}: "))
            lon = float(input(f"Введите долготу {el_ + 1}: "))
            self.coordinates.append((lat, lon))
        
        print('Добавлены следующие координаты: ')
        print(self.coordinates)

    def calculate_hord_distance(self):
        for i in range(len(self.coordinates) - 1):
            hord = []
            if len(self.coordinates[i]) == 2:
                lat_1, lon_1 = self.coordinates[i]
            else:
                lat_1, lon_1 = self.coordinates[i][0], self.coordinates[i][1]
            for el_2 in self.coordinates[i+1:]:
                if len(el_2) == 2:
                    lat_2, lon_2 = el_2
                else:
                    lat_2, lon_2 = el_2[0], el_2[1]
                d = math.sqrt((lat_2 - lat_1) ** 2 + (lon_2 - lon_1) ** 2)
                hord.append(d)
            self.hord_distances.append(hord)
        # print(self.hord_distances)

    def calculate_radius(self):
        for i in range(len(self.hord_distances)):
            hord = self.hord_distances[i]
            for j in range(len(hord)):
                radius = hord[j] / (2 * math.sin(math.pi / len(hord)))
                self.radius.append(radius)
        # print(self.radius)
    
    def calculate_optimal_grades(self):
        self.betta = math.acos(self.hord_distances[0][0] / self.radius[0])
        print(self.betta)

    def center_coordinates(self):
        center_lat = 0
        center_lon = 0
        alfa_1 = math.atan()


    def plot_hord_distance(self):
        distances = [d for sublist in self.hord_distances for d in sublist]
        plt.plot(distances)
        plt.xlabel('Index')
        plt.ylabel('Horizontal Distance')
        plt.title('Horizontal Distances')
        plt.show()
                                