# class NumMatrix:

#     def __init__(self, matrix: List[List[int]]):
#         self.numMatrix = matrix
#         self.sumMatrix = []
#         # print(len(self.numMatrix))
#         # print(self.numMatrix)
#         self.initializeSumMatrix()

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         totalSum = 0
#         for row in range(row1, row2+1):
#             if col1 > 0:
#                 print(row, col1, col2, "iiiiii")
#                 totalSum += (self.sumMatrix[row][col2] - self.sumMatrix[row][col1-1])
#             else:
#                 totalSum += self.sumMatrix[row][col2]
#         return totalSum

#     def initializeSumMatrix(self):
#         for row in range(len(self.numMatrix)):
#             currColumn = []
#             for column in range(len(self.numMatrix[row])):
#                 if column == 0:
#                     currColumn.append(self.numMatrix[row][column])
#                 else:
#                     print()
#                     currColumn.append(currColumn[column-1] + self.numMatrix[row][column])
#             self.sumMatrix.append(currColumn)
#         # print(self.sumMatrix)


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.numMatrix = matrix
        self.sumMatrix = []
        # print(len(self.numMatrix))
        # print(self.numMatrix)
        self.initializeSumMatrix()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print(self.sumMatrix)
        totalSum = 0
        if row1 == 0 and col1 == 0:
            # print(row1,row2,col1,col2, "hgcydgcdgc")
            totalSum = self.sumMatrix[row2][col2]
        elif row1 == 0:
            # print(row1,row2,col1,col2, "*********")
            totalSum = self.sumMatrix[row2][col2] - self.sumMatrix[row2][col1-1]
        elif col1 == 0:
            # print(row1,row2,col1,col2, "&&&&&&&&&&")
            # print(self.sumMatrix[row2][col2], self.sumMatrix[row1-1][col2])
            totalSum = self.sumMatrix[row2][col2] - self.sumMatrix[row1-1][col2]
        else:
            # print(row1,row2,col1,col2, "+++++++++++")
            temp = self.sumMatrix[row2][col1-1] - self.sumMatrix[row1-1][col1-1]
            totalSum = self.sumMatrix[row2][col2] - self.sumMatrix[row1-1][col2] - temp
        return totalSum

        # for row in range(row1, row2+1):
        #     if col1 > 0:
        #         print(row, col1, col2, "iiiiii")
        #         totalSum += (self.sumMatrix[row][col2] - self.sumMatrix[row][col1-1])
        #     else:
        #         totalSum += self.sumMatrix[row][col2]
        # return totalSum

    def initializeSumMatrix(self):
        for row in range(len(self.numMatrix)):
            currColumn = []
            for column in range(len(self.numMatrix[row])):
                if row == 0 and column == 0:
                    currColumn.append(self.numMatrix[row][column])
                elif row == 0:                    
                    currColumn.append(currColumn[column-1] + self.numMatrix[row][column])
                elif column == 0:
                    currColumn.append(self.sumMatrix[row-1][column] + self.numMatrix[row][column])
                else:
                    currColumn.append(currColumn[column-1] + self.numMatrix[row][column] + self.sumMatrix[row-1][column] - self.sumMatrix[row-1][column-1])

            self.sumMatrix.append(currColumn)
        # print(self.sumMatrix)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)