def power_set(input_set):
    if not input_set:
        return [[]]
    
    # 2. Otherwise, create a variable to hold the first element of the input list.
    first = input_set[0]
    
    # 3. Recursively call power_set to compute the power set of the rest of the list.
    rest_subsets = power_set(input_set[1:])
    
    # 4. Create a new list to hold the final collection of subsets.
    final_subsets = []
    
    # 5. For each subset returned by the recursive call:
    #    - Create a new subset that includes the first element combined with the current subset.
    #    - Also include the current subset itself.
    for subset in rest_subsets:
        final_subsets.append([first] + subset)
        final_subsets.append(subset)
    
    # 6. Return the final collection of subsets.
    return final_subsets

print(power_set(['a','b','c']))