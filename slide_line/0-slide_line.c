#include "slide_line.h"

/**
 * slide_line - Slide and merge array according to direction
 * @line: Array of integers
 * @size: Size of the array
 * @direction: Direction to slide (SLIDE_LEFT or SLIDE_RIGHT)
 * Return: 1 upon success, 0 upon failure
 */
int slide_line(int *line, size_t size, int direction) {
    size_t i, j, k;
    int merged = 0;

    if (direction != SLIDE_LEFT && direction != SLIDE_RIGHT)
        return 0;

    for (i = 0; i < size; i++) {
        if (line[i] == 0)
            continue;

        j = (direction == SLIDE_LEFT) ? 0 : size - 1;
        k = (direction == SLIDE_LEFT) ? i : size - i - 1;

        if (line[j] == 0)
            line[j] = line[k];
        else if (line[j] == line[k] && !merged) {
            line[j] += line[k];
            merged = 1;
        } else {
            j += (direction == SLIDE_LEFT) ? 1 : -1;
            line[j] = line[k];
            merged = 0;
        }

        if (j != k)
            line[k] = 0;
    }

    return 1;
}
