P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    inp = input()
    if inp[0] == "0":
        break
    K, S = inp.split()
    K = int(K)
    result = ""
    for i in S:
        result += P[(P.find(i) + K) % 28]
    print(result[::-1])

