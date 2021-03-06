![Chatterbot: Machine learning in Python](http://i.imgur.com/b3SCmGT.png)

# ChatterBot

ChatterBot is a machine-learning based conversational dialog engine build in
Python which makes it possible to generate responses based on collections of
known conversations. The language independent design of ChatterBot allows it to
be trained to speak any language.

[![Package Version](https://badge.fury.io/py/ChatterBot.png)](http://badge.fury.io/py/ChatterBot)
[![Requirements Status](https://requires.io/github/gunthercox/ChatterBot/requirements.svg?branch=master)](https://requires.io/github/gunthercox/ChatterBot/requirements/?branch=master)
[![Build Status](https://travis-ci.org/gunthercox/ChatterBot.svg?branch=master)](https://travis-ci.org/gunthercox/ChatterBot)
[![Coverage Status](https://img.shields.io/coveralls/gunthercox/ChatterBot.svg)](https://coveralls.io/r/gunthercox/ChatterBot)
[![Code Climate](https://codeclimate.com/github/gunthercox/ChatterBot/badges/gpa.svg)](https://codeclimate.com/github/gunthercox/ChatterBot)

An example of typical input would be something like this:

> **user:** Good morning! How are you doing?  
> **bot:**  I am doing very well, thank you for asking.  
> **user:** You're welcome.  
> **bot:** Do you like hats?  

## How it works

An untrained instance of ChatterBot starts off with no knowledge of how to communicate. Each time a user enters a statement, the library saves the text that they entered and the text that the statement was in response to. As ChatterBot receives more input the number of responses that it can reply and the accuracy of each response in relation to the input statement increase. The program selects the closest matching response by searching for the closest matching known statement that matches the input, it then returns the most likely response to that statement based on how frequently each response is issued by the people the bot communicates with.

## Installation

This package can be installed from [PyPi](https://pypi.python.org/pypi/ChatterBot) by running:

```
pip install chatterbot
```

### Create a new chat bot  
**Note:** *The `ChatBot` requires that a name is specified for the bot.

```
from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")
```

An optional parameter `database` can be used to change the default database path.
The default database path is 'database.db'.*

```
from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious", database="my/custom/database.db")
```

### Training
After creating a new chatterbot instance it is also possible to train the bot. Training is a good way to ensure that the bot starts off with knowledge about specific responses. The current training method takes a list of statements that represent a conversation.

**Note:** Training is not required but it is recommended.

```
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot.train(conversation)
```

### Get a response

```
response = chatbot.get_response("Good morning!")
print(response)
```

## Other bot types

ChatterBot comes with a selection of useful chat bots built in.

#### Terminal ChatterBot
This is a simple chatterbot that runs in the console. It responds to any user input that is entered.
```
from chatterbot import Terminal
terminal = Terminal()
terminal.begin()
```

### Social ChatterBot
This bot type integrates with various social networking sites to communicate.
```
from chatterbot import SocialBot

TWITTER = {
    "CONSUMER_KEY": "<consumer_key>",
    "CONSUMER_SECRET": "<consumer_secret>"
}

chatbot = SocialBot(twitter=TWITTER)
```

You will need to generate your own keys for using any API. To use this feature with twitter's api you will need to register your application at
[Twitter's developer website](https://dev.twitter.com/apps) to get the token and
secret keys.

### Talk with CleverBot
Want to see what two bots have to say to each other? This allows your ChatterBot to talk to [CleverBot](http://www.cleverbot.com/).
```
from chatterbot import TalkWithCleverbot
talk = TalkWithCleverbot()
talk.begin()
```

## Testing

ChatterBot's built in tests can be run using nose.  
See the [nose documentation](https://nose.readthedocs.org/en/latest/) for more information.

## Use Cases

**Using ChatterBot in your app? Let us know!**

|[Salvius the Robot](https://github.com/gunthercox/salvius)|A humanoid robot.|
|---|---|
|[Zuluhotel](http://zuluhotel3.com)|A mmorpg shard emulation game.|

## History

See release notes for changes https://github.com/gunthercox/ChatterBot/releases
