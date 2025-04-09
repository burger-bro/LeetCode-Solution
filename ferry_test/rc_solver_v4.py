from collections import deque
import itertools

def generate_moves(state, objects, rowers, boat_capacity):
    n = len(objects)
    current_boat_side = state[-1]
    current_shore = [i for i in range(n) if state[i] == current_boat_side]
    subsets = []
    # 生成所有可能的子集
    for k in range(1, boat_capacity + 1):
        for subset in itertools.combinations(current_shore, k):
            if any(objects[idx] in rowers for idx in subset):
                subsets.append(subset)
    # 生成新状态
    moves = []
    for subset in subsets:
        new_state = list(state)
        for idx in subset:
            new_state[idx] = 1 - new_state[idx]  # 翻转对象位置
        new_state[-1] = 1 - new_state[-1]       # 翻转船的位置
        moves.append(tuple(new_state))
    return moves

def is_valid(state, conditions, objects):
    n = len(objects)
    # 检查两岸的合法性
    for side in [0, 1]:
        shore_objects = [i for i in range(n) if state[i] == side]
        for condition in conditions:
            # 检查所有对象是否在同一岸
            obj_indices = [objects.index(obj) for obj in condition['objects']]
            if all(state[idx] == side for idx in obj_indices):
                # 检查该岸是否有监管者
                unless_indices = [objects.index(obj) for obj in condition['unless']]
                if not any(state[idx] == side for idx in unless_indices):
                    return False  # 触发冲突条件
    # 检查船上的合法性
    boat_objects = [i for i in range(n) if state[i] != state[-1]]
    for condition in conditions:
        # 检查所有对象是否在船上
        obj_indices = [objects.index(obj) for obj in condition['objects']]
        if all(state[idx] != state[-1] for idx in obj_indices):
            # 检查船上是否有监管者
            unless_indices = [objects.index(obj) for obj in condition['unless']]
            if not any(state[idx] != state[-1] for idx in unless_indices):
                return False  # 触发冲突条件
    return True

def solve(objects, rowers, boat_capacity, conditions):
    n = len(objects)
    initial_state = tuple([0] * n + [0])  # 初始状态
    target_state = tuple([1] * n + [1])   # 目标状态

    queue = deque([(initial_state, [])])
    visited = set()  # 全局记录已访问状态
    solutions = []

    while queue:
        current_state, path = queue.popleft()
        if current_state == target_state:
            solutions.append(path)
            continue
        for new_state in generate_moves(current_state, objects, rowers, boat_capacity):
            if is_valid(new_state, conditions, objects) and new_state not in visited:
                visited.add(new_state)  # 记录已访问状态
                new_path = path + [(new_state, describe_move(current_state, new_state, objects))]
                queue.append((new_state, new_path))
    return solutions

def describe_move(old_state, new_state, objects):
    moved = [obj for i, obj in enumerate(objects) if old_state[i] != new_state[i]]
    direction = 'right' if new_state[-1] == 1 else 'left'
    return f"bring {', '.join(moved)} to {direction}"

# 输入参数
objects = ['mother', 'father', 'brother', 'sister', 'stranger']
rowers = ['mother', 'father', 'brother', 'stranger']
boat_capacity = 2
conditions = [
    {'objects': ['mother', 'father'], 'unless': ['brother', 'sister', 'stranger']},
    {'objects': ['mother', 'brother'], 'unless': ['father', 'sister', 'stranger']},
    {'objects': ['mother', 'stranger'], 'unless': ['brother', 'sister', 'father']},
    {'objects': ['sister', 'brother'], 'unless': ['mother', 'father', 'stranger']},
    {'objects': ['sister', 'father'], 'unless': ['mother', 'brother', 'stranger']},
    {'objects': ['brother', 'stranger'], 'unless': ['sister', 'brother', 'father']},
]

# 求解
solutions = solve(objects, rowers, boat_capacity, conditions)

# 输出结果
for i, path in enumerate(solutions):
    print(f"Solutions {i + 1}:")
    for step in path:
        print(step[1])
    print()

