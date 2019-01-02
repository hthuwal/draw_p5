RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def bubble_sort(heights):
    for i in range(len(heights)):
        for j in range(len(heights) - i - 1):
            yield "doing", {j: GREEN, j + 1: GREEN}
            if(heights[j] > heights[j + 1]):
                heights[j], heights[j + 1] = heights[j + 1], heights[j]
    yield "done", None


def selection_sort(heights):
    for i in range(len(heights)):
        k = i
        for j in range(i, len(heights)):
            yield "doing", {i: BLUE, j: GREEN, k: GREEN}
            if heights[k] > heights[j]:
                k = j

        heights[i], heights[k] = heights[k], heights[i]
        yield "doing", None

    yield "done", None
