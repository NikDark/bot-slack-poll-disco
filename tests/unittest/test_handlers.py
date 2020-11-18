import unittest
from unittest.mock import patch, Mock

from handlers.handlers import handle_commands, handle_interactivity
from tests.common_data import check_command_for_handle_commands_func


class TestPollStatus(unittest.TestCase):
    """
    Testing handlers.
    """

    def test_handle_commands(self):
        check_command_for_handle_commands_func('/disco', 'handlers.handlers.start_disco')
        check_command_for_handle_commands_func('/lightsoff', 'handlers.handlers.start_lightsoff')
        check_command_for_handle_commands_func('/poptop', 'handlers.handlers.start_poptop')
        check_command_for_handle_commands_func('/top', 'handlers.handlers.start_top')
        check_command_for_handle_commands_func('/poll_status', 'handlers.handlers.start_poll_status')
        check_command_for_handle_commands_func('/settings', 'handlers.handlers.start_settings')
        check_command_for_handle_commands_func('/drop', 'handlers.handlers.start_drop')
        check_command_for_handle_commands_func('/resume', 'handlers.handlers.start_resume')

    @patch('handlers.handlers.json')
    def test_handle_interactivity(self, mock_json):
        client = Mock()
        poll = Mock()
        request_form = Mock()
        
        mock_json.loads.return_value = {
            'type': 'block_actions',
            'user': {
                'id': 'UserID'
            },
            'actions':[{
                'value': 'TestValue'
            }],
            'container': {
                'channel_id': 'ChannelId',
                'message_ts': 'MessageId'
            }
        }

        handle_interactivity(client, poll, request_form)