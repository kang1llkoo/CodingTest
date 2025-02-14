def solution(triangle):
    pre = triangle[0]
    for step in triangle[1:]:
        for idx in range(len(step)):
            if idx == 0:
                step[idx] += pre[idx]
            elif idx == len(step)-1:
                step[idx] += pre[-1]
            else:
                step[idx] += max(pre[idx-1], pre[idx])
        pre = step
    return max(step)