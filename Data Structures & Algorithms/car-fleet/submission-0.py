class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        slowest_fleet_time = 0
        num_fleets = 0

        for pos, spd in cars:
            time_to_target = (target - pos) / spd

            if time_to_target > slowest_fleet_time:
                # this car will take longer to arrive at the
                # destination and will not catch up with the
                # fleet whose time_to_target it is being 
                # compared to
                num_fleets += 1
                slowest_fleet_time = time_to_target

                # if the time_to_target < slowest_fleet_time,
                # it doesn't matter because this current fleet
                # will not be able to go past the fleet it is
                # being compared to, even if it would otherwise
                # arrive at the desination faster.
                # if time_to_target == slowest_fleet_time, then
                # they would arrive at the destination at the
                # same time. in either case, they would all be
                # part of the same fleet
        
        return num_fleets