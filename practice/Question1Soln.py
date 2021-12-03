#Question 1

# Given a target value, this function will determine if the value exists in the list or not
#
# target - the value we are searching for
# nums - the list of numbers given
#
# Return true if found, otherwise false.
# NOTE: This should work for any list size given 
def search(target, nums):
    #Modify the body below
    for num in nums:
        if num == target:
            return True
    return False


def main():

    # Test search function
    myNums = []
    target = 10
    print("Empty set of nums: ", search(target, myNums)) # Should return False
    myNums = [2,5,3,7,10,8,1,9,6,4]

    print("Target: ", target, "Target Found: ", search(target, myNums)) # Should return True

    target = 11
    print("Target: ", target, "Target Found: ", search(11, myNums)) # Should return False


# What is the time complexity of the search function given a list of length N?
# Reponse: 

if __name__ == "__main__":
    main()
"""
# Question 1 Solution
# Time complexity is Linear, or O(N)
"""
