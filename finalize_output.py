import _io

def sort_and_output(output: _io.StringIO, sim_time: str) -> None:
    """
    The function sorts the lines to be outputted in chronological order and outputs it.

    Args:
        output: An _io.StringIO object whose value is a string containing the lines to be outputted, out of order.
        sim_time: The time the simulation ends stored as a string.

    Returns:
        None
    """
    cancel_output = []
    sorting = []
    sorting2 = []
    final_output = []
    remove_dup = {}
    remove_dup2 = {}
    dup = []
    [cancel_output.append(i) for i in output.getvalue().split("\n")]
    cancel_output.append(f'@{sim_time}: END')
    for i in cancel_output[:]: #Acquires the time corresponding to each message, storing them as integers in "sorting".
        if not i:
            cancel_output.remove(i)
            continue
        number = i.strip("@").split(":")[0]
        sorting.append(int(number))
    for i in sorted(set(sorting)): #Stores the times from "sorting" into chronological order and as strings that are then stored into "sorting2".
        sorting2.append(str(i))
    for i in sorting2: #Appends each line of output in chronological order into "final_output" whose elements will be individually printed to the user.
        for j in cancel_output:
            if i == j.strip("@").split(":")[0]:
                final_output.append(j)
    [print(i) for i in final_output]