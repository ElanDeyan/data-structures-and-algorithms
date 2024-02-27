from module.stack import Stack

import unittest

from module.errors.empty_stack_error import EmptyStackError


class TestStack(unittest.TestCase):
    def test_isinstance(self):
        maybe_stack = Stack[str]()

        maybe_empty_stack = Stack[int].empty()

        maybe_stack_from_sequence = Stack[int].from_sequence([1, 2, 3, 4, 5])

        self.assertIsInstance(maybe_empty_stack, Stack)

        self.assertIsInstance(maybe_stack, Stack)

        self.assertNotIsInstance([1, 2, 3, 4, 5], Stack)

        self.assertIsInstance(maybe_stack_from_sequence, Stack)

    def test_len(self):
        empty_stack = Stack[int]()

        self.assertEqual(len(empty_stack), 0)

        another_empty_stack = Stack[int].empty()

        self.assertEqual(len(another_empty_stack), 0)

        stack_from_sequence = Stack[int].from_sequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        self.assertGreater(len(stack_from_sequence), 0)

        self.assertEqual(len(stack_from_sequence), 10)

        # stack_from_sequence.pop_n(5)

        # self.assertEqual(len(stack_from_sequence), 5)

    def test_contains(self):
        stack = Stack[float]()

        stack.push(1.0)

        self.assertIn(1.0, stack)

        self.assertNotIn(5.0, stack)

        another = Stack[str].from_sequence(["oi", "tudo", "bem", "?"])

        self.assertIn("oi", another)

        self.assertNotIn("am i here?", another)

    def test_emptiness(self):
        empty = Stack[int]()

        self.assertEqual(len(empty), 0)

        self.assertTrue(empty.is_empty)
        self.assertFalse(empty.is_not_empty)

        one_more_empty = Stack[int].empty()

        self.assertTrue(one_more_empty.is_empty)
        self.assertFalse(one_more_empty.is_not_empty)

        another_stack = Stack[str]()

        another_stack.push("oieeeee")
        another_stack.push("how're you?")

        self.assertFalse(another_stack.is_empty)
        self.assertTrue(another_stack.is_not_empty)

        from_sequence = Stack[int].from_sequence([1, 2, 3, 4, 5])

        self.assertFalse(from_sequence.is_empty)
        self.assertTrue(from_sequence.is_not_empty)

    def test_push(self):
        stack = Stack[int]()

        stack.push(5)

        self.assertGreater(len(stack), 0)

        self.assertIn(5, stack)

        stack.push(3)
        self.assertIn(3, stack)

    def test_pop(self):
        stack = Stack[int].from_sequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        poped_item = stack.pop()

        self.assertLess(len(stack), 10)

        self.assertEqual(poped_item, 10)

        another_poped = stack.pop()

        self.assertEqual(another_poped, 9)

        empty = Stack[int]()

        self.assertRaises(EmptyStackError, empty.pop)

    def test_try_pop(self):
        stack = Stack[int].from_sequence([1])

        poped_item = stack.pop_or_none()

        self.assertEqual(poped_item, 1)

        maybe_int = stack.pop_or_none()

        self.assertIsNone(maybe_int)

    def test_peek(self):
        stack = Stack[int].from_sequence([3, 4, 5, 6, 7, 8, 9])

        self.assertEqual(stack.top(), 9)

        empty = Stack[bool]()

        self.assertRaises(EmptyStackError, empty.top)

    def test_try_peek(self):
        stack = Stack[bool]()

        stack.push(True)

        self.assertEqual(stack.top_or_none(), True)

        stack.pop()

        self.assertIsNone(stack.top_or_none())

    def test_stack_iterator(self):
        from_zero_to_nine = [i for i in range(10)]
        stack = Stack[int].from_sequence(from_zero_to_nine)
        from_nine_to_zero = reversed(from_zero_to_nine)

        self.assertListEqual(list(stack.__iter__()), list(from_nine_to_zero))

    def test_clear(self):
        stack = Stack[int].from_sequence([1, 2, 3, 4, 5])

        self.assertEqual(len(stack), 5)

        stack.clear()

        self.assertEqual(len(stack), 0)

    def test_push_all(self):
        my_stack = Stack[float].empty()

        self.assertTrue(my_stack.is_empty)

        numbers = [1.2, 3.5, 5.6, 9.8, 10.9]

        my_stack.push_all(numbers)

        self.assertEqual(len(my_stack), len(numbers))

        for number in numbers:
            self.assertIn(number, my_stack)

    def test_pop_all(self):
        strings = ["hello", "everyone", ":-)"]
        my_stack = Stack[str].from_sequence(strings)

        popped_items = my_stack.pop_all()

        self.assertListEqual(list(popped_items), list(reversed(strings)))

        self.assertTrue(my_stack.is_empty)

        self.assertEqual(len(my_stack), 0)

    def test_pop_n(self):
        nine_nines = [9 for _ in range(9)]

        my_stack = Stack[int].from_sequence(nine_nines)

        NUMBER_OF_ITEMS_TO_POP = 5

        popped_items = my_stack.pop_n(NUMBER_OF_ITEMS_TO_POP)

        NUMBER_OF_ITEMS_REMAINING = len(nine_nines) - NUMBER_OF_ITEMS_TO_POP

        self.assertEqual(len(my_stack), NUMBER_OF_ITEMS_REMAINING)
        self.assertListEqual(
            list(popped_items), [9 for _ in range(NUMBER_OF_ITEMS_TO_POP)]
        )

        self.assertLess(NUMBER_OF_ITEMS_REMAINING, NUMBER_OF_ITEMS_TO_POP)

        self.assertRaises(ValueError, my_stack.pop_n, 10)

    def try_pop_n(self):
        int_tuple = (1, 2, 3, 4, 5, 6)
        my_stack = Stack[int].from_sequence(int_tuple)

        NUMBER_OF_ITEMS_TO_POP = 4

        self.assertLess(NUMBER_OF_ITEMS_TO_POP, len(int_tuple))

        my_stack.pop_n_or_all(NUMBER_OF_ITEMS_TO_POP)

        self.assertGreater(NUMBER_OF_ITEMS_TO_POP, len(my_stack))

        popped_items = list(my_stack.pop_n_or_all(NUMBER_OF_ITEMS_TO_POP))

        self.assertGreater(NUMBER_OF_ITEMS_TO_POP, len(popped_items))


if __name__ == "__main__":
    unittest.main()
