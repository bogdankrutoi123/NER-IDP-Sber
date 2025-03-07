from score_fn import score_fn
import unittest

class TestScoreFn(unittest.TestCase):

    def test_perfect_match(self):
        gold = "John\tPER\nDoe\tPER"
        pred = "John\tPER\nDoe\tPER"
        self.assertEqual(score_fn(gold, pred), 1.0)

    def test_partial_match(self):
        gold = "John\tPER\nDoe\tPER"
        pred = "John\tPER\nSmith\tPER"
        self.assertEqual(score_fn(gold, pred), 0.5)

    def test_no_match(self):
        gold = "John\tPER\nDoe\tPER"
        pred = "Acme\tORG\nCorp\tORG"
        self.assertEqual(score_fn(gold, pred), 0.0)

    def test_empty_gold(self):
        gold = ""
        pred = "John\tPER\nDoe\tPER"
        self.assertEqual(score_fn(gold, pred), 0.0)

    def test_empty_pred(self):
        gold = "John\tPER\nDoe\tPER"
        pred = ""
        self.assertEqual(score_fn(gold, pred), 0.0)

    def test_empty_both(self):
        gold = ""
        pred = ""
        self.assertEqual(score_fn(gold, pred), 1.0)

    def test_wrong_class(self):
        gold = "Apple\tORG"
        pred = "Apple\tPER"
        self.assertEqual(score_fn(gold, pred), 0.0)

    def test_wrong_name(self):
        gold = "Apple\tORG"
        pred = "Microsoft\tORG"
        self.assertEqual(score_fn(gold, pred), 0.0)

if __name__ == '__main__':
    unittest.main()
