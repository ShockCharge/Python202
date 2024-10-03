"""
# The sequence_checker() function will see if the length of s1 matches the length of s2.
# By default it's set to True boolean. However, once the checker does not match the length, it will return a False boolean.
"""
def sequence_checker(s1,s2):
    if len(s1) != len(s2):
        return False
    return True

"""
# calculate_mean() function creates a list of numbers, adding and increasing them, dividing the total, and count so it prints the average.
# For Example: My list is [5, 6, 8, 9, 13] Total sum is 41, and the count is 5. Now, when you divide them, the result should be 41 / 5 = 8.2.
"""
def calculate_mean(anysequence):
    total = 0
    count = 0
    for num in anysequence:
        total += num
        count += 1
    return total / count

"""
# distance_fn() function checks if the s1 and s2 lists have the same length, 
# finds the difference in between, and multiplies it. Then it returns the total number to squared_diff_sum.
"""
def distance_fn(s1,s2):
    squared_diff_sum = 0
    for i in range(len(s1)):
        squared_diff_sum += (s1[i] - s2[i]) ** 2
    return squared_diff_sum

"""
# These 2 lists have 5 elements that are both used in the distance_fn() function to calculate the difference and give the total amount. 
"""
s1 = [1,2,4,5,9]
s2 = [6,7,8,9,10]

"""
# cond calls the sequence_checker() function from above to grab the boolean result, which is True since S1 and S2 have the same length.
# me1 and me2 are pretty simple, as they find the mean or average of S1 and S2 to store here.
# Anyway, the rest of the code is just printing the results, and if the cond boolean result is False, it will say the error message.
"""
cond = sequence_checker(s1,s2)
if (cond):
    me1 = calculate_mean(s1)
    me2 = calculate_mean(s2)
    distance = distance_fn(s1,s2)
    print("Mean of sequence 1:", me1)
    print("Mean of sequence 2:", me2)
    print("Distance between the sequences:", distance)
else:
    print('Warning! Error.')
"""
# Also, the 4th question, squared_diff_sum += (s1[i] - s2[i]) will result in the numbers being negative and be inaccurate
# to show the difference because it only adds them together without using squaring. Therefore, the final result will be -19 instead of 83.
"""