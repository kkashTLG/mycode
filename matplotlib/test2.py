#!/usr/bin/env python3

import matplotlib.pyplot as plt

def main():
    fig, ax = plt.subplots()

    fruits = ['Nintendo Switch', 'Playstation 5', 'Xbox X/S']
    counts = [25.02, 12.59, 8.75]
    bar_labels = ['Nintendo', 'Sony', 'Microsoft']
    bar_colors = ['tab:red', 'tab:blue', 'tab:green']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Unit sales in miilions')
    ax.set_xlabel('Source: https://www.statista.com/statistics/276768/global-unit-sales-of-video-game-consoles/ ')
    ax.set_title('Game console sales in 2021')
    ax.legend(title='Manufacturer')

    plt.savefig("/home/student/static/test2.png")

main()
