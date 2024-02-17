from module.errors.empty_stack_error import EmptyStackError
from module.stack import Stack


if __name__ == "__main__":
    # constructors
    empty_stack = Stack[int]()
    stack_from_list = Stack[int].from_sequence([1, 2, 3, 4, 5, 6, 7])
    print(empty_stack.is_empty)  # True
    print(stack_from_list.is_empty)  # False

    # Push method and in operator
    a_string = "Hello!"
    str_stack = Stack[str]()
    str_stack.push(a_string)
    print(a_string in str_stack)  # True

    # Push and peek
    another_string = "How're you?"
    str_stack.push(another_string)
    print(str_stack.peek())  # "How're you?"

    print(another_string in str_stack)  # Peek doesn't remove the element

    # Len dunder method
    print(len(str_stack))  # How many elements do we have? 2

    # Pop and in operator
    popped_item = str_stack.pop()
    print(popped_item)  # "How're you?"
    print(another_string in str_stack)  # False, because pop removes the item

    # Error prevention methods
    a_stack = Stack[float]()
    a_stack.push(3.14)
    peeked_item = a_stack.peek()
    number = a_stack.pop()
    print(peeked_item)  # 3.14
    print(number)  # 3.14

    print(f"The stack has {len(a_stack)} element(s)")  # 0
    try:
        a_stack.pop()
    except EmptyStackError as error:
        print(f"There was an error: {error.message}")

    print(f"The stack has {len(a_stack)} element(s)")  # 0
    
    # but, what about try to pop but without error?
    maybe_a_number = a_stack.try_pop()

    print(maybe_a_number)  # None and no exception raised :-)

    print(f"The stack has {len(a_stack)} element(s)")  # 0

    try:
        a_stack.peek()
    except EmptyStackError as error:
        print(f"There was an error: {error.message}")

    # let's peek and don't have error raising?
    maybe_peeked_item = a_stack.try_peek()

    print(maybe_peeked_item)  # None and no exception raised :-)
