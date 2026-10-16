## Q1. Find the Frequency of Each Word in a Sentence
from solutions import word_frequency
word_freq1 = word_frequency("python is easy and python is powerful")
print(word_freq1) 

word_freq2 = word_frequency("coding with python programming coding")
print(word_freq2)

## Q2. Find the Frequency of Each Character in a Word
from solutions import char_frequency
char_freq1 = char_frequency("banana") 
print(char_freq1)

char_freq2 = char_frequency("programming")
print(char_freq2)

## Q3. Find the First Non-Repeating Character in a Word
from solutions import first_non_repeating_char
first_non_repeating1 = first_non_repeating_char("swiss")
print(first_non_repeating1)

first_non_repeating2 = first_non_repeating_char("programming")
print(first_non_repeating2)

## Q4. Check Whether Two Strings Are Anagrams
from solutions import are_anagrams
anagram_check1 = are_anagrams("listen", "silent")  
print(anagram_check1)

anagram_check2 = are_anagrams("hello", "world")
print(anagram_check2)

## Q5. Find the First Repeating Character in a String
from solutions import first_repeating_char
first_repeating1 = first_repeating_char("programming")
print(first_repeating1)

first_repeating2 = first_repeating_char("swiss")
print(first_repeating2)

## Q6. Move All Zeros to the End of a List
from solutions import move_zeros_to_end
list1 = [0, 3, 0, 1, 2, 0, 4]
result1 = move_zeros_to_end(list1)
print(result1)

list2 = [0, 0, 1, 0, 2, 3]
result2 = move_zeros_to_end(list2)
print(result2)

## Q7. Find the Second Highest Distinct Number in a List
from solutions import second_highest_distinct
list1 = [10, 20, 40, 30, 40, 20]
second_highest1 = second_highest_distinct(list1)        
print(second_highest1)

list2 = [10, 20, 30, 40, 50]
second_highest2 = second_highest_distinct(list2)
print(second_highest2)

## Q8. Remove Duplicates Without Changing the Original Order
from solutions import remove_duplicates
list1 = [4, 2, 4, 5, 2, 7, 5]
result1 = remove_duplicates(list1) 
print(result1)

list2 = ['a', 'b', 'c', 'a', 'd', 'b']
result2 = remove_duplicates(list2)
print(result2)

## Q9. Find the Missing Number from 1 to N
from solutions import find_missing_number
list1 = [1, 2, 4, 5, 6]
N1 = 6
missing_number1 = find_missing_number(list1, N1)
print(missing_number1)

list2 = [1, 2, 3, 5]
N2 = 5
missing_number2 = find_missing_number(list2, N2)
print(missing_number2)


## Q10. Find Two Numbers Whose Sum Equals a Target
from solutions import find_two_numbers_with_sum
list1 = [2, 7, 11, 15]
target1 = 9
result1 = find_two_numbers_with_sum(list1, target1) 
print(result1)

list2 = [1, 2, 3, 4, 5]
target2 = 8
result2 = find_two_numbers_with_sum(list2, target2)
print(result2)

## Q11. Find the Number Closest to Zero
from solutions import closest_to_zero
list1 = [-8, -3, 2, 5, -2]
closest1 = closest_to_zero(list1)
print(closest1)

list2 = [-10, -5, -1, 2, 4]
closest2 = closest_to_zero(list2)
print(closest2)

## Q12. Find Common Elements Between Two Lists
from solutions import common_elements
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common1 = common_elements(list1, list2)
print(common1)

list3 = ['a', 'b', 'c', 'd']
list4 = ['c', 'd', 'e', 'f']
common2 = common_elements(list3, list4)
print(common2)

## Q13. Rotate a List to the Right by K Positions
from solutions import rotate_list
list1 = [1, 2, 3, 4, 5]
k1 = 2
rotated1 = rotate_list(list1, k1)
print(rotated1)

list2 = ['a', 'b', 'c', 'd', 'e']
k2 = 3
rotated2 = rotate_list(list2, k2)
print(rotated2)

## Q14. Find the Maximum Sum of Two Consecutive Elements
from solutions import max_sum_of_consecutive
list1 = [4, 7, 2, 9, 5]
max_sum1 = max_sum_of_consecutive(list1)
print(max_sum1)

list2 = [10, 20, 30, 5, 15]
max_sum2 = max_sum_of_consecutive(list2)
print(max_sum2)

## Q15. Find All Pairs of Numbers Whose Sum Equals a Target
from solutions import find_all_pairs_with_sum
list1 = [2, 4, 3, 5, 7, 8, 1]
target1 = 9
pairs1 = find_all_pairs_with_sum(list1, target1)
print(pairs1)

list2 = [10, 20, 30, 40, 50]
target2 = 60
pairs2 = find_all_pairs_with_sum(list2, target2)
print(pairs2)





