class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        n = len(points)
        for i in range(n):
            distance = ((points[i][0] ** 2) + (points[i][1] ** 2))
            distances.append([distance, points[i]])
        distances.sort()
        print(distances)
        final = []
        for i in range(k):
            final.append(distances[i][1])
        return final