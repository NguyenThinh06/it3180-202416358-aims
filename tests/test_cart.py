import unittest
from aims.dvd import DigitalVideoDisc
from aims.cart import Cart


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i + 1}", cost=10.0)))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21", cost=10.0)))

    def test_total_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", cost=19.95))
        cart.add_dvd(DigitalVideoDisc("DVD 2", cost=24.95))
        self.assertAlmostEqual(cart.total_cost(), 44.90)
    def test_total_cost_with_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", cost=100.0))
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0)

    def test_discount_invalid_percent(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", cost=100.0))
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

if __name__ == "__main__":
    unittest.main()