import logging

logger = logging.getLogger()

print(logger.parent)

logger = logging.getLogger(__name__)

print(logger.parent)