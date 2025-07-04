import matplotlib.pyplot as plt
from utils.grid_map import create_empty_grid, add_random_obstacles, add_wall


# def test_grid_map():
#     w, h = 10, 20
#     g = create_empty_grid(w, h)

#     add_random_obstacles(g, 0.4, 42, exclude=)


def test_grid_map():
    width, height = 20, 20
    grid = create_empty_grid(width, height)

    add_wall(grid, range(5, 15), fixed=10, axis='horizontal')
    add_wall(grid, range(3, 12), fixed=5, axis='vertical')

    start = (0, 0)
    goal = (19, 19)
    add_random_obstacles(grid, density=0.2, seed=42, exclude=[start, goal])

    plt.imshow(grid.T, origin='lower', cmap='Greys')
    plt.plot(start[0], start[1], 'go', label='Start')
    plt.plot(goal[0], goal[1], 'ro', label='Goal')
    plt.title("Grid Map Test")
    plt.legend()
    plt.axis('equal')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    test_grid_map()
