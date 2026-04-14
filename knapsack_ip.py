from pulp import LpProblem, LpVariable, LpMaximize, lpSum, LpBinary

# ====== 0-1背包 IP（选哪些物品使利润最大）======

items = ["物品A", "物品B", "物品C", "物品D"]
profit = [40, 60, 50, 30] # 各物品利润
weight = [5, 6, 4, 3] # 各物品重量
capacity = 10 # 背包容量

prob = LpProblem("KnapsackIP", LpMaximize)

# 决策变量：选或不选（0-1变量）
x = [LpVariable(f"x{i}", cat=LpBinary) for i in range(len(items))]

# 目标函数：最大化总利润
prob += lpSum([profit[i] * x[i] for i in range(len(items))]), "TotalProfit"

# 约束：总重量不能超过容量
prob += lpSum([weight[i] * x[i] for i in range(len(items))]) <= capacity, "WeightLimit"

# 求解
prob.solve()

print("状态:", prob.status)
print("最大利润:", value(prob.objective))
print("选中的物品：")
for i in range(len(items)):
 if value(x[i]) == 1:
 print(f" {items[i]}（利润={profit[i]}，重量={weight[i]}）")
