from django.conf import settings
import appconf


class DemultiplexerConfig(appconf.AppConf):
    STREAM_KEY = "stream"
    PAYLOAD_KEY = "payload"
    MANAGE_ENVELOPE_USER_SIDE = True
    RAISE_EXCEPTIONS = False

    class Meta:
        prefix = "MULTIPLEXER"
