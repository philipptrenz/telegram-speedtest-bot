import os

from telegram.ext import Updater #, CommandHandler, MessageHandler, Filters


class Bot():

    def __init__(self, token, channel):

        self.inner_bot = None

        self.token = token
        self.channel = channel

        self.main()

    # Define a few command handlers. These usually take the two arguments bot and
    # update. Error handlers also receive the raised TelegramError object in error.
    def start(self, bot, update):
        """Send a message when the command /start is issued."""

        text= 'Welcome!\n' \
              'You want to receive a daily timelapse from Peru? Just send me /subscribe\n' \
              'If you no longer want to receive the videos, just let me know by sending me /unsubscribe'

        self.inner_bot.send_message(chat_id=update.message.chat_id, text=text)

    def help(self, bot, update):
        """Send a message when the command /help is issued."""
        bot.send_message(chat_id=update.message.chat_id, text='Help!')

    def error(self, bot, update, telegramError):
        """Log Errors caused by Updates."""
        self.logger.warning('Update "%s" caused error "%s"', bot, telegramError)

    def send_message_to_channel(self, text):
        self.inner_bot.sendMessage(chat_id=self.channel, text=text)

    def send_hello_message(self):
        text = '👋 Hi, I\'m happy to report speedtest measurements!'
        self.send_message_to_channel(text)

    def stop(self):
        self.updater.stop()

    def main(self):
        """Start the bot."""
        # Create the Updater and pass it your bot's token.
        # Make sure to set use_context=True to use the new context based callbacks
        # Post version 12 this will no longer be necessary
        self.updater = Updater(token=self.token, request_kwargs={'read_timeout': 1000, 'connect_timeout': 1000})

        # Start the Bot
        self.updater.start_polling()

        #
        self.inner_bot = self.updater.bot

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        #updater.idle()


