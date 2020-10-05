import sys, unittest
from md import calcenergy
from ase.lattice.cubic import FaceCenteredCubic
from asap3 import EMT

class MdTests(unittest.TestCase):

    def test_calcenergy(self):
        atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                                  symbol='Cu',
                                  size=(4, 4, 4),
                                  pbc=True)
        atoms.calc = EMT()
        l = [[1,1,1]]*len(atoms)
        atoms.set_momenta(l)
        test1 = calcenergy(atoms)
        print(test1)
        self.assertAlmostEqual(test1[1], 0.023604947597016316)
        self.assertAlmostEqual(test1[2], 182.6160900827904)
        self.assertTrue(True)


if __name__ == '__main__':
    tests =  [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())
