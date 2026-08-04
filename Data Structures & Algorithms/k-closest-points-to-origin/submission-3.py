class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        if n < k:
            return points

        distances = []
        for i in range(k):
            distances.append([((points[i][0] ** 2) + (points[i][1] ** 2)) * -1, points[i]])
        heapq.heapify(distances)

        for i in range(k, n):
            distance = ((points[i][0] ** 2) + (points[i][1] ** 2)) * -1
            if distances[0][0] < distance:
                heapq.heappop(distances)
                heapq.heappush(distances, [distance, points[i]])

        final = []
        for i in range(k):
            final.append(heapq.heappop(distances)[1])
        return final
