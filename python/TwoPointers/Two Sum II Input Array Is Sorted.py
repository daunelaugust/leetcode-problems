def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # the idea here is to set up two pointers and move the pointer at the end or the start towards the solution
        if len(numbers) == 1:
            return numbers

        i = 0
        j = len(numbers)-1

        while i<j:

            if target == numbers[i] + numbers[j]:
                return [i+1, j+1]
            elif target > numbers[i] + numbers[j]:
                i+=1
                continue
            elif target < numbers[i] + numbers[j]:
                j-=1