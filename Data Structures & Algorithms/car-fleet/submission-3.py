class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        cars.sort(reverse=True)

        for pos, spd in cars:
            times.append((target - pos) / spd)
            # Join the same fleet if top of stack <= car in front
            if len(times) >= 2 and times[-1] <= times[-2]:
                times.pop()
        print(times)
        return len(times)


        