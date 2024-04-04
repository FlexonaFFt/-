from FunctionsClasses import GeodesyCalculations as geo

geoObj = geo()
geoObj.import_coordinates()
geoObj.calculate_hord_distance()
geoObj.calculate_radius()
geoObj.optimal_radius()