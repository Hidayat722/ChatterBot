from .chatterbot import ChatBot


class Terminal(ChatBot):

    def __init__(self, name="Terminal", adapter="chatterbot.adapters.JsonDatabaseAdapter", database="database.db", logging=True):
        super(Terminal, self).__init__(name, adapter, database)

    def begin(self, user_input="Type something to begin..."):
        import sys

        print(user_input)

        while True:
            try:
                # 'raw_input' is just 'input' in python3
                if sys.version_info[0] < 3:
                    user_input = str(raw_input())
                else:
                    user_input = input()

                bot_input = self.get_response(user_input)
                print(bot_input)

            except (KeyboardInterrupt, EOFError, SystemExit):
                break


class TalkWithCleverbot(ChatBot):

    def __init__(self, name="ChatterBot", adapter="chatterbot.adapters.JsonDatabaseAdapter", database="database.db", logging=True):
        super(TalkWithCleverbot, self).__init__(name, adapter, database)
        from chatterbot.cleverbot.cleverbot import Cleverbot

        self.running = True
        self.cleverbot = Cleverbot()

    def begin(self, bot_input="Hi. How are you?"):
        import time
        from random import randint
        from chatterbot.apis import clean

        print(self.name, bot_input)

        while self.running:
            cb_input = self.cleverbot.ask(bot_input)
            print("cleverbot:", cb_input)
            cb_input = clean(cb_input)

            bot_input = self.get_response(cb_input, "cleverbot")
            print(self.name, bot_input)
            bot_input = clean(bot_input)

            # Delay a random number of seconds.
            time.sleep(1.05 + randint(0, 9))


class SocialBot(object):
    """
    Check for online mentions on social media sites.
    The bot will follow the user who mentioned it and
    favorite the post in which the mention was made.
    """

    def __init__(self, **kwargs):
        from chatterbot.apis.twitter import Twitter

        chatbot = ChatBot("ChatterBot")

        if "twitter" in kwargs:
            twitter_bot = Twitter(kwargs["twitter"])

            for mention in twitter_bot.get_mentions():

                '''
                Check to see if the post has been favorited
                We will use this as a check for whether or not to respond to it.
                Only respond to unfavorited mentions.
                '''

                if not mention["favorited"]:
                    screen_name = mention["user"]["screen_name"]
                    text = mention["text"]
                    response = chatbot.get_response(text)

                    print(text)
                    print(response)

                    follow(screen_name)
                    favorite(mention["id"])
                    reply(mention["id"], response)
