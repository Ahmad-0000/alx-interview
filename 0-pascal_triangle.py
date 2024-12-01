"""
A function to print the Pascal Triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []
    old = []
    all_lists = []
    i = 0
    while i < n:
        new = []
        j = 0
        while j < len(old):
            if j > 0:
                new.append(old[j] + old[j - 1])
            else:
                new.append(1)
            j += 1
        new.append(1)
        old = new
        all_lists.append(new)
        i += 1
    return all_lists
