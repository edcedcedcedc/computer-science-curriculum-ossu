import test_suite

""" 
WARMP UP sliding window // min len subarray sum >= target 

l 
left pointer = 0
right pointer = 0
min len = float inf 
cur len = 0
cur sum = 0

main loop
    if right pointer >= left pointer 
        cur sum += l(right pointer) 
        inner loop cur sum >= t
            cur len = right - left + 1
            if cur len < min len
                min len = cur len
            cur sum -= l(left pointer)
            left pointer += 1 
    right pointer += 1   
 """

def min_len_subarray_sum_06102026(l, t):
    left_p = 0
    cur_len = 0
    min_len = float('inf')
    cur_sum = 0 
    for right_p in range(len(l)):
        if right_p >= left_p:
            cur_sum += l[right_p]
            while cur_sum >= t:
                cur_len = right_p - left_p + 1
                if cur_len < min_len:
                    min_len = cur_len
                cur_sum -= l[left_p]
                left_p += 1
    return min_len if min_len != float('inf') else 0


                
""" 
REVIEW hash map
 """

def duplicate2_06102026(l,k):
    map = dict()
    for i in range(len(l)):
        if l[i] in map:
            d = abs(map[l[i]] - i)
            if d <= k:
                return True 
        map[l[i]] = i 


""" MASTERY CHALLENGE  prefix sum"""       


class RangeSumQuery:
    def __init__(self, nums):
        self.prefix = list()
        self.prefix.append(nums[0])
        for i in range(1, len(nums)):
            self.prefix.append(self.prefix[i - 1] + nums[i])
    def sum_range(self, i, j):
        return self.prefix[j] - self.prefix[i - 1]
        







""" 
WARM UP 10/07/2026
"""

class PrefixSum():
    def __init__(self, arr):
        self.arr = arr
        self.prefix_arr = list()
        self.prefix_arr.append(arr[0])
        for i in range(1, len(arr)):
            self.prefix_arr.append(self.prefix_arr[i - 1] + self.arr[i])

   
    def sum_interval(self,i: int, j: int) -> int:
        if i == 0:
            return self.prefix[j]
        return self.prefix_arr[j] - self.prefix_arr[i - 1]




""" 

REVIEW // sliding window 
"""

def longest_substring_without_repeating_07_10_2026(s: str) -> int:
    array = list(s)
    hash_map = dict()
    pointer_left = 0
    max_len = 0
    current_len = 0
    for pointer_right in range(len(array)):
        if array[pointer_right] in hash_map:
            if hash_map[array[pointer_right]] >= pointer_left:
                pointer_left = hash_map[array[pointer_right]] + 1
                current_len = pointer_right - pointer_left + 1
        if current_len > max_len: #this should be hear for all char unique case 
            max_len = current_len     
        hash_map[array[pointer_right]] = pointer_right

    return max_len



""" 

WARM UP - monotonic stack 

stack 
output 
input 

if current value less than stack value append to stack
if current value greater than stack value then update output and pop the stack


 """
def next_great_element_08102026(l: list[int]) -> list[int]:
    output = -1 * len(l)
    stack = list()
    for i in range(len(l)):
        while len(stack) > 0 and l[i] > l[stack[-1]]:
            popped_i = stack.pop()
            output[popped_i] = l[i]
        stack.append(i)




""" REVIEW prefix sum / hash map; number of times the any len subarray equals key

I think I got the abstraction how I think on it, 

the previous hash map pattern with complement got me thinking algebraically 
and programmatically the same time,

you assign the value but at the same time you approve the equality
so when we say prefix[j] - prefix[i - 1] = k and prefix[i - 1] = prefix[j] - k 

then in program when I do, if prefix_l[j] - k in map and 
after that map[prefix_l[j] = map.get(prefix_l[j], 0) + 1 

I literally state the math behind it that prefix[i-1] = prefix[j] - k 
and this thinking reminded me the hash map basic pattern 
and the mathematical part of it 


"""

def times_subarray_sum_equal_k(l: list[int], k: int) -> int:
    map = dict()
    map[0] = 1
    total_counts = 0
    prefix_l = list()
    prefix_l.append[l[0]]
    
    for i in range(1, len(l)):
        prefix_l.append(prefix_l[i - 1] + l[i])

    for j in range(len(l)): 
        if prefix_l[j] - k in map:
            total_counts += map[prefix_l[j] - k]
        map[prefix_l[j]] = map.get(prefix_l[j], 0) + 1
    
    return total_counts





