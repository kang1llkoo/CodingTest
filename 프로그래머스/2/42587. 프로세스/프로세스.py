def solution(priorities, location):
    queue = list(enumerate(priorities))
    order = 0
    while queue:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            order += 1
            if cur[0] == location:
                return order