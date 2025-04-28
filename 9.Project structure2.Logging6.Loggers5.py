import logging

logger_1 = logging.getLogger('one.two')

print(logger_1.parent)

logger_2 = logging.getLogger('one.two.three')

print(logger_2.parent)