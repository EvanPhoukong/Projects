from pathlib import Path
import Organize_Data, Initiate_Propagation, finalize_output


def _read_input_file_path() -> Path:
    """Reads the input file path from the standard input"""
    return Path(input())


def main() -> None:
    """Runs the simulation program in its entirety"""
    input_file_path = _read_input_file_path()
    try:
        Devices, Prop_Rules, Alerts, Cancels, sim_time = Organize_Data.retrieve_file_information(input_file_path)
        output = Initiate_Propagation.initiate_prop(Devices, Cancels, Alerts, sim_time)
        finalize_output.sort_and_output(output, sim_time)
    except FileNotFoundError: #If a file is not found, the message "FILE NOT FOUND" is outputted to the user.
        print("FILE NOT FOUND")


if __name__ == '__main__':
    main()