""" WARM UP  09/10/2026"""
def total_sum_equal_k_count(array: list[int], k: int) -> int:
    map = {0: 1}
    prefix_sum = [array[0]]
    for i in range(1,len(array)):
        prefix_sum.append(prefix_sum[i - 1] + array[i])
    count = 0
    for i in range(len(array)):
        c = prefix_sum[i] - k
        if c in map:
            count += map[c]
        map[prefix_sum[i]] += map.get(prefix_sum[i], 0) + 1
    return count


""" REVIEW  """

"""
What happens to the elements currently sitting inside the monotonic 
stack when you encounter a number larger than them? 


my answer:
you pop the indexes of the stack and insert them 
into resulting array that before was all full with -1s"""



def next_smaller_element(l: list[int]) -> int:
    result = [-1] * len(l)
    stack = list()
    for i in range(len(l)):
        while len(stack) > 0 and l[i] < l[stack[-1]]:
            popped_idx = stack.pop()
            result[popped_idx] = l[i]
        stack.append(i)
    return result



""" MASTERY CHALLENGE  """

#O(n^2)
def reverse_string_(s:str) -> str:
    l = list(s) 
    def helper(i: int):
        if i == len(l) - 1:
            return l[i]
        else:
            return helper(i + 1) + l[i]
    print(helper(0))

#O(n)
def reverse_string__(s:str) -> str:
    l = list(s)
    acc = list()                                  
    def helper(i: int):
        if i == len(l):
            return 
        helper(i + 1)
        acc.append(l[i])
    helper(0)
    return "".join(acc)
print(reverse_string__("abc"))



""" GLOBAL REVIEW """


#prefix sum // hash map // subarray seeker 
def subarray_seeker_k(l:list[int], k: int) -> int:
    map = {0: 1}
    prefix_sum = [l[0]]
    total = 0
    for i in range(1,len(l)):
        prefix_sum.append(prefix_sum[i - 1] + l[i])
    for i in range(len(prefix_sum)):
        c = prefix_sum[i] - k
        if c in map:
            total += map[c]
        map[prefix_sum[i]] = map.get(prefix_sum[i],0) + 1
    return total 


#monotonic stack(increasing) // temperature rise 
def temperature_rise(l: list[int]) -> list[int]:
    stack = list()
    output = [0] * len(l)
    for i in range(len(l)):
        while len(stack) > 0 and l[i] > l[stack[-1]]:
            popped_idx = stack.pop()
            output[popped_idx] = i - popped_idx
        stack.append(i)
    return output


# hash map 
def the_duplicate_window(l: list[int], k: int) -> int:
    d = dict()
    for i, v in enumerate(l):
        if v in d and i - d[v]  <= k:
            return True 
        d[v] = i
    return False




""" WARM UP - duplicate window// hash map """


def dup_window_12102026(l: list[int], k: int) -> bool:
    dct = dict()
    for i in range(len(l)):
        if l[i] in dct and abs(dct[l[i]] - l[i]) <= k:
            return True 
        dct[l[i]] = i 
    return False 



""" REVIEW - fixed size sliding window  """

def subarray_average(l:list[int], k: int) -> float:
    max_sum: float = sum(l[:k])
    cur_sum: float = max_sum
    for right in range(1,len(l)):
        cur_sum += l[right] - l[right - k] 
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum


""" NEW MASTERY - linked links  """

class Node:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next  

def reverse(head: Node) -> Node: 
    curr = head 
    prev = None 
    while(curr):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev 

tail = Node(3)
node2 = Node(2, next=tail)
head = Node(1, next=node2)





""" WARM UP linked list reverse 151026"""


class Node151026:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 

"""
head 
1 -> 2 -> 3 - > None 
    curr
prev
   next_node
 """
def reverse_linked_list_151026(head: Node151026) -> Node151026:
    curr = head 
    prev = None
    while(curr):
        next_node = curr.next
        curr.next = prev
        curr = next_node
    return prev 


""" REVIEW linked list traverse"""

#version with print
def print_linked_list_151026(head:Node151026) -> str:
    curr = head 
    tail = None
    while(curr):
        val = curr.val
        print(val, "->", end="")
        curr = curr.next
    print(tail, "", end="")

