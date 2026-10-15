# ------1------
def word_frequency(text):
    words=text.split()
    result={}
    for word in words:
        if word in result:
            result[word]+=1
        else:
            result[word]=1
    return result

# ------2------
def char_frequency(text):
    result={}
    for ch in text:
        if ch in result:
            result[ch]+=1
        else:
            result[ch]=1
    return result

# ------3------
def first_non_rep_char(word):
    for ch in word:
        if word.count(ch)==1:
            return ch
    return None

# ------4------
def str_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    return sorted(s1)==sorted(s2)

# ------5------
def first_rep_char(text):
    for ch in text:
        if text.count(ch)>1:
            return ch
    return None

# ------6------
def move_zeros_to_end(nums):
    result=[]
    for i in nums:
        if i!=0:
            result.append(i)
    zeros_count=len(nums)-len(result)
    result.extend([0]*zeros_count)
    return result

# ------7------
def second_high_distinct_num(nums):
    result=sorted(set(nums))
    if len(result)<2:
        return None
    return result[-2]

# ------8------
def remove_dup(nums):
    result=[]
    for num in nums:
        if num not in result:
            result.append(num)
    return result

# ------9------
def missing_num(nums,n):
    sum_n=n*(n+1)//2
    s1=sum(nums)
    return sum_n-s1

# ------10------
def sum_equal_target(nums,target):
    seen=set()
    for num in nums:
        required=target-num
        if required in seen:
           return [required,num]
        seen.add(num)
    return []

# ------11------
def num_closeto_zero(nums):
    short=float('inf')
    for num in nums:
        shortest=abs(num)
        if shortest<short:
            short=shortest
    return short

# ------12------
def common_ele_2list(l1,l2):
    result=[]
    for num in l1:
        if num in l2 and num not in result:
            result.append(num)
    return result

# ------13------
def rotate_k_pos(nums,k):
    if not nums:
        return []
    k=k%len(nums)

    return nums[-k:]+nums[:-k] if k else nums[:]

# ------14------
def max_sum_2consec(nums):
    max_sum=nums[0]+nums[1]
    for i in range(1,len(nums)-1):
        curr_sum=nums[i]+nums[i+1]
        if curr_sum>max_sum:
            max_sum=curr_sum
    return max_sum

# ------15------
def unique_pairs_sum_equal_target(nums,target):
    result=set()
    pairs=set()
    for num in nums:
        required=target-num
        if required in result:
            pair=tuple(sorted((num,required)))
            pairs.add(pair)
        result.add(num)
    return [list(pair) for pair in sorted(pairs)]