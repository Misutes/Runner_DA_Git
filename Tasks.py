

# Создаем  функцию столкнавения с объектом
def check_collision(barriers, x, y, width,  line_level):
    for element in barriers:
        if line_level + element.barriers_height <= y <= line_level:
            if element.barriers_x <= x < element.barriers_x + element.barriers_width:
                return True
            elif element.barriers_x <= x + width / 2 < element.barriers_x + element.barriers_width:
                return True
