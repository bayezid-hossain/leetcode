class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        #max heap
        max_heap=[]
        
        #for each class we calculate the percentage gain and push it to max_heap
        for passed,students in classes:
            gain=((passed+1)/(students+1))-((passed)/(students))
            heappush(max_heap,(-gain,passed,students))

        #calculate new gain for each class by adding 1 extra student Since the change in the pass ratio is  always decreasing with the more students you add, then the very first student you add to each class is the one that makes the biggest change in the pass ratio.
        for _ in range(extraStudents):
            gain,passed,total=heappop(max_heap)

            passed+=1
            total+=1

            new_gain=((passed+1)/(total+1))-((passed)/(total))
            heappush(max_heap,(-new_gain,passed,total))
        
        total_ratio=0
        #just calculating total ratio 
        for i,passed,total in max_heap:
            total_ratio+=(passed/total)
        #average ratio
        return total_ratio/len(classes)