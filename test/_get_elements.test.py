import unittest
from unittest.mock import MagicMock
from scraper.scraper import _get_elements


class TestGetElements(unittest.TestCase):
    def test_valid_element(self):

        cell_0 = MagicMock()
        cell_0.text = "1\nEthereum"
        cell_1 = MagicMock()
        cell_1.text = "1373"
        cell_2 = MagicMock()
        cell_2.text = "-"
        cell_3 = MagicMock()
        cell_3.text = "-"
        cell_4 = MagicMock()
        cell_4.text = "$65B"

        mock_element = MagicMock()
        mock_element.find_elements.return_value = [cell_0, cell_1, cell_2, cell_3, cell_4]

        expected = [{
            'Name': 'Ethereum',
            'Protocols': '1373',
            'TVL': '$65B'
        }]

        result = _get_elements([mock_element])
        print("RESULT:", result)
        self.assertEqual(result, expected)

    def test_invalid_split(self):
        cell_0 = MagicMock()
        cell_0.text = "Ethereum"
        cell_1 = MagicMock()
        cell_1.text = "100"
        cell_4 = MagicMock()
        cell_4.text = "$10B"

        mock_element = MagicMock()
        mock_element.find_elements.return_value = [cell_0, cell_1, MagicMock(), MagicMock(), cell_4]

        result = _get_elements([mock_element])
        self.assertEqual(result, [])

    def test_element_exception(self):
        broken_element = MagicMock()
        broken_element.find_elements.side_effect = Exception("Some error")

        result = _get_elements([broken_element])
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
