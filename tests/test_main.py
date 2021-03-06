#!/usr/bin/python

from dtxScraper import main
import unittest
from mock import patch


class dtxScraperTests(unittest.TestCase):
    @patch('__builtin__.open')
    @patch('dtxScraper.main.logging')
    def test_get_grade_bad_file_io(self, mock_logger, mock_open):

        mock_open.side_effect = IOError
        with self.assertRaises(IOError):
            main.get_grade(123, "some_file")
        mock_open.assert_called_once_with('some_file', 'r')
        mock_logger.error.assert_called_once_with('Failed to open grades file')

    @patch('__builtin__.open')
    @patch('dtxScraper.main.logging')
    def test_get_grade_empty_file_contents(self, mock_logger, mock_open):

        mock_open.readlines.return_value = []
        with self.assertRaises(Exception):
            main.get_grade(123, 'some_file')
        mock_open.assert_called_once_with('some_file', 'r')
        mock_logger.error.assert_called_once_with('Grade file is empty')

    def test_get_grade_no_employee_number_found(self):

        pass

    def test_get_grade_no_splittable_line(self):

        pass

    def test_get_grade_returns_grade(self):

        pass

    def test_generate_csv_missing_jar(self):

        pass

    def test_generate_csv_file_jar_input_not_found(self):

        pass

    def test_generate_csv_wait_timeout(self):

        pass

    def test_parse_data_zero_length_data_post_backn_split(self):

        pass

    def test_parse_data_zero_length_data_post_backt_split(self):

        pass

    def test_get_details_zero_length_data_post_backr_split(self):

        pass

    def test_get_details_index_error_post_colon_split(self):

        pass

    def test_calculate_tb_empty_time_bookings(self):

        pass

    def test_calculate_tb_index_error_colon_split(self):

        pass

    def test_calculate_tb_APT_project_code(self):

        pass

    def test_calculate_tb_NBT_true(self):

        pass

    def test_calculate_tb_NBT_false(self):

        pass

    def test_calculate_tb_day_bookings_array_logic(self):

        pass

    def test_calculate_tb_day_bookings_index_error(self):

        pass

    def test_calculate_tb_project_booking_dict(self):

        pass

    def test_generate_timesheet_bad_load_workbook(self):

        pass

    def test_generate_timesheet_bad_get_sheet(self):

        pass

    def test_generate_timesheet_bad_period_split(self):

        pass

    def test_generate_timesheet_bad_cell_assignment(self):

        pass

    def test_generate_timesheet_bad_generate_cell_refs(self):

        pass

    def test_generate_timesheet_bad_cell_refs_pop(self):

        pass

    def test_generate_timesheet_bad_time_bookings_key(self):

        pass

    def test_generate_timesheet_bad_datetime_formatting(self):

        pass

    def test_generate_timesheet_empty_day_booking_day_value(self):

        pass

    def test_generate_timesheet_bad_workbook_save(self):

        pass

    def test_generate_cell_refs_bad_index(self):

        pass

    def test_generate_cell_refs_array_output(self):

        pass


if __name__ == "__main__":
    unittest.main()
