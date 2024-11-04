import unittest
from unittest.mock import patch

from click.testing import CliRunner

from python_tool_template.__main__ import cli


class TestsCli(unittest.TestCase):
    """
    Unit tests to run against the command-line interface of the tool.
    """

    def setUp(self):
        self.runner = CliRunner()

    def test_cli_context_injection(self):
        """
        Tests the injection of a mock `click.Context` into the CLI command.
        Uses an isolated filesystem to ensure no side effects on the real filesystem.

        :return: None
        """
        with self.runner.isolated_filesystem():
            with patch('click.Context', create=True) as mock_context:
                result = self.runner.invoke(cli)
                mock_context.assert_called_once()
                self.assertEqual(result.exit_code, 0)

    def test_cli_help_option(self):
        """
        Runs the CLI with the --help option and verifies the output and exit code.

        :return: None
        """
        result = self.runner.invoke(cli, ['--help'])
        self.assertIn('The base command-line interface for the tool.', result.output)
        self.assertEqual(result.exit_code, 0)


if __name__ == "__main__":
    unittest.main()
