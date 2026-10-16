# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# Q2. Find the Frequency of Each Character in a Word
def char_frequency(word):
    frequency = {}
    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating_char(word):
    frequency = {}
    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    for char in word:
        if frequency[char] == 1:
            return char 
    else:
        return None

## Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    frequency1 = {}
    frequency2 = {}
    for char in str1:
        if char in frequency1:
            frequency1[char] += 1
        else:
            frequency1[char] = 1
    for char in str2:
        if char in frequency2:
            frequency2[char] += 1
        else:
            frequency2[char] = 1
    return frequency1 == frequency2

## Q5. Find the First Repeating Character in a String
def first_repeating_char(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    for char in string:
        if frequency[char] > 1:
            return char
    else:
        return None

## Q6. Move All Zeros to the End of a List
def move_zeros_to_end(lst):
    non_zero_elements = [num for num in lst if num != 0]
    zero_count = lst.count(0)
    return non_zero_elements + [0] * zero_count

## Q7. Find the Second Highest Distinct Number in a List
def second_highest_distinct(lst):
    distinct_numbers = list(set(lst))
    if len(distinct_numbers) < 2:
        return None
    distinct_numbers.sort(reverse=True)
    return distinct_numbers[1]

## Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


## Q9. Find the Missing Number from 1 to N
def find_missing_number(lst, N):
    expected_sum = N * (N + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

## Q10. Find Two Numbers Whose Sum Equals a Target
def find_two_numbers_with_sum(lst, target):
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    return None

## Q11. Find the Number Closest to Zero
def closest_to_zero(lst):
    closest = lst[0]
    for num in lst:
        if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
            closest = num
    return closest


## Q12. Find Common Elements Between Two Lists
def common_elements(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return list(set1.intersection(set2))

## Q13. Rotate a List to the Right by K Positions
def rotate_list(lst, k):
    n = len(lst)
    k = k % n 
    return lst[-k:] + lst[:-k]

## Q14. Find the Maximum Sum of Two Consecutive Elements
def max_sum_of_consecutive(lst):
    if len(lst) < 2:
        return None
    max_sum = lst[0] + lst[1]
    for i in range(1, len(lst) - 1):
        current_sum = lst[i] + lst[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

## Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def find_all_pairs_with_sum(lst, target):
    pairs = []
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.append([complement, num])
        seen.add(num)
    return pairs

