import sys

# part 1
fuel = lambda m: int(m/3)-2
lines = sys.stdin.readlines()
f = sum([fuel(int(line.strip())) for line in lines])
print(f)

# part 2
def fuel_rec(m):
    ans = int(m/3)-2
    if ans > 0:
        return ans + fuel_rec(ans)
    else:
        return 0

f = sum([fuel_rec(int(line.strip())) for line in lines])
print(f)