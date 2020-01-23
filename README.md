# CodingTask

## Running the example
- run `python merging_example.py` in the root directory

## Running tests
- run `python -m pytest .` in the root directory
- or similarly run `sh run_tests.sh` in the root directory

## Solution approach
My first approach was using recursion and deleting elements from the list.
Finally however, I decided to use a simple for loop in order to generate the merged list.
I iterate over all intervals in the list and build the result conditionally depending on
whether the interval overlaps or not. The if-Block checks whether the interval at the current
index lays within the previous interval(s) or not. If the condition is true, it means that the 
starting position of the new entry is greater than the current maximum end position. I append
the current interval. In the else block, I update the end-position of my last element in the merged
list, until a new element is greater. If my merging list is empty (at the beginning), I set it to the
current element itself.

### Time complexity:
Considering a sorted list the runtime will be O(n). 
The python sorting method uses timsort which has O(n*log(n)).

### Space complexity:
The only dynamic part of the algorithm is the generated merged list.
In the worst case (when having no overlaps) the space complexity is O(n).
In the best case, when there is a full overlap, the space complexity is O(1).