"""
This will be a project to get throttle data from a car and display it in a graph, 
similar to how throttle and brake pressure is visualized in Formula1 broadcasts.
This could help normal people to "analyze" their daily driving style and for example,
be smoother on the throttle, and could be cool for track days.
"""

import obd
import matplotlib.pyplot as plt
from time import time, sleep
import tkinter as tk

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

    # check the connection again to make sure that there is no unexpected
    # connection drop during data collection
    while connection:
        rpm = connection.query(rpm_cmd)
        rpm_vals.append(rpm.value.magnitude)

        time_of_measurement: float = time() - start_time
        if rpm_vals != 0:
            time_vals.append(time_of_measurement)

        if len(rpm_vals) > 10:  # restrict the size of the rpm vals : TESTING ONLY
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
    try:
        while True:
            if not connection.is_connected():

                print(
                    "Connection couldn't be made. \n"
                    "Please ensure the OBD-II device is plugged in and connected. \n"
                    "if you turned off the engine, or unplugged the device yourself, you can ignore this message"
                )
                break

            rpm_vals, time_vals = collect_rpm_values()
            plot_rpm_graph(rpm_vals, time_vals)

    except Exception as e:
        print(f"an unexpected error occurred {e}")


if __name__ == "__main__":
    main()
