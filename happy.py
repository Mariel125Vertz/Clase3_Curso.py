import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import numpy as np

def draw_birthday_cake():
    fig, ax = plt.subplots(figsize=(10, 10))

    # Dibuja la base del pastel
    base = patches.Rectangle((0.2, 0.2), 0.6, 0.3, edgecolor='black', facecolor='#b3cde0', lw=2)
    middle = patches.Rectangle((0.25, 0.55), 0.5, 0.2, edgecolor='black', facecolor='#a2c2e0', lw=2)
    top = patches.Rectangle((0.3, 0.8), 0.4, 0.15, edgecolor='black', facecolor='#85a2d6', lw=2)
    
    ax.add_patch(base)
    ax.add_patch(middle)
    ax.add_patch(top)

    # Añadir decoraciones (grageas)
    grageas_colors = ['#d9eaf7', '#a6c2e0', '#9ab3e1']
    for i in range(10):
        x = 0.3 + (i % 5) * 0.1
        y = 0.8 + (i // 5) * 0.1
        ax.add_patch(patches.Circle((x, y), 0.03, color=grageas_colors[i % 3]))

    # Añadir velas
    candles = []
    for i in range(5):
        candle_x = 0.3 + i * 0.1
        candle = patches.Rectangle((candle_x, 0.85), 0.08, 0.2, edgecolor='black', facecolor='#f4b942', lw=2)
        ax.add_patch(candle)
        candles.append(candle)
        
        # Añadir llamas
        flame, = ax.plot([], [], color='orange', lw=2, linestyle='-', marker='o')
        candles.append((candle, flame))

    # Función de inicialización para la animación
    def init():
        for _, flame in candles:
            flame.set_data([], [])
        return [flame for _, flame in candles]

    # Función de animación
    def animate(frame):
        for candle, flame in candles:
            # Animar las llamas
            x_center = candle.get_x() + 0.04
            y_center = candle.get_y() + 0.2
            x_data = [x_center, x_center + 0.02 * np.sin(frame / 10)]
            y_data = [y_center, y_center + 0.1 * np.cos(frame / 10)]
            flame.set_data(x_data, y_data)
        return [flame for _, flame in candles]

    # Añadir el mensaje
    plt.text(0.5, 0.5, 'Feliz Cumpleaños', horizontalalignment='center', verticalalignment='center', fontsize=24, weight='bold', color='#003d66')

    # Configurar el gráfico
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')  # Oculta los ejes

    plt.title('¡Feliz Cumpleaños!', fontsize=24, weight='bold', color='#003d66')

    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)
    plt.show()

draw_birthday_cake()
