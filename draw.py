import pygame

def draw_grid(screen, width, height, grid_size):
    """Draws a grid on the screen with x and y axes at the center"""
    color = (200, 200, 200)  # Light gray color
    
    # Calculate the center of the screen dynamically
    center_x = width // 2
    center_y = height // 2

    # Adjust the grid's origin to be at the center
    grid_origin_x = center_x - (center_x % grid_size)
    grid_origin_y = center_y - (center_y % grid_size)

    # Draw vertical lines (grid lines)
    for x in range(grid_origin_x, width, grid_size):
        pygame.draw.aaline(screen, color, (x, 0), (x, height), 1)

    for x in range(grid_origin_x - grid_size, 0, -grid_size):
        pygame.draw.aaline(screen, color, (x, 0), (x, height), 1)

    # Draw horizontal lines (grid lines)
    for y in range(grid_origin_y, height, grid_size):
        pygame.draw.aaline(screen, color, (0, y), (width, y), 1)

    for y in range(grid_origin_y - grid_size, 0, -grid_size):
        pygame.draw.aaline(screen, color, (0, y), (width, y), 1)

    # Draw the center x-axis (black line) at the center of the screen
    pygame.draw.aaline(screen, (0, 0, 0), (center_x, 0), (center_x, height), 1)

    # Draw the center y-axis (black line) at the center of the screen
    pygame.draw.aaline(screen, (0, 0, 0), (0, center_y), (width, center_y), 1)

def draw_perimeter_box(screen, width, height, grid_size, perimeter_Width, perimeter_Height):
    """Draws an empty box (just lines) in the center of the screen"""
    color = (216, 75, 29)  # Orange color for the perimeter lines
    
    # Calculate the center of the screen
    center_x = width // 2
    center_y = height // 2

    # Define the size of the box (aligning with grid size)
    box_width = perimeter_Width # 8 grid units wide
    box_height = perimeter_Height # 8 grid units high

    # Calculate the coordinates for the four corners of the box
    left = center_x - box_width // 2
    top = center_y - box_height // 2
    right = left + box_width
    bottom = top + box_height

    # Draw the perimeter using lines (top, left, bottom, and right)
    pygame.draw.aaline(screen, color, (left, top), (right, top), 2)  # Top
    pygame.draw.aaline(screen, color, (right, top), (right, bottom), 2)  # Right
    pygame.draw.aaline(screen, color, (right, bottom), (left, bottom), 2)  # Bottom
    pygame.draw.aaline(screen, color, (left, bottom), (left, top), 2)  # Left
    pygame.draw.circle(screen, color, (center_x, center_y), 10, 20)

def draw_line(screen, path):
    """Draw the path (line) based on the given list of points"""
    if len(path) > 1:
        pygame.draw.aalines(screen, (0, 0, 0), False, path, 2)
