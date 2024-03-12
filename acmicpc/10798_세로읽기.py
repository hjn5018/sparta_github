# import sys

# sys.stdin = open('input.txt')

# rows = []
# for _ in range(5):
#     row = sys.stdin.readline()
#     rows.append(row)

# max_len = 0
# for i in range(5):
#     if len(rows[i]) > max_len:
#         max_len = len(rows[i])

# for i in range(5):
#     for j in range(max_len):
#         print(rows[j][i],sep='',end='')
# IndexError: string index out of range
# =============================================
# import sys

# sys.stdin = open('input.txt')

# rows = []
# for _ in range(5):
#     row = sys.stdin.readline()
#     rows.append(row)

# max_len = 0
# for i in range(5):
#     if len(rows[i]) > max_len:
#         max_len = len(rows[i])

# for i in range(5):
#     for j in range(max_len):
#         print(rows[j][i],sep='',end='')
# IndexError: list index out of range
# ==========================================
# import sys

# sys.stdin = open('input.txt')

# rows = []
# for _ in range(5):
#     row = sys.stdin.readline()
#     rows.append(row)

# print(rows)
# ['ABCDE\n', 'abcde\n', '01234\n', 'FGHIJ\n', 'fghij']
# =======================================
# import sys

# sys.stdin = open('input.txt')

# rows = []
# for _ in range(5):
#     row = sys.stdin.readline().rstrip('\n')
#     rows.append(row)

# print(rows)
# ['ABCDE', 'abcde', '01234', 'FGHIJ', 'fghij']
# ====================================
# import sys

# sys.stdin = open('input.txt')

# rows = []
# for _ in range(5):
#     row = sys.stdin.readline().rstrip('\n')
#     rows.append(row)

# max_len = 0
# for i in range(5):
#     if len(rows[i]) > max_len:
#         max_len = len(rows[i])

# for i in range(5):
#     for j in range(max_len):
#         print(rows[j][i],sep='',end='')
# Aa0FfBb1GgCc2HhDd3IiEe4Jj
# 런타임 에러(FileNotFoundError)
# ===================================================
# import sys
# sys.stdin = open('input.txt')
# rows = []
# for _ in range(5):
#     row = sys.stdin.readline().rstrip('\n')
#     rows.append(row)

# max_len = 0
# for i in range(5):
#     if len(rows[i]) > max_len:
#         max_len = len(rows[i])

# for i in range(5):
#     for j in range(max_len):
#         print(rows[j][i],sep='',end='')
# 런타임 에러 (IndexError)
# Aa0FfBb1GgCc2HhDd3IiEe4Jj
# Aa0FfBb1GgCc2HhDd3IiEe4Jj
# Aa0aPAf985Bz1EhCz2W3D1gkD6x
# IndexError: list index out of range
# ==============================================
import sys
sys.stdin = open('input.txt')
rows = []
for _ in range(5):
    row = sys.stdin.readline().rstrip('\n')
    rows.append(row)

max_len = 0
for i in range(5):
    if len(rows[i]) > max_len:
        max_len = len(rows[i])

# for i in range(5):
#     for j in range(max_len):
#         try:
#             print(rows[j][i],sep='',end='')
#         except IndexError:
#             # continue
#             pass
for i in range(5):
    for j in range(max_len):
        # print(rows[j][i],sep='',end='')
        # print(f"{rows[j+1][i] if rows[j][i] is None else rows[j][i]}" ,sep='',end='')
        if rows[j][i] is None:
# IndexError: list index out of range
            char = rows[j+1][i]
        else:
            char = rows[j][i]
        print(char, sep='',end='')

# Aa0aPAf985Bz1EhCz2W3D1gkD6x
# Aa0aPAf985Bz1EhCz2W3D1gk