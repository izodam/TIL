# 조합
arr = ['A', 'B', 'C', 'D', 'E']
path = []

n = 3
def run(lev, start):
    if lev == n:
        print(path)
        return
    for i in range(start, 5):
        path.append(arr[i])
        run(lev+1, i+1)
        path.pop()

run(0,0)




# 중복을 허용한 조합
path = []
n = 3

def run1(lev, start):
    if lev == n:
        print(path)
        return
    for i in range(start, 7):
        path.append(i)
        run1(lev + 1, i)
        path.pop()
run1(0,1)