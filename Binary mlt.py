#multiply_binary : (listof (anyof 0 1)) (listof (anyof 0 1)) -> (listof (listof (anyof 0 1)))
#Requires:
  #A and B are non-empty
  #A and B have no leading zeros
def multiply_binary(A, B):
    A.reverse()
    B.reverse()
    r = (len(B) + len(A)) * [0]
    i_A = 0
    i_B = 0
    for i in A:
        for j in B:
            r[i_A + i_B] = r[i_A + i_B] + i * j;
            i_B += 1
        i_B = 0
        i_A += 1
    index = 0
    for j in r:
        if j // 2 != 0:
            r[index + 1] = r[index + 1] + r[index] // 2
        r[index] = r[index] % 2
        index += 1 
    if r == len(r) * [0]:
        r = [0]
    elif r[-1] == 0:
        r = r[:-1]
        r.reverse()
    else:
        r.reverse()
    return r
    