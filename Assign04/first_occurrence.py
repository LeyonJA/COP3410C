
"""
Coded by: Leyon Anderson
3/28/2026
COP3410 Assignment #4

Goal is to modify the binary search algorithm to find the position of the first occurrence 
of a value that can occur multiple times in the ordered list.
"""

def fOccurence(lst, target):
    '''
    A binary search algorithm to find the position of the first occurence of a value.

    :param list lst: List of integers.
    :param int target: The target to find.
    '''
    low = 0
    high = len(lst) - 1
    result = -1 # Default if not found

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == target:
            result = mid    # Track location if match found
            high = mid - 1  # Keep looking to the left (to find earlier occurnaces)
        elif lst[mid] < target:
            low = mid + 1
        else: 
            high = mid - 1

    return result

if __name__ == "__main__":
    test_case = [1, 2, 2, 3, 4, 5, 6, 6]    # Test case list
    target = 6                              # Test case target

    result = fOccurence(test_case, target)

    print(f'{f"{target} was first found at index {result}." if result != -1 else f"{target} was not found."}')