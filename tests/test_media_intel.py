import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Ensure the media_intel module can be imported
sys.path.append(os.path.abspath('media-intel'))

from media_intel import media_intel

class TestMediaIntel(unittest.TestCase):
    @patch('media_intel.media_intel.paramiko.SSHClient')
    def test_list_media(self, mock_ssh):
        # Mock SSH client behavior
        mock_client = MagicMock()
        mock_ssh.return_value = mock_client
        mock_stdout = MagicMock()
        mock_stdout.readlines.return_value = [
            "total 8\n",
            "-rw-r--r-- 1 user user 123 Jan 1 00:00 video.mp4\n",
            "-rw-r--r-- 1 user user 456 Jan 1 00:01 audio.mp3\n",
        ]
        mock_client.exec_command.return_value = (None, mock_stdout, None)
        result = media_intel.list_media()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'video.mp4')
        self.assertEqual(result[1]['name'], 'audio.mp3')

if __name__ == '__main__':
    unittest.main()
