colors = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

input_colors = [input().strip() for _ in range(3)]

value = (colors[input_colors[0]] * 10 + colors[input_colors[1]]) * (10 ** colors[input_colors[2]])

print(value)