## Question 1

 I would use linear search as the we have no idea if the search space is sequentially placed or not. As linear search checks each element in sequential order, we know that its implementation would be superior in cases of rooms arranged in a random order. 


## Question 2 

It will take 15 steps considering room EY 100 as step 1 and EY 102 as step ...... till room EY 128. So, a step is each comparison against the target room number, and you would need 15 steps to find room EY128.

## Question 3

This neither case. 

## Question 4

The worst case would be if the target element is at the end of the search space which would be the room EY 138. This is also not th best case considering that the best case scenario in a sequentially arranged data set for a linear search is when the target element is the first element. This would be if the target element is EY 100 which would have O(1)

## Question 5 

We will have a more informed search strategy. We know that the room 128 is close if we start from EY 138 considering we already know the floor plan. We can optimize the search by starting closer to EY138 and moving towards EY128. This approach minimizes the distance and therefore the number of rooms you need to check. This is in simple words linear search applied on the reversed search space. 
