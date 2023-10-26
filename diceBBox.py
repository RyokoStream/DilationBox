import random

# 6面体サイコロαを振る
alpha_result = random.randint(1, 6)

if alpha_result % 2 == 1:
    # αの目が奇数なら10面体サイコロβを振る
    beta_result = random.randint(0, 9)
    a = beta_result
else:
    # αの目が偶数なら8面体サイコロγを振る
    gamma_result = random.randint(1, 8)
    a = gamma_result

# 10面体サイコロδを振る
delta_result = random.randint(0, 9)
b = a * delta_result

# cが40を超えている場合の処理
if b > 40:
    d = b % 40
else:
    d = b

# 6面体サイコロεを振る
epsilon_result = random.randint(1, 6)

if epsilon_result % 2 == 1:
    d_color = "赤"
else:
    d_color = "黄色"

print(f"αの目: {alpha_result}")
print(f"βまたはγの結果: {a}")
print(f"δの目: {delta_result}")
print(f"計算結果 c: {b}")
print(f"d: {d}")
print(f"εの目: {epsilon_result}")
print(f"dの色: {d_color}")
