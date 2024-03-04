import unittest

from AssignmentsInPython.Character_Format_Error import CharacterFormatError
from AssignmentsInPython.Seven_Segment_Display import SevenSegmentDisplay
from AssignmentsInPython.binary_format_error import BinaryFormatError
from AssignmentsInPython.invalid_length_error import InvalidLengthError


class MyTestCase(unittest.TestCase):
    def test_inputNumberWithDigitsMoreThanEight_raisesError(self):
        sevenSegment = SevenSegmentDisplay()
        with self.assertRaises(InvalidLengthError):
            sevenSegment.my_segment("1111111111")

    def test_inputNumberWithNonBinaryDigits(self):
        sevenSegment = SevenSegmentDisplay()
        with self.assertRaises(BinaryFormatError):
            sevenSegment.my_segment("11123111")
    def test_for_inputs_with_alphabets(self):
        sevenSegment = SevenSegmentDisplay()
        with self.assertRaises(CharacterFormatError):
            sevenSegment.my_segment("abcdefgh")
