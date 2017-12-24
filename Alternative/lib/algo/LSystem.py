# Duration rules
# 1/2 -> [1/4, 1/4]
# 1/4 -> [1/4, 1/3, 1/8]
# 1/8 -> [1/16, 1/8, 1/8]
# 1/16 -> [1/2, 1/6, 1/8]
# 1/3 -> [1/2, 1/4, 1/3]
# 1/6 -> [1/3, 1/4, 1/8]

def flatten_nested_list(nested_list):
    flat_list = []
    fringe = [nested_list]

    while len(fringe) > 0:
        node = fringe.pop(0)
        # ノードがリストであれば子要素をフリンジに追加
        # リストでなければそのままフラットリストに追加
        if isinstance(node, list):
            fringe = node + fringe
        else:
            flat_list.append(node)

    return flat_list


def apply_rules(num):
    num_list = []

    if num == 1/2:
        num_list = [1/4, 1/4]
    elif num == 1/4:
        num_list = [1/4, 1/3, 1/8]
    elif num == 1/8:
        num_list = [1/16, 1/8, 1/8]
    elif num == 1/16:
        num_list = [1/2, 1/6, 1/8]
    elif num == 1/3:
        num_list = [1/2, 1/4, 1.3]
    elif num == 1/6:
        num_list = [1/3, 1/4, 1/8]
    else:
        num_list = []

    return num_list


def create_Lsystem(*num_lists):
    final_list = []
    for list in num_lists:
        flat_num_list = flatten_nested_list(list)

        for num in flat_num_list:
            final_list.append(apply_rules(num))

    return final_list


def get_Lsystem(messages, num_iters, initial_list):
    durations = []

    for i in range(num_iters):
        if i == 0:
            durations = create_Lsystem(initial_list)
        else:
            durations = create_Lsystem(*durations)

    print("{0} : {1}".format(messages, durations))
    return durations
