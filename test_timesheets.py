import unittest

from unittest import TestCase
from unittest.mock import patch, call
import timesheets

class TestTimeSheet(TestCase):
    #mock input() and force to return a value
    #side_effect is always a list [] - replaces input with this value
    @patch('builtins.input',side_effect=['2'])
    def test_get_hours_for_day(self, mock_input):
        hours= timesheets.get_hours_for_day('Monday')
        self.assertEqual(2, hours)

#add valid value at end; mock inputs are rejected until a correct value is input
    @patch('builtins.input', side_effect=['cat', '', 'fish', '12bird', 'icecream23', '2'])
    def test_get_hours_for_day_not_nmeric_rejected(self, mock_input):
        hours= timesheets.get_hours_for_day('Monday')
        self.assertEqual(2, hours)

    @patch('builtins.input', side_effect=['-1', '-124', '2'])
    def test_get_hours_for_day_hours_greater_than_zero(self, mock_input):
        hours= timesheets.get_hours_for_day('Monday')
        self.assertEqual(2, hours)

    @patch('builtins.input', side_effect=['25', '36', '100', '6'])
    def test_get_hours_for_day_hours_less_than_twentyfour(self, mock_input):
        hours= timesheets.get_hours_for_day('Monday')
        self.assertEqual(6, hours)

    @patch('builtins.print')
    def test_display_total(self, mock_print):
        timesheets.display_total(40)
        mock_print.assert_called_once_with('Total hours worked: 40')

    @patch('timesheets.alert')
    def test_alert_meet_min_hours_doesnt_meet(self, mock_alert):
        timesheets.alert_not_meet_min_hours(12,30)
        mock_alert.assert_called_once()

    @patch('timesheets.alert')
    def test_alert_meet_min_hours_does_meet_min(self, mock_alert):
        timesheets.alert_not_meet_min_hours(40,30)
        mock_alert.assert_not_called()

    @patch('timesheets.get_hours_for_day')
    def test_get_hours(self, mock_get_hours):
        mock_hours = [5,7,9]
        mock_get_hours.side_effect = mock_hours
        days=['m','t','w']
        expected_hours = dict(zip(days, mock_hours)) #make a dict days are K, mock_hours are V by zipping the 2 lists
        hours = timesheets.get_hours(days)
        self.assertEqual(expected_hours, hours)

    @patch('builtins.print')
    def test_display_hours(self, mock_print):
        example = {'M': 3, 'T':12, 'W':8}
        expected_table_calls= [
            call('Day            Hours Worked   '),
            call('M              3              '),
            call('T              12             '),
            call('W              8              ')
        ]
        timesheets.display_hours(example) #call method
        mock_print.assert_has_calls(expected_table_calls)


    def test_total_hours(self):
        example = {'M': 3, 'T':12, 'W':8}
        total = timesheets.total_hours(example)
        expected_total= 3 + 12 + 8
        self.assertEqual(total, expected_total)



if __name__ == '__main__':
    unittest.main()