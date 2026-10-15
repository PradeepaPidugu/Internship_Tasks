from solutions import(
    word_frequency,
    char_frequency,
    first_non_rep_char,
    str_anagram,
    first_rep_char,
    move_zeros_to_end,
    second_high_distinct_num,
    remove_dup,
    missing_num,
    sum_equal_target,
    num_closeto_zero,
    common_ele_2list,
    rotate_k_pos,
    max_sum_2consec,
    unique_pairs_sum_equal_target
)
# Q1
print("Q1:", word_frequency("python is easy and python is powerful"))

# Q2
print("Q2:", char_frequency("banana"))

# Q3
print("Q3:", first_non_rep_char("swiss"))

# Q4
print("Q4:", str_anagram("listen", "silent"))

# Q5
print("Q5:", first_rep_char("programming"))

# Q6
print("Q6:", move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]))

# Q7
print("Q7:", second_high_distinct_num([10, 20, 40, 30, 40, 20]))

# Q8
print("Q8:", remove_dup([4, 2, 4, 5, 2, 7, 5]))

# Q9
print("Q9:", missing_num([1, 2, 4, 5, 6], 6))

# Q10
print("Q10:", sum_equal_target([2, 7, 11, 15], 9))

# Q11
print("Q11:", num_closeto_zero([-8, -3, 2, 5, -2]))

# Q12
print("Q12:", common_ele_2list([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

# Q13
print("Q13:", rotate_k_pos([1, 2, 3, 4, 5], 2))

# Q14
print("Q14:", max_sum_2consec([4, 7, 2, 9, 5]))

# Q15
print("Q15:", unique_pairs_sum_equal_target([2, 4, 3, 5, 7, 8, 1], 9))



print("\nADDITIONAL TEST CASES")

print("Q1:", word_frequency("apple apple mango"))

print("Q2:", char_frequency("hello"))

print("Q3:", first_non_rep_char("aabbc"))

print("Q4:", str_anagram("race", "care"))

print("Q5:", first_rep_char("abca"))

print("Q6:", move_zeros_to_end([1, 0, 2, 0, 3]))

print("Q7:", second_high_distinct_num([5, 10, 10, 3]))

print("Q8:", remove_dup([1, 1, 2, 3, 2]))

print("Q9:", missing_num([1, 3, 4, 5], 5))

print("Q10:", sum_equal_target([1, 2, 3], 5))

print("Q11:", num_closeto_zero([-5, -1, 3]))

print("Q12:", common_ele_2list([1, 2, 2, 3], [2, 3, 4]))

print("Q13:", rotate_k_pos([1, 2, 3], 1))

print("Q14:", max_sum_2consec([1, 10, 2]))

print("Q15:", unique_pairs_sum_equal_target([1, 2, 3, 4, 5, 6], 7))