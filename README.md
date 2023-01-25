# Airplane-Seating-Algo

The time complexity of this algorithm is O(n^2), where n is the number of rows in the input array.

The outer while loop iterates n times, where n is the number of rows in the input array. Each iteration of the outer while loop consists of three nested while loops, one for each type of seat (aisle, window, and middle). Each nested while loop iterates through each column of the current row. Since the number of columns is constant for each row, the number of iterations in each nested while loop is also constant. Therefore, the total number of iterations in all three nested while loops is proportional to n.

In addition, there are also some for loops within the nested while loops that iterate through the elements of the mat variable, which is a 2-dimensional array. These for loops also have a constant number of iterations, so the time complexity of these for loops is also O(n).

As a result, the overall time complexity of the algorithm is O(n) \* O(n) = O(n^2).
