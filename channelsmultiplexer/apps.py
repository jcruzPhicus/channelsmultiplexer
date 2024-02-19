from django import apps


class ChannelsMultiplexerConfig(apps.AppConfig):
    name = "channelsmultiplexer"
    verbose_name = "Channels Multiplexer"

    def ready(self):
        super().ready()
        from .conf import settings
