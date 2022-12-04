import logging

logger = logging.Logger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler = logging.FileHandler(f'{__name__}.log')
handler.setFormatter(formatter)
logger.addHandler(handler)


def draw(h, w):
    logger.debug(f'{h}; {w}')
    result = f"{'*' * w}\n" + \
             f"*{' ' * (w - 2)}*\n" * (h - 2) + \
             '*' * w
    return result


print(draw(12, 8))
print(draw(6, 14))