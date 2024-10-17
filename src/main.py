"""
This will be a project to get throttle data from a car and display it in a graph, 
similar to how throttle and brake pressure is visualized in Formula1 broadcasts.
This could help normal people to "analyze" their daily driving style and for example,
be smoother on the throttle, and could be cool for track days.
"""

import obd
import matplotlib.pyplot as plt
import numpy as np
from time import time, sleep

# start obd connection to the car
connection = obd.OBD()


def collect_rpm_values() -> list[float]:
    """collects the RPM values from the car

    Returns:
        list[float]: the rpm values recorded at regular intervals ie measured one time per second
    """

    rpm_cmd = obd.commands.RPM
    rpm_vals: list[float] = []

    time_vals: list[float] = []
    start_time: float = time()

    while connection:  # true when the engine is on
        rpm = connection.query(rpm_cmd)
        rpm_vals.append(rpm.value.magnitude)

        time_of_measurement: float = time() - start_time
        time_vals.append(time_of_measurement)

        if len(rpm_vals) > 10:
            break

        sleep(1)
    return rpm_vals, time_vals


def plot_rpm_graph(time_vals: list[float], rpm_vals: list[float]) -> None:
    """plots the rpm values (y) against time each second (y)

    Args:
        rpm_vals (list[int]): list of rpm measurements from OBD RPM sensor
    """

    plt.plot(time_vals, rpm_vals)
    plt.title("RPM")
    plt.xlabel("Time (seconds)")
    plt.ylabel("RPM")
    plt.show()


# driver function(s)
def main() -> None:
    if connection:
        plot_rpm_graph(collect_rpm_values)
    else:
        print("connection couldnt be made")


if __name__ == "__main__":
    main()
