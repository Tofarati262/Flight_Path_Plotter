import pygame
from config import perimeter_Width, perimeter_Height
from draw import draw_grid, draw_perimeter_box, draw_line

# Initialize Pygame
pygame.init()

# Set initial screen size
width, height = 800, 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Mouse Scroll and Draw Example")

grid_size = 50  # Grid size
scale_factor = 1  # Used to scale the grid
show_menu = True  # Boolean to control whether to show the menu box

# Perimeter box size and position
erase_mode = False

# Variable to track the current drawing path
drawing = False
drawn_path = []
coordinate_path = []

# Threshold for when to add a new point to the drawn path
distance_threshold = 5  # Pixels

# Store the last drawn point
last_x, last_y = None, None

# FPS Clock
clock = pygame.time.Clock()

# Menu options
options = ["DRAW", "ERASE", "EXPORT", "HIDE"]
Selected = " "

# Function to check if mouse is inside perimeter box
def is_mouse_in_perimeter_box(mouse_x, mouse_y, width, height, grid_size):
    center_x = width // 2
    center_y = height // 2
    box_width = perimeter_Width # 8 grid units wide
    box_height = perimeter_Height # 8 grid units high

    left = center_x - box_width // 2
    top = center_y - box_height // 2
    right = left + box_width
    bottom = top + box_height

    return left <= mouse_x <= right and top <= mouse_y <= bottom

running = True
while running:
    # Calculate menu box size
    menuboxwidth = min(500, max(200, int(width * 0.2)))  
    menuboxheight = min(600, max(150, int(height * 0.4)))  
    menu_x = width - menuboxwidth - 10  
    menu_y = height - menuboxheight - 10  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            drawn_path = []  # Clear the drawing
            coordinate_path = []  # Clear the drawing


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the click is inside the perimeter box
            if is_mouse_in_perimeter_box(mouse_x, mouse_y, width, height, grid_size):
                if event.button == 1:  # Left click
                    if not erase_mode:  # Draw mode
                        if is_mouse_in_perimeter_box(mouse_x, mouse_y, width, height, grid_size):
                            drawing = True
                            drawn_path.append((mouse_x, mouse_y))
                            coordinate_path.append(((mouse_x - (width / 2)), (mouse_y - (height / 2))))
                            last_x, last_y = mouse_x, mouse_y
                        else:
                            drawing = False
                    else:  # Erase mode
                        drawn_path = []  # Clear the drawing
            
            # Check if click is inside the menu
            for i, option in enumerate(options):
                option_y = menu_y + (menuboxheight // (len(options) + 1)) * (i + 1)
                if menu_x <= mouse_x <= menu_x + menuboxwidth and option_y - 10 <= mouse_y <= option_y + 10:
                    if option == "DRAW":
                        erase_mode = False
                        Selected = "DRAW"
                        print("draw")
                    elif option == "ERASE":
                        erase_mode = True
                        drawn_path = []
                        Selected = "ERASE"
                        print("erase")
                    elif option == "HIDE":
                        show_menu = not show_menu
                        Selected = "HIDE"
                        print("hide")
                    elif option == "EXPORT":
                        if drawn_path:
                            print("Exporting....")
                            Selected = "EXPORTED"
                            with open('FlightCoordinates.csv', 'w') as file:
                                file.write(f"\"{str("X")}\",\"{str("Y")}\"\n")
                                # Write the coordinates
                                for coord in coordinate_path:
                                    file.write(f"\"{str(coord[0])}\", \"{str(coord[1])}\"\n")

                        else:
                            print("No path drawn")

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
            elif event.button == 4:  # Scroll up
                scale_factor += 0.1
            elif event.button == 5:  # Scroll down
                scale_factor -= 0.1
            scale_factor = max(0.3, min(scale_factor, 5))  # Limit zooming range

        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if drawing and pygame.mouse.get_pressed()[0] and not erase_mode and is_mouse_in_perimeter_box(mouse_x, mouse_y, width, height, grid_size):  # Left button held down
                if last_x is not None and last_y is not None:
                    dist = ((mouse_x - last_x) ** 2 + (mouse_y - last_y) ** 2) ** 0.5
                    if dist >= distance_threshold:
                        drawn_path.append((mouse_x, mouse_y))
                        coordinate_path.append(((mouse_x - (width / 2)), (mouse_y - (height / 2))))
                        last_x, last_y = mouse_x, mouse_y
                else:
                    last_x, last_y = mouse_x, mouse_y

    # Clear screen
    screen.fill((255, 255, 255))

    # Adjust grid size based on scale_factor
    adjusted_grid_size = int(grid_size * scale_factor)

    # Draw elements
    draw_grid(screen, width, height, adjusted_grid_size)
    draw_perimeter_box(screen, width, height, grid_size, perimeter_Width, perimeter_Height)
    draw_line(screen, drawn_path)

    # Draw menu box
    if show_menu:
        pygame.draw.rect(screen, (224, 220, 219), (menu_x, menu_y, menuboxwidth, menuboxheight), border_radius=5)
        font = pygame.font.Font(None, 30)
        text_color = (0, 0, 0)

        for i, option in enumerate(options):
            text_surface = font.render(option, True, text_color)
            text_rect = text_surface.get_rect(center=(menu_x + menuboxwidth // 2, menu_y + (menuboxheight // (len(options) + 1)) * (i + 1)))
            screen.blit(text_surface, text_rect)

    # Draw FPS
    fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (0, 0, 0))
    screen.blit(fps_text, (width - fps_text.get_width() - 10, 10))

    # Draw Mouse Coordinates
    mouse_coords_text = font.render(f"Mouse: {pygame.mouse.get_pos()}", True, (0, 0, 0))
    screen.blit(mouse_coords_text, (10, 10))

    #Draw Selected State
    fps_text = font.render(f"STATE: {Selected}", True, (0, 0, 0))
    screen.blit(fps_text, (width - fps_text.get_width() -  200, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
