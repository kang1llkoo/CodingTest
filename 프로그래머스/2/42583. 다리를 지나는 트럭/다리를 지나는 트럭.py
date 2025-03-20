from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque()
    curr_weight = 0
    
    for truck in truck_weights:
        while True:
            time += 1
            
            if bridge and time - bridge[0][1] >= bridge_length:
                t, _ = bridge.popleft()
                curr_weight -= t
                
            if curr_weight + truck <= weight and len(bridge) < bridge_length:
                bridge.append((truck, time))
                curr_weight += truck
                break
                
    return time + bridge_length