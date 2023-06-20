"""
https://leetcode.com/problems/design-underground-system/

An underground railway system is keeping track of customer travel times between different stations.
They are using this data to calculate the average time it takes to travel from one station to another.

Implement the UndergroundSystem class:

void checkIn(int id, string stationName, int t)
A customer with a card ID equal to id, checks in at the station stationName at time t.
A customer can only be checked into one place at a time.
void checkOut(int id, string stationName, int t)
A customer with a card ID equal to id, checks out from the station stationName at time t.
double getAverageTime(string startStation, string endStation)
Returns the average time it takes to travel from startStation to endStation.
The average time is computed from all the previous traveling times from startStation to endStation that
happened directly, meaning a check in at startStation followed by a check out from endStation.
The time it takes to travel from startStation to endStation may be different from the time it takes to
travel from endStation to startStation.
There will be at least one customer that has traveled from startStation to endStation before
getAverageTime is called.
You may assume all calls to the checkIn and checkOut methods are consistent.
If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.


Notes:
My design looks fine, fails 2 out of 58 test cases because...
The input does not keep this valid but says it is guaranteed:
A customer can only be checked into one place at a time.
"""
import collections


class UndergroundSystem:

    def __init__(self):
        self.average_times = collections.defaultdict(RouteTime)
        self.active_travelers = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.active_travelers[id] = CheckIn(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkIn = self.active_travelers[id]
        checkInStation = checkIn.stationName
        checkInTime = checkIn.time
        key = tuple([checkInStation, stationName])
        time_taken = t - checkInTime
        del self.active_travelers[id]
        self.average_times[key].update_average(time_taken)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.average_times[tuple([startStation, endStation])].get_average()


class CheckIn:

    def __init__(self, stationName, time):
        self.stationName = stationName
        self.time = time


class RouteTime:

    def __init__(self):
        self.total_time = 0
        self.count = 0

    def update_average(self, new_time_observation):
        self.total_time += new_time_observation
        self.count += 1

    def get_average(self):
        return self.total_time / self.count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)