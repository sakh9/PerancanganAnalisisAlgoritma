def climbStairs(n):

    f = [0] * (n + 1)
    f[1] = 1
    f[2] = 2

    for i in range(3, n + 1):
        
        f[i] = f[i - 1] + f[i - 2]
        print(f"Iterasi i = {i} → f[{i}] = f[{i-1}] + f[{i-2}]")
        print(f)
    return f[n]

# input
n = int(input("Masukkan jumlah tangga: "))   
print("Jumlah cara untuk mendaki", n, "tangga adalah:", climbStairs(n))
