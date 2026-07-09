class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        combo = []
        for i in range(n):
            combo.append([position[i], speed[i]])
        combo.sort() #NlogN
        time = [0] * n
        #[0 1 5 8]->[4 4 9 11]->[7 7 13 14]->[8 8 14.67 15]
        #[5 3 4 3]  [[15/5->3][14/3->4.67][10/4->2.5],[7/3->2.33]]
        groups = n
        time[n - 1] = (target - combo[n - 1][0]) / combo[n - 1][1]
        for i in range(n - 2, -1, -1): #O(N)
            time[i] = max(((target - combo[i][0]) / combo[i][1]), time[i + 1])
            if time[i] == time[i + 1]:
                groups -= 1
        return groups
