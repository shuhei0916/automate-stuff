import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('program started')

def factorial(n):
    logging.debug('factorial({})start'.format(n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i = {}, total = {}'.format(i, total))
    logging.debug('factorial({})End'.format(n))
    return total

print(factorial(5))
logging.debug('program ended')