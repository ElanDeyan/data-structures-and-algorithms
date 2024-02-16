import unittest

from queue.queue import Queue


class TestQueue(unittest.TestCase):
    def test_is_instance(self):
        empty_queue = Queue[int]()

        a_sequence = [1,2,3,4,5,6,7]

        filled_queue = Queue[int].from_sequence(a_sequence)

        self.assertIsInstance(empty_queue, Queue)

        self.assertIsInstance(filled_queue, Queue)

        self.assertNotIsInstance(a_sequence, Queue)

    def test_max_capacity_from_instantiation(self):

        empty_and_without_max_capacity = Queue[str]()
        self.assertIsNone(empty_and_without_max_capacity.max_capacity)

        filled_and_without_max_capacity = Queue[str].from_sequence(["hello", "how're", "you", "?"])
        self.assertIsNone(filled_and_without_max_capacity.max_capacity)

        sample_sequence = 1, 2, 3, 4, 5

        queue_to_fill = Queue[int](max_capacity=len(sample_sequence))
        self.assertEqual(queue_to_fill.max_capacity, len(sample_sequence))

        filled_queue = Queue[int].from_sequence(sample_sequence, max_capacity=len(sample_sequence))
        self.assertEqual(filled_queue.max_capacity, len(sample_sequence))

    def test_len(self):
        empty_queue = Queue[float]()
        self.assertEqual(len(empty_queue), 0)

        float_sequence = [1.2, 3.2, 1.5, 3.9]

        filled_queue = Queue[float].from_sequence(float_sequence)
        self.assertEqual(len(filled_queue), len(float_sequence))

        empty_but_with_max_capacity = Queue[float](max_capacity=10)
        self.assertEqual(len(empty_but_with_max_capacity), 0)


if __name__ == "__main__":
    unittest.main()
