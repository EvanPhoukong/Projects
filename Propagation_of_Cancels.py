def propagate_cancellations(Devices: dict, start_device: str, issue: str, time: str, sim_time: str) -> None:
    """
    The function propagates a given Cancel.

    Args:
        Devices: A dictionary that contains the number of a device and its corresponding device object as a key-value pair.
        start_device: The first device that receives a cancellation.
        issue: The issue corresponding to a cancellation.
        time: The time corresponding to when an alert is first received.
        sim_time: The time the simulation ends stored as a string

    Returns:
        None
    """
    if int(time) >= int(sim_time): #Checks to see if current time is higher or equal to the sim_time. If so, propagation is stopped.
        return
    if issue in Devices[start_device].get_cancellations(): #Checks to see if this device is already aware of the cancellation.
        return
    Devices[start_device].cancellations(issue, time)
    prop_devices = {}
    og_time = time
    for i in Devices[start_device].prop_to: #Ouputs the propagation messages for each device that "start_device" propagates to.
        time = og_time
        print(f'@{time}: #{start_device} SENT CANCELLATION TO #{i}: {issue}')
        time = str(int(time) + int(Devices[start_device].get_time(i)))
        if int(time) >= int(sim_time): #Checks to see if current time is higher or equal to the sim_time. If so, alert will not be received.
            pass
        else:
            print(f'@{time}: #{i} RECEIVED CANCELLATION FROM #{start_device}: {issue}')
        prop_devices[i] = time
    [propagate_cancellations(Devices, e, issue, i, sim_time) for e, i in prop_devices.items() if int(i) < int(sim_time)]
    #Propagates the cancellation across the devices in the "start_device" propagation set.
