import matplotlib.pyplot as plt
from config import PLOT_TITLE, X_LABEL, Y_LABEL, GRID

def plot_vi_curves(voltages, currents, resistance):
    plt.figure(figsize=(10, 6))
    plt.plot(voltages, currents, label=f"Resistance: {resistance} Ω", linewidth=2)
    plt.title(PLOT_TITLE)
    plt.xlabel(X_LABEL)
    plt.ylabel(Y_LABEL)
    plt.grid(GRID)
    plt.legend()
    plt.show()
    plt.savefig(f"vi_curve_{resistance}ohm.png")
    plt.close()