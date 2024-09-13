import control
import matplotlib.pyplot as plt
from prettytable import PrettyTable

## ----------------- 1. Block diagrams and transfer function ----------------- ##

def step_plot(
    x: list,
    y: list,
    title: str = 'Respuesta de escalón del sistema',
    x_label: str = 'Time (seconds)',
    y_label: str = 'Amplitude',
    legend: list = ['Respuesta al escalón'],
    linewidth: float = 2,
    linestyle: str = ":"
) -> None:
    """
    Plots a step response of a system.

    Parameters:
    x (list): The x-axis data points (e.g., time).
    y (list): The y-axis data points (e.g., amplitude).
    title (str): The title of the plot. Default is 'Respuesta de escalón del sistema'.
    x_label (str): The label for the x-axis. Default is 'Time (seconds)'.
    y_label (str): The label for the y-axis. Default is 'Amplitude'.
    legend (list): The legend for the plot. Default is ['Respuesta al escalón'].
    linewidth (float): The width of the plot line. Default is 2.
    linestyle (str): The style of the grid lines. Default is ":".

    Returns:
    None
    """
    try:
        plt.plot(x, y, linewidth=linewidth)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(legend)
        plt.grid(linestyle = linestyle)
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


def step_info(
    sys: control.TransferFunction
) -> None:
    """
    Prints the step response information of a given transfer function.

    Parameters:
    sys (control.TransferFunction): The transfer function of the system.

    Returns:
    None
    """
    info = control.step_info(sys)
    table_info = PrettyTable()
    table_info.field_names = ["Parameters", "Values"]
    for key, value in info.items():
        table_info.add_row([key, value])
    print(table_info)