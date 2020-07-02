# Approach 1
def find_paths(root, target):
    if root is None:
        return 0

    root_paths = find_paths_with_sum(root, target, 0)
    left_paths = find_paths(root.left, target)
    right_paths = find_paths(root.right, target)

    return root_paths + left_paths + right_paths


def find_paths_with_sum(root, target, current_sum):
    if root is None:
        return 0
    total_paths = 0
    current_sum += root.data
    if current_sum == target:
        total_paths += 1

    total_paths += find_paths_with_sum(root.left, target, current_sum)
    total_paths += find_paths_with_sum(root.right, target, current_sum)
    return total_paths


# Approach 2
def count_paths(root, target):
    return count_paths_with_sum(root, target, 0, {})


def count_paths_with_sum(root, target, running_sum, sum_dict):
    if root is None:
        return 0
    running_sum += root.data
    remaining = running_sum - target
    total_paths = sum_dict.get(remaining, 0)

    if running_sum in sum_dict:
        sum_dict[running_sum] += 1
    else:
        sum_dict[running_sum] = 1
    total_paths += count_paths_with_sum(root.left, target, running_sum, sum_dict)
    total_paths += count_paths_with_sum(root.right, target, running_sum, sum_dict)
    if running_sum in sum_dict:
        sum_dict[running_sum] -= 1
    return total_paths

