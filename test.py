def check_increasing_sequences(arr):
    increasing_sequences = []
    current_sequence = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            current_sequence.append(arr[i])
        else:
            increasing_sequences.append(current_sequence)
            current_sequence = [arr[i]]

    increasing_sequences.append(current_sequence)

    return increasing_sequences

def is_increasing_and_complete(subarray):
    
    expected_sequence = set(range(1, len(subarray) + 1))
    print(1111, len(subarray) == len(expected_sequence), 1111, set(subarray).issubset(expected_sequence))
    
    return len(subarray) == len(expected_sequence) and set(subarray).issubset(expected_sequence)


def check_arrays(arrays):
    
    return all(is_increasing_and_complete(subarray) for subarray in arrays)

my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 6, 7, 8, 9, 10]

data = check_increasing_sequences(my_array)
result = check_arrays(data)
print(result)
