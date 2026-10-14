
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

grid = []

for i in range(rows):
    row = list(map(int, input("Enter row: ").split()))
    grid.append(row)

queue = []
fresh = 0

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 2:
            queue.append((i, j))
        elif grid[i][j] == 1:
            fresh += 1

minutes = 0

while len(queue) > 0 and fresh > 0:
    size = len(queue)

    for i in range(size):
        r, c = queue.pop(0)

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = r + dr
            nc = c + dc

            if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == 1):
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc))

    minutes += 1

if fresh == 0:
    print("Minutes:", minutes)
else:
    print("Minutes: -1")
