from .base_case import ChatBotTestCase
from chatterbot.algorithms.engram import Engram


class EngramTests(ChatBotTestCase):

    def test_exact_results(self):

        output = Engram("What... is your quest?", self.chatbot.database)
        expected = "To seek the Holy Grail."

        self.assertIn(expected, output.get().keys())

    def test_empty_input(self):
        """
        If empty input is provided, anything may be returned.
        """
        output = self.chatbot.get_response("")

        self.assertTrue(len(output) > -1)
