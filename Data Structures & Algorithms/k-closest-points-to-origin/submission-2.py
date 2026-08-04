class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        n = len(points)
        for i in range(min(k, n)):
            distances.append([((points[i][0] ** 2) + (points[i][1] ** 2)) * -1, points[i]])
        heapq.heapify(distances)
        for i in range(k, n):
            distance = ((points[i][0] ** 2) + (points[i][1] ** 2)) * -1
            if distances[0][0] < distance:
                heapq.heappop(distances)
                heapq.heappush(distances, [distance, points[i]])
        final = []
        for i in range(min(k, len(distances))):
            popped = heapq.heappop(distances)
            final.append(popped[1])
        return final
