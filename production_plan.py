from pulp import LpProblem, LpVariable, LpMaximize, lpSum, value

# ====== 生产计划 LP（最大化利润）======

# 产品A利润=40元，B利润=30元
# 产品A需要1工人+2机器；产品B需要2工人+1机器
# 总工人最多10人，总机器最多12台

profit = [40, 30] # 产品A、B的利润
workers = [1, 2] # 每个产品需要的工人
machines = [2, 1] # 每个产品需要的机器

prob = LpProblem("ProductionPlan", LpMaximize)

# 决策变量：生产多少产品A、多少产品B
x = [LpVariable(f"x{i}", lowBound=0, cat="Continuous") for i in range(2)]

# 目标函数：最大化利润
prob += lpSum([profit[i] * x[i] for i in range(2)]), "TotalProfit"

# 约束：工人限制
prob += lpSum([workers[i] * x[i] for i in range(2)]) <= 10, "WorkerLimit"

# 约束：机器限制
prob += lpSum([machines[i] * x[i] for i in range(2)]) <= 12, "MachineLimit"

# 求解
prob.solve()

# 输出结果
print("状态:", prob.status)
print("最优利润:", value(prob.objective))
for i in range(2):
 print(f"产品{chr(65+i)}生产量:", value(x[i]))
