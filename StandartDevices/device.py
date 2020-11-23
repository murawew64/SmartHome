'''

'''
from abc import ABC, abstractmethod, abstractproperty


class Device(ABC):
    '''
    This parent abstract class provide base information about every device
    '''

    @abstractmethod
    def on(self):
        '''
        Every device can be turned on
        '''
        pass

    @abstractmethod
    def off(self):
        '''
        Every device can be turned off
        '''
        pass

    @abstractproperty
    def is_on(self):
        '''
        Property provide information about device state (on or off)
        '''
        pass
