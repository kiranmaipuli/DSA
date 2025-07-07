class minHeap:
    def __init__(self, heap_arr):
        self.heap_arr = heap_arr
        
    def heapify(self, topFreqDict):
        lastIndex = len(self.heap_arr) - 1
        lastParent = (lastIndex - 1) // 2
        for i in range(lastParent, -1, -1):
            index = i
            while index <= lastIndex:
                leftChild = (2*index) + 1
                rightChild = (2*index) + 2
                if rightChild <= lastIndex:
                    if topFreqDict[self.heap_arr[leftChild]] < topFreqDict[self.heap_arr[rightChild]]:
                        minIndex = leftChild
                    else:
                        minIndex = rightChild
                    if topFreqDict[self.heap_arr[index]] > topFreqDict[self.heap_arr[minIndex]]:
                        self.heap_arr[index], self.heap_arr[minIndex] = \
                            self.heap_arr[minIndex], self.heap_arr[index]
                        index = minIndex
                    else:
                        break
                elif leftChild <= lastIndex:
                    if topFreqDict[self.heap_arr[leftChild]] < topFreqDict[self.heap_arr[index]]:
                        self.heap_arr[index], self.heap_arr[leftChild] = \
                            self.heap_arr[leftChild], self.heap_arr[index]
                        index = leftChild
                    else:
                        break
                else:
                    break
            
        
    # def add(self, element):
    #     print("Adding element to the heap")
    #     self.heap_arr.append(element)
    #     currIndex = len(self.heap_arr) - 1
    #     parentIndex = (currIndex - 1) // 2
    #     while currIndex >= 0 and self.heap_arr[currIndex] < self.heap_arr[parentIndex]:
    #         self.heap_arr[currIndex], self.heap_arr[parentIndex] = \
    #             self.heap_arr[parentIndex], self.heap_arr[currIndex]
    #         currIndex = parentIndex
    #         parentIndex = (parentIndex - 1)//2                                    
            
        
    def delete(self, topFreqDict, reduce_arr_size=True):
        print("Deleting element from the heap")
        if self.heap_arr:
            lastIndex = len(self.heap_arr)-1
            currIndex = 0
            while currIndex <= lastIndex:
                leftChild = (2*currIndex) + 1
                rightChild = (2*currIndex) + 2
                if rightChild <= lastIndex:
                    if topFreqDict[self.heap_arr[leftChild]] < topFreqDict[self.heap_arr[rightChild]]:
                        minIndex = leftChild
                    else:
                        minIndex = rightChild
                    if topFreqDict[self.heap_arr[currIndex]] > topFreqDict[self.heap_arr[minIndex]]:
                        self.heap_arr[currIndex], self.heap_arr[minIndex] = \
                            self.heap_arr[minIndex], self.heap_arr[currIndex]
                        currIndex = minIndex
                    else:
                        break
                elif leftChild <= lastIndex:
                    if topFreqDict[self.heap_arr[leftChild]] < topFreqDict[self.heap_arr[currIndex]]:
                        self.heap_arr[currIndex], self.heap_arr[leftChild] = \
                            self.heap_arr[leftChild], self.heap_arr[currIndex]
                        currIndex = leftChild
                    else:
                        break
                else:
                    break
            
        else:
            print("Heap is empty")
            return None


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topFreqDict = {}
        minHeapArr = []
        minHeapObj = None
        count = 0
        if len(nums) == 1:
            return nums 
        for num in nums:
            if num not in topFreqDict:
                topFreqDict[num] = 1
            else:
                topFreqDict[num] += 1
        print(num)
        for num in topFreqDict:
            if len(minHeapArr) < k:
                minHeapArr.append(num)
            else:
                if topFreqDict[minHeapObj.heap_arr[0]] < topFreqDict[num]:
                    minHeapObj.heap_arr[0] = num
                    minHeapObj.delete(topFreqDict, reduce_arr_size=False)

            if (len(minHeapArr) == k) and (count == 0):
                minHeapObj = minHeap(minHeapArr)
                minHeapObj.heapify(topFreqDict)
                count += 1
        return minHeapObj.heap_arr
        

