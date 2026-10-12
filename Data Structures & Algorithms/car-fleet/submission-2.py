class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions_speeds = list(sorted(zip(position, speed), reverse=True))

        fleets = 1

        time_to_beat = (target - positions_speeds[0][0]) / positions_speeds[0][1]

        for pos, spd in positions_speeds[1:]:
            fleet_time = (target - pos) / spd

            if fleet_time > time_to_beat:
                time_to_beat = fleet_time
                fleets += 1
        
        return fleets