#version with list 
def print_linked_list_151026_2(head:Node151026) -> str:
    curr = head 
    tail = None
    buffer = list()
    while(curr):
        buffer.append(str(curr.val))
        curr = curr.next
    buffer.append(str(tail))
    return "->".join(buffer)


""" NEW MASTERY middle of the linked list // ahh okay I got it its fast slow pointer pattern
1 -> 2 -> 3 -> 4 -> 5 -> None
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None 
slow
fast       
    slow
        fast
        slow  
                   fast
            slow
                                                                     
"""

def middle_of_linked_list_101526(head: Node151026) -> Node151026: 
    slow = head  
    fast = head
    while(fast and fast.next):
        slow = slow.next 
        fast = fast.next.next
    return slow 


""" GLOBAL REVIEW """

def binary_search_20_10_2026(l: list[int], k: int):
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if(l[mid] == k):
            return mid
        elif (k < l[mid]):
            right -= mid - 1
            """ INCORRECT 
                should be right = mid - 1 """
        else:
            left += mid + 1
            """ INCORRECT 
                should be left = mid + 1 """


def two_sum_20_10_2026(l: list[int], t: int) -> list[int]:
    hash_map = dict()
    for i in range(len(l)):
        c = l[i] - t 
        """ INCORRECT it should 
            a + c = t 
            c = t - a  where a is l[i]""" 
        if c in hash_map:
            return (i, l[c])
        """ INCORRECT it should
            hash_map[c] """ 
        hash_map[l[i]] = i
    return None 

def interval_between_min_max(l: list[int]) -> list[int]:
    a = l.index(max(l))
    b = l.index(min(l))
    return l[min(a,b) - 1:max(a,b)]

class Node_20_10_2026:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 

def reverse_linked_list_20_10_2026(head: Node_20_10_2026) -> Node_20_10_2026:
    curr = head 
    prev = None 
    while(curr):
        next_val = curr.next
        curr.next = prev
        prev = next_val 
        """ INCORRECT
        prev = curr     shifts prev forward 
        curr = next_val shifts curr forward"""
    return prev 

            
def prefix_sum_20_10_2026(l: list[int]) -> list[int]:
    prefix_sum = list()
    prefix_sum.append(l[0])
    for i in range(1,len(l)):
        prefix_sum.append(prefix_sum[i - 1] + l[i])
    """ INCORRECT 
        return prefix_sum """

def recursion_reverse_string_20_10_2026(s: str) -> str:
    l = list(s)
    buf = list()
    def helper(i: int):
        if i == len(l) - 1:
            return l[i] #INCORRECT return 
        helper(i + 1)
        return buf.append(l[i]) #INCORRECT you do not return anything 
    return "".join(helper(0)) #INCORRECT you join the buf

    

def running_state_20_10_2026(l: list[int]):
    min_price = float('inf')
    max_profit = float('-inf')
    for i,v in enumerate(l):
        if v < min_price:
            min_price = v 
        curr_profit = v - min_price
        if curr_profit > max_profit:
            max_profit = curr_profit
    return max_profit  


def monotonic_stack_20_10_2026(l: list[int]) -> list[int]:
    stack = list()
    output = [-1] * len(l)
    for i in range(len(l)):
        while len(stack) > 0 and l[i] > l[stack[i]]: 
            """ INCORRECT l[stack[-1]] the top of the stack not i of the stack"""
            popped_idx = stack.pop()
            output[popped_idx] = l[i] 
        stack.append(i)
    return output

def valid_palindrome_20_10_2026(s: str) -> bool:
    l = list(s)
    left = 0
    right = len(l) - 1
    while left <= right:
        while not l[left].isalpha() and left <= right:
            left += 1
        while not l[right].isalpha() and left <= right:
            right -= 1
        if l[left] != l[right]:
            return False 
    """ INCORRECT 
        left += 1
        right -= 1 
        I never advace the loop """
    return True 
 

def sliding_window_20_10_2026(l: list[int],k: int):
    max_sum = sum(l[:k])
    cur_sum = max_sum 
    for i in range(k,len(l)):
        cur_sum += l[i] - l[i - k]
        if cur_sum > max_sum:
            max_sum = cur_sum 
    return max_sum 



