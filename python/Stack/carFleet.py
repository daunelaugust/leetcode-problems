def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        stack = []

        for i in range(len(position)):

            slope =(target - position[i])/ speed[i]
            fleets.append((position[i], speed[i], slope))

        
        fleets = sorted(fleets, key = lambda x: x[0])

        print(fleets)

        for _, _, k in fleets[::-1]:

            if not stack or k > stack[-1]:
                
                stack.append(k)
        
        return len(stack)