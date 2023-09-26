import pytest
from app.types.comment_type import CommentType
from app.utils.utils import (
    extractTimeAndFormat,
)  # Substitua 'your_module' pelo nome real do seu módulo
from typing import List
import unittest


class TestExtractTimeAndFormat(unittest.TestCase):
    def test_extraction(self):
        sample_data: List[CommentType] = [
            {"text": "0:28 eu como mono Kalista"},
            {"text": "8:25 mto engraçado"},
            {"text": "Ainda bem que o sylas não é nordestino"},
        ]

        expected_result: List[CommentType] = [
            {"text": "0:28 eu como mono Kalista", "timestamp": "0:28"},
            {"text": "8:25 mto engraçado", "timestamp": "8:25"},
            {"text": "Ainda bem que o sylas não é nordestino", "timestamp": None},
        ]

        self.assertEqual(extractTimeAndFormat(sample_data), expected_result)


if __name__ == "__main__":
    unittest.main()
