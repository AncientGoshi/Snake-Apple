def check_rect_in_point(rect, x, y):
    if rect.right >= x >= rect.left and \
            rect.bottom >= y >= rect.top:
        return True

    return False

def check_rects_collision(rect1, rect2):
    if check_rect_in_point(rect1, rect2.left, rect2.top):
        return True

    if check_rect_in_point(rect1, rect2.left, rect2.bottom):
        return True

    if check_rect_in_point(rect1, rect2.right, rect2.top):
        return True

    if check_rect_in_point(rect1, rect2.right, rect2.bottom):
        return True

    return False

