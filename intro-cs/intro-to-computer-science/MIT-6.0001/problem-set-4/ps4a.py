# Problem Set 4A
# Name: eurodollarclub
# Collaborators: None
# Time Spent: 17 hours

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string
    sequence (string): an arbitrary string to permute. Assume that it is a non-empty string.  
    Returns: a list of all permutations of sequence

    strategy:
    sequence len == 1 => 0 
    sequence len == 2 => 0 + 1, 1 + 0
    sequence len > 2 => 3 + 0 + 1, 0 + 3 + 1, 0 + 1 + 3...
    '''
    
    assert len(sequence) > 0, 'Len of the sequence must be greater then zero'
    permutations_list = list()
    init_list = list()
    if len(sequence) == 1:
        return [sequence]
    else:
        lower_scope_or_base_case = get_permutations(sequence[:-1])
        upper_scope = [sequence]
        init_list = lower_scope_or_base_case + upper_scope
        if len(init_list) == 1:
            return init_list
        elif len(init_list) == 2:
            for i in range(len(init_list)):
                if len(init_list[i]) == 2:
                    permutations_list = permutations_list + [init_list[i]]
                    permutations_list = permutations_list + [init_list[i][1:] + init_list[i][:-1]]
        elif len(init_list) > 2:
            permutation_letter = init_list[len(init_list)-1][len(sequence)-1]
            permutations_list = init_list.copy()
            permutations_list.pop()
            temporary_permutations_list = list()
            sequence_none_list = [None] * len(init_list[len(init_list)-1])
            while len(permutations_list) != 0:
                permutation = permutations_list.pop()
                for i in range(len(sequence_none_list)):
                    sequence_none_list[i] = permutation_letter
                    z = 0
                    for j in range(len(sequence_none_list)):  
                        if sequence_none_list[j] == None:
                            sequence_none_list[j] = permutation[z]
                            z += 1  
                        if len(sequence_none_list) - 1 == j:
                            temporary_permutations_list.append("".join(sequence_none_list))
                            sequence_none_list = [None] * len(sequence)  
            permutations_list = list(temporary_permutations_list)
    return permutations_list

if __name__ == '__main__':
    print("Input: ", 'ab')
    print("Expected Output: ", ['ab', 'ba'])
    print("Actual Output: ", get_permutations("ab"))

    print("Input: ", 'a')
    print("Expected Output: ", ['a'])
    print("Actual Output: ", get_permutations("a"))

    print("Input: ", 'abc')
    print("Expected Output: ", ['abc', 'acb', 'cab', 'bac', 'bca', 'cba'])
    print("Actual Output: ", get_permutations('abc'))
