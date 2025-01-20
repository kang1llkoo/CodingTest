def solution(num_list):
    total_count = 0
    for i in range(len(num_list)):
        count = 0 
        while num_list[i] != 1: 
            if num_list[i] % 2 == 0:  
                num_list[i] //= 2 
            else:  
                num_list[i] = (num_list[i] - 1) // 2  
            count += 1  
        total_count += count  
    return total_count
