from nose.tools import assert_equal
import pandas.util.testing as pdt


class TestFoo(object):

    def __init__(self, score = 0):
        self.score = score

    def test_response1(self):
        assert_equal(answer1(), "A")
        self.score += 0.25

    def test_response2(self):
        assert_equal(answer2(), "B")
        self.score += 0.25

    def test_response3(self):
        try:
            assert average([3,1,3,4]) == 2.75
            self.score += 2.5
        except:
            assert (average([3,1,3,4]) == 2.75).all()
            self.score += 2.5

    def test_response4(self):
        assert_equal(answer4(), "C")
        self.score += 0.25

    def test_response5(self):
        assert_equal(answer5(), "B")
        self.score += 0.25

    def test_response6(self):
        assert_equal(answer6(), "D")
        self.score += 0.25

    def test_response7(self):
        assert_equal(answer7(), "A")
        self.score += 0.25

    def test_response8(self):
        assert_equal(answer8(), "D")
        self.score += 0.5

    def test_response9(self):
        assert_equal(answer9(), "A")
        self.score += 0.5

    def test_response10(self):
        assert countTinyPairs([16, 1, 4, 2, 14], [7, 11, 2, 0, 15], 743), 4
        self.score += 4

    def test_response11(self):
        assert_equal(prediction(4.7), 8)
        self.score += 5

    def test_response12(self):
        assert_equal(answer12(), "5/6")
        self.score += 2

    def test_response13(self):
        assert_equal(answer13(), "D")
        self.score += 0.5

    def test_response14(self):
        assert_equal(answer14(), "B")
        self.score += 0.5

    def test_response15(self):
        assert_equal(answer15(), "D")
        self.score += 0.5

    def test_response16(self):
        assert_equal(answer16(), "B")
        self.score += 0.5

    def test_response17(self):
        assert_equal(answer17(), "C")
        self.score += 0.5

    def test_response18(self):
        assert_equal(answer18(), "B")
        self.score += 0.5

    def test_response19(self):
        assert_equal(answer19(), "G")
        self.score += 0.5

    def test_response20(self):
        assert_equal(answer20(), "C")
        self.score += 0.5

    def print_scores(self):
        print("thanks for taking the test, here is your score : {}".format(self.score))

def main():
    test = TestFoo()

    for func in [test.test_response1,
                 test.test_response2,
                 test.test_response3,
                 test.test_response4,
                 test.test_response5,
                 test.test_response6,
                 test.test_response7,
                 test.test_response8,
                 test.test_response9,
                 test.test_response10,
                 test.test_response11,
                 test.test_response12,
                 test.test_response13,
                 test.test_response14,
                 test.test_response15,
                 test.test_response16,
                 test.test_response17,
                 test.test_response18,
                 test.test_response19,
                 test.test_response20
                ]:
        try:
            func()
        except:
            print("error : {}".format(func))

    test.print_scores()

if __name__ == '__main__':
    main()
