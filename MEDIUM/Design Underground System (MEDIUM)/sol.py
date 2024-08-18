class Customer:
    def __init__(self, stationName: str, t: int):
        self.stationName = stationName
        self.t = t

class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.trip_data = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = Customer(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        customer = self.customers.pop(id)
        trip = (customer.stationName, stationName)
        trip_time = t - customer.t

        if trip not in self.trip_data:
            self.trip_data[trip] = [trip_time]
        else:
            self.trip_data[trip].append(trip_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip = (startStation, endStation)
        total_time = sum(self.trip_data[trip])
        trip_count = len(self.trip_data[trip])
        return total_time / trip_count
