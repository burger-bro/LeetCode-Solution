"""
A: 0.9A 0.1B
B: 0.7B 0.3A

1:
A50 B50
2:
A=0.9*50 + 0.3*50 = 60
B=0.1*50 + 0.7*50 = 40
"""

init_A, init_B = 0, 100
cur_A, cur_B = init_A, init_B
for _ in range(50):
    # nxt_A = 0.9*cur_A + 0.3*cur_B
    # nxt_B = 0.1*cur_A + 0.7*cur_B

    # nxt_A = cur_A + 0.3*cur_B
    # nxt_B = 0.7*cur_B

    nxt_A = 0.9*cur_A + 0.3*cur_B
    nxt_B = 0.1*cur_A + 0.7*cur_B
    cur_A, cur_B = nxt_A, nxt_B
    print(cur_A, cur_B)

