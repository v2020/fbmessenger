class MessageTag(object):
    TAGS = [
        'SHIPPING_UPDATE',
        'RESERVATION_UPDATE',
        'ISSUE_RESOLUTION'
    ]

    def __init__(self, tag):
        if tag not in self.TAGS:
            raise ValueError('Invalid tag provided.')
        self.tag = tag

    def to_dict(self):
        return self.tag
