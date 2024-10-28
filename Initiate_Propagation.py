import Propagation_of_Cancels, Propagation_of_Alerts, io, contextlib, _io

def initiate_prop(Devices: dict, Cancels: dict, Alerts: dict, sim_time: str) -> _io.StringIO:
    """
    The function initiates the propagation process of all cancels and alerts.

    Args:
        Devices: A dictionary that contains the number of a device and its corresponding device object as a key-value pair.
        Cancels: A dictionary whose keys are device numbers and whose values are dictionaries. For these nested dictionaries, the issue associated with a cancel
        and the time its first received by a device are stored as key-value pair.
        Alerts: A dictionary whose keys are device numbers and whose values are dictionaries. For these nested dictionaries, the issue associated with an alert
        and the time its first received by a device are stored as key-value pair.
        sim_time: The time the simulation ends stored as a string

    Returns:
        output: An _io.StringIO object whose value is a string containing the lines to be outputted, out of order.
    """
    with contextlib.redirect_stdout(io.StringIO()) as output: #Stores all lines to be outputted to the user in the variable "output".
        for start_device, cancels_dict in Cancels.items(): #Acquires each cancel and calls "propagate_cancellations" from "Propagation_of_Cancels" to propagate it.
            for issue, time in cancels_dict.items():
                Propagation_of_Cancels.propagate_cancellations(Devices, start_device, issue, time, sim_time)
        for start_device, alerts_dict in Alerts.items(): #Acquires each alert and calls "propagate_Alerts" from "Propagation_of_Alerts" to propagate it.
            for issue, time in alerts_dict.items():
                Propagation_of_Alerts.propagate_Alerts(Devices, start_device, issue, time, sim_time)
    return output
