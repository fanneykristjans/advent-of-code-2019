import sys

inp = sys.stdin.readline().strip().split(',')
inp = [int(x) for x in inp]

def part_1(f, pos1, pos2):
    f[1] = pos1
    f[2] = pos2

    n = 0
    while n+3 < len(f):
        if f[n] is 1: # ADD
            f[f[n+3]] = f[f[n+1]] + f[f[n+2]]
        elif f[n] is 2: # MULTIPLY
            f[f[n+3]] = f[f[n+1]] * f[f[n+2]]
        else: # HALT
            return f
        n += 4
    return f

# part 1:
print(part_1(inp.copy(), 12,2)[0])

# part 2:
for i in range(0,100):
    for j in range(0,100):
        a = inp.copy()
        ans = part_1(a,i,j)
        if ans[0] == 19690720:
            print(f"i={i}, j={j}, 100*i+j={100*i+j}")
            exit()