import logging

logger = logging.Logger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.FileHandler(f'add_student.log')
handler.setFormatter(formatter)
logger.addHandler(handler)

