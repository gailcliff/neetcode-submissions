class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        least_fleet_time = float('-inf')
        fleets = 0

        for pos, spd in cars:
            time_taken = (target - pos) / spd

            if time_taken > least_fleet_time:
                fleets += 1
                least_fleet_time = time_taken
            
        return fleets