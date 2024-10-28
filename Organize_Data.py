from Devices import Device
import pathlib

def retrieve_file_information(input_file_path: pathlib.WindowsPath) -> tuple:
    """
    The function retrieves information pertaining to device, propagation rules, alerts, and cancellations from the file.

    Args:
        input_file_path: The path to the file.

    Returns:
        (Devices, Prop_Rules, Alerts, Cancels, sim_time): A tuple containing all important information from the file.
    """
    Devices = {}
    Prop_Rules = {}
    Alerts = {}
    Cancels = {}
    sim_time = 0
    with open(input_file_path, "r") as file: #Opens the file
        for i in file: #Iterates through each line of the file
            splitLine = i.strip("\n").split() #Removes newline characters from a line and splits it where spaces are present.
            if not splitLine:
                continue
            if splitLine[0] == "DEVICE": #If the line contains the word "DEVICE", adds key-value pair corresponding to the device in "Devices"
                Devices[splitLine[1]] = Device()
            if splitLine[0] == "PROPAGATE": #If the line contains the word "PROPAGATE", adds key-value pair corresponding to the propagation rule in "Prop_Rules".
                Prop_Rules[splitLine[1]] = splitLine[2] + " " + splitLine[3]
                Devices[splitLine[1]].prop_to_device(splitLine[2], splitLine[3])
            if splitLine[0] == "ALERT": #If the line contains the word "ALERT", adds key-value pair corresponding to the alert in "Alerts".
                if splitLine[1] in Alerts:
                    Alerts[splitLine[1]][splitLine[2]] = splitLine[3]
                else:
                    alert = {}
                    alert[splitLine[2]] = splitLine[3]
                    Alerts[splitLine[1]] = alert
            if splitLine[0] == "CANCEL": #If the line contains the word "CANCEL", cancel information is stored in a dictionary that is then added to "Cancels".
                if splitLine[1] in Cancels:
                    Cancels[splitLine[1]][splitLine[2]] = splitLine[3]
                else:
                    cancellation = {}
                    cancellation[splitLine[2]] = splitLine[3]
                    Cancels[splitLine[1]] = cancellation
            if splitLine[0] == "LENGTH": #If the line contains the word "Length", alert information is stored in a dictionary that is then added to "Alerts".
                 sim_time = splitLine[1]
    return Devices, Prop_Rules, Alerts, Cancels, sim_time