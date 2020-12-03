def paint_fill(mat, r, c, colour):
    if mat[r][c] == colour:
        return False
    return fill_paint(mat, r, c, mat[r][c], colour)


def fill_paint(mat, r, c, orig_color, colour):
    if r < 0 or r >= len(mat) or c < 0 or c >= len(mat):
        return False
    if mat[r][c] == orig_color:
        mat[r][c] = colour
        fill_paint(mat, r-1, c, orig_color, colour)
        fill_paint(mat, r+1, c, orig_color, colour)
        fill_paint(mat, r, c-1, orig_color, colour)
        fill_paint(mat, r, c+1, orig_color, colour)
    return True
