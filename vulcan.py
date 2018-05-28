from time import sleep


class Vulcan:
    def __init__(self, multiple=3, wait=1, exceptions=(Exception, )):
        self.multiple = multiple
        self.wait = wait 
        self.exceptions = exceptions

    def __call__(self, func):
        def timer(*args, **kwargs):
            for i in range(self.multiple + 1):    
                try:
                    res = func(*args, **kwargs)
                except self.exceptions:
                    sleep(self.wait)
                    print('this is the %s times' % i)
                    continue
                else:
                    return res
        return timer


import random


@Vulcan(3, 3)
def vulcan_div(x):
    n = random.choice([0,2])
    return print(x / n)

vulcan_div(2)
vulcan_div(3)
vulcan_div(4)
vulcan_div(5)
vulcan_div(6)
