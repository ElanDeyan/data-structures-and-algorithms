from module.stack import Stack


if __name__ == "__main__":
    # constructors
    empty_stack = Stack[int]()
    stack_from_list = Stack[int].from_sequence([1, 2, 3, 4, 5, 6, 7])

    print(empty_stack.is_empty)  # True
    print(stack_from_list.is_empty)  # False
