from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    for key, value in tickets:
        routes[key].append(value)
    routes = {key: sorted(value) for key, value in routes.items()}
    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top not in routes or not routes[top]:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop(0))
    return path[::-1]