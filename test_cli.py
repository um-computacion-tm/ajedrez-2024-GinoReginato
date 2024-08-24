from unittest.mock import patch
from chess import Chess
from cli import play

class TestCli(unittest.TestCase):
    @patch(
        "builtins.imput",
        side_effect=['1','1','2','2']
    )
    #@patch