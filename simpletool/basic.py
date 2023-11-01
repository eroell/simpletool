class SimpleClass(object):
    """This is a simple class

    :param input: This is an input
    :type input: str
    :param addr: Address, defaults to None
    :type addr: str, optional
    """

    def __init__(self, input, addr=None):
        """Constructor method
        """
        self.input = input
        self.addr = addr


    def doSomething(self, concat_piece=None):
        """Returns a string. This will perform Bluetooth service
        discovery if this has not already been done; otherwise it will return a
        cached list of services immediately..

        :param concat_piece: A piece of string which is added to this classes
            input string
        :type concat_piece: str, optional
        :return: A string.
        :rtype: str
        """
        return self.input + concat_piece

def add_1(number: int):
    """Adds one to the input..

    :param number: A piece of string which is added to this classes
        input string.
    :type number: int
    :return: The number incremented by one.
    :rtype: int
    """
    return 1 + number