from bot import Bot
from utils import Utils
from speedtest import Speedtest


if __name__ == '__main__':

    util = Utils()
    config = util.get_config()

    telegram_token = config['telegram']['token']
    telegram_channel = config['telegram']['channel']

    util.log('starting telegram bot')
    bot = Bot(token=telegram_token, channel=telegram_channel)

    util.log('starting speedtest')
    s = Speedtest()

    try:
        s.get_best_server()
        s.download()
        s.upload()
        s.results.share()

        res = s.results.dict()

        stats = "⬆️ {:.0f} kBit/s\n⬇️ {:.0f} kBit/s\n⏱ {:.0f} ms".format(
            res['download'] / 1000,
            res['upload'] / 1000,
            res['ping']
        )

        util.log('speedtest: ' + stats.replace('\n', ', '))

        bot.send_message_to_channel(stats)
        util.log('sent speedtest results to telegram channel')

    except Exception as e:

        util.log('something went wrong')
        print(e)

    bot.stop()
