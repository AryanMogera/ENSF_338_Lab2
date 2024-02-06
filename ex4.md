1. I would use a binary search since the rooms are sorted. The binary search would divide the array of rooms in half, if the key matches the middle item the search ends. if the key is < middle item it divides the left subarray in half repeats from beginning or if key is > middle item it divides the right subarray in half and repeats until a match is found.

2. 

3. 

4. With this particular sign and floor layout, the worst case scenario will be element in first last or does not exist O(logn), the best case scenario will be element to find is exactly in the middle O(1)

5. we can make the algorithm more efficient by changing the application of midpoint, it can be modified accordingly so that it converges faster towards the first element. A condition could be added to binary search to look for first or last element which will result in O(1) without traversing through the entire array.
