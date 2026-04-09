# ProjectEulerProblem31.py

import unittest
import math

class test_ProjectEulerProblem31(unittest.TestCase):
    def test_mainDriver(self):
        counterCombin = 0
        for k200 in range(2):
            for k100 in range(3):
                for k50 in range(5):
                    for k20 in range(11):
                        for k10 in range(21):
                            for k5 in range(41):
                                for k2 in range(101):
                                    k1 = 200 - k200*200
                                    k1 = k1 - k100*100
                                    k1 = k1 - k50*50
                                    k1 = k1 - k20*20
                                    k1 = k1 - k10*10
                                    k1 = k1 - k5*5
                                    k1 = k1 - k2*2
                                    if k1 >= 0:
                                        counterCombin = counterCombin + 1
                                        print("-"*50)
                                        print(
                                            "Number of 200p coins = ",
                                            k200
                                            )
                                        print(
                                            "Number of 100p coins = ",
                                            k100
                                            )
                                        print(
                                            "Number of 50p coins = ",
                                            k50
                                            )
                                        print(
                                            "Number of 20p coins = ",
                                            k20
                                            )
                                        print(
                                            "Number of 10p coins = ",
                                            k10
                                            )
                                        print(
                                            "Number of 5p coins = ",
                                            k5
                                            )
                                        print(
                                            "Number of 2p coins = ",
                                            k2
                                            )
                                        print(
                                            "Number of 1p coins = ",
                                            k1
                                            )
                                        print(
                                            "Total currency =",
                                            k1 + 2*k2 + 5*k5 \
                                            + 10*k10 \
                                            + 20*k20 \
                                            + 50*k50 \
                                            + 100*k100 \
                                            + 200*k200
                                            )
                                        self.assertEqual(
                                            k1 + 2*k2 + 5*k5 \
                                            + 10*k10 \
                                            + 20*k20 \
                                            + 50*k50 \
                                            + 100*k100 \
                                            + 200*k200, 200
                                            )
                                        print("-"*50)
        print("Total number of combinations =", counterCombin)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()