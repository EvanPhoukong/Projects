class Device:
    """
    The Device Class creates Device objects that act as a device in our simulation, storing information relatively to each unique device.

    Attributes:
        prop_to (dict): Contains the device the current object props to and the time it takes to propagate to that device as a key-value pair.
        cancels (dict): Dictionary containing keys regarding the issue of the Alert that the cancel seeks to resolve, and values
                        pertaining to the associated time the object should be aware of a cancellation.

    """
    def __init__(self) -> None:
        """
        Device is initialized with object attributes "prop_to" and "cancels" being created. The first stores the devices the object propagates
        to as keys and the time it takes to propagate to each device as values. The latter stores cancellations, with the issues being keys, and the time
        the objects become aware of these cancellations as values.

        Args:
            None

        Returns:
            None
        """
        self.prop_to = {}
        self.cancels = {}

    def prop_to_device(self, prop: str, time: str) -> None:
        """
        The method creates a key-value pair in prop_to, with the devices the object propagates to as keys and
        the time it takes to propagate to each device as values.

        Args:
            prop: the device the object propagates
            time: the time it takes to propagate to device

        Returns:
            None
        """
        self.prop_to[prop] = time

    def get_time(self, prop: str) -> str:
        """
        The method use "prop_to" to retrieve the time it takes to propagate to a given device given a key, "prop".

        Args:
            prop: the device the object propagates

        Returns:
            time: the time it takes to propagate to device
        """
        return self.prop_to[prop]

    def cancellations(self, issue: str, time: str) -> None:
        """
        The method stores the issue/reason and time of a cancellation as a key-value pair in "cancels".

        Args:
            issue: The issue/reason of the Alert that needs to be cancelled.
            time: the time the device is supposed to be aware of this cancellation

        Returns:
            None
        """
        self.cancels[issue] = time

    def get_cancellations(self) -> dict:
        """
        The method returns the dictionary containing information about the cancellations that the device is aware of as
        well as the time the device should be aware of the cancellation.

        Args:
            None

        Returns:
            Cancels: Dictionary containing keys regarding the issue of the Alert that the cancel seeks to resolve, and values
            pertaining to the associated time the object should be aware of a cancellation.
        """
        return self.cancels