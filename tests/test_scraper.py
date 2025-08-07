import unittest
from unittest.mock import MagicMock

from selenium.common.exceptions import StaleElementReferenceException

from src.scraper.scraper import Scraper


class TestScraper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.scrapper = Scraper("test-url", [])

    def test_successful_data_extraction(self):
        cell_0 = MagicMock()
        cell_0.text = '1\nEthereum'
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

        result = self.scrapper.extract_data([mock_element])
        self.assertEqual(result, expected)

    def test_stale_element_handling(self):
        broken_element = MagicMock()
        broken_element.find_elements.side_effect = StaleElementReferenceException()

        result = self.scrapper.extract_data([broken_element])
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
