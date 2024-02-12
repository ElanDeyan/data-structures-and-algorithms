from stack import Stack

import unittest

from state_error import EmptyStackError


class TestStack(unittest.TestCase):
    def test_isinstance(self):
        maybe_stack = Stack[str]()

        maybe_stack_from_sequence = Stack[int].from_sequence([1, 2, 3, 4, 5])

        self.assertIsInstance(maybe_stack, Stack)

        self.assertIsInstance(maybe_stack_from_sequence, Stack)

    def test_len(self):
        empty_stack = Stack[int]()

        self.assertEqual(len(empty_stack), 0)

        stack_from_sequence = Stack[int].from_sequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        self.assertEqual(len(stack_from_sequence), 10)

    def test_contains(self):
        stack = Stack[float]()

        stack.push(1.0)

        self.assertIn(1.0, stack)

        another = Stack[str].from_sequence(["oi", "tudo", "bem", "?"])

        self.assertIn("oi", another)

    def test_emptiness(self):
        empty = Stack[int]()

        self.assertEqual(len(empty), 0)

        self.assertTrue(empty.is_empty)

        another_stack = Stack[str]()

        another_stack.push("oieeeee")
        another_stack.push("how're you?")

        self.assertFalse(another_stack.is_empty)

        from_sequence = Stack[int].from_sequence([1, 2, 3, 4, 5])

        self.assertFalse(from_sequence.is_empty)

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

        poped_item = stack.try_pop()

        self.assertEqual(poped_item, 1)

        maybe_int = stack.try_pop()

        self.assertIsNone(maybe_int)

    def test_peek(self):
        stack = Stack[int].from_sequence([3, 4, 5, 6, 7, 8, 9])

        self.assertEqual(stack.peek(), 9)

        empty = Stack[bool]()

        self.assertRaises(EmptyStackError, empty.peek)

    def test_try_peek(self):
        stack = Stack[bool]()

        stack.push(True)

        self.assertEqual(stack.try_peek(), True)

        stack.pop()

        self.assertIsNone(stack.try_peek())

    def test_stack_iterator(self):
        from_zero_to_nine = [i for i in range(10)]
        stack = Stack[int].from_sequence(from_zero_to_nine)
        from_nine_to_zero = reversed(from_zero_to_nine)

        self.assertListEqual(list(stack.__iter__()), list(from_nine_to_zero))

    def test_clear(self):
        stack = Stack[int].from_sequence([1,2,3,4,5])

        self.assertEqual(len(stack), 5)

        stack.clear()

        self.assertEqual(len(stack), 0)


if __name__ == "__main__":
    unittest.main()
