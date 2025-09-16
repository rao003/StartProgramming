import unittest
from src.bridge_selector import calculate_bridge_configuration

class TestBridgeSelector(unittest.TestCase):

    def test_valid_configuration(self):
        span = 20.0
        load = 40
        config, num_panels, components = calculate_bridge_configuration(span, load)
        self.assertIsNotNone(config)
        self.assertEqual(config, 'Single-Double')
        self.assertEqual(num_panels, 7)
        self.assertEqual(components['Panel'], 14)
        self.assertEqual(components['Transom'], 8)
        self.assertEqual(components['Panel Pin'], 28)
        self.assertEqual(components['Male End Post'], 2)
        self.assertEqual(components['Female End Post'], 2)

    def test_no_configuration(self):
        span = 50.0
        load = 100
        config, num_panels, components = calculate_bridge_configuration(span, load)
        self.assertIsNone(config)
        self.assertIsNone(num_panels)
        self.assertIsNone(components)

    def test_edge_case_minimum_requirements(self):
        span = 12.2
        load = 12
        config, num_panels, components = calculate_bridge_configuration(span, load)
        self.assertIsNotNone(config)
        self.assertEqual(config, 'Single-Single')
        self.assertEqual(num_panels, 4)
        self.assertEqual(components['Panel'], 4)
        self.assertEqual(components['Transom'], 5)

    def test_invalid_input(self):
        span = -10.0
        load = 0
        config, num_panels, components = calculate_bridge_configuration(span, load)
        self.assertIsNone(config)
        self.assertIsNone(num_panels)
        self.assertIsNone(components)

if __name__ == '__main__':
    unittest.main()