## Sorting algorithms

#### Selection sort

Assume current index is the smallest element in the array or list. Iterate over the remaining portion of the array to find the smallest element compared to the one at the current index. Swap and repeat until end of the array is reached.

##### Complexity

Time: O(N^2) for all cases (Best, Average, Worst)<br>
Space: O(1) - sorts in place, does not require extra storage <br>

**Practice problem:** https://www.geeksforgeeks.org/problems/selection-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=selection-sort

---

#### Bubble sort

Repeatedly compare and swap adjacent elements to move larger values toward the end of the array. A boolean swapped, initialized to False, tracks if any swaps occur during a pass. If no swaps are made in a full pass, indicating the array is sorted, the algorithm terminates.

##### Complexity

Time: O(N) for best case ie already in order and O(N^2) for all other cases (Average, Worst)<br>
Space: O(1) - sorts in place, does not require extra storage <br>

**Practice problem:** https://www.geeksforgeeks.org/problems/bubble-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bubble-sort

---

#### Insertion sort

Assume the element at index 0 is already sorted. In the outer loop, start iterating from index 1(i) to n . In the inner loop, iterate backwards from the current index (i) to 0, comparing adjacent elements and swapping them if they are out of order. This process continues until the correct position for the current element is found. Repeat this process until the end of the outer loop.

##### Complexity

Time: O(N) for best case ie already in order and O(N^2) for all other cases (Average, Worst)<br>
Space: O(1) - sorts in place, does not require extra storage <br>

**Practice problem:** https://www.geeksforgeeks.org/problems/insertion-sort/0?category%5B%5D=Algorithms&page=1&query=category%5B%5DAlgorithmspage1&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=insertion-sort

---

#### Merge sort

Assume the entire array is initially unsorted. In the first step, divide the array into two halves. Recursively divide each half into two smaller halves until each subarray contains a single element, which is considered sorted. Then, begin merging the subarrays back together. In each merge step, compare the elements of the two subarrays and combine them in order, ensuring that the resulting array is sorted. This process continues until all subarrays have been merged back into a single sorted array.

##### Complexity

Time: O(N log N) for all cases (Best, Average, Worst)<br> 
Space: O(N) - requires additional space for the temporary arrays used during merging.<br>

**Practice problem:** https://www.geeksforgeeks.org/problems/merge-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=merge-sort

---

