class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        operations = []
        index = 0

        for number in range(1, n + 1):
            if index == len(target):
                break
            if number == target[index]:
                operations.append("Push")
                index += 1
            else:
                operations.append("Push")
                operations.append("Pop")

        return operations
            