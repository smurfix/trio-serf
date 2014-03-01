class SerfResult(object):
    """
    Bounded result object for responses from a Serf agent.
    """

    def __init__(self, head=None, body=None):
        self.head, self.body = head, body

    def __repr__(self):
        return "%(class)s<head=%(h)s,body=%(b)s>" \
            % {'class': self.__class__.__name__,
               'h': self.head,
               'b': self.body}
