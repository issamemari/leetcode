from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        queue = []

        for i in range(len(board)):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][len(board[i]) - 1] == "O":
                queue.append((i, len(board[i]) - 1))

        for j in range(len(board[0])):
            if board[0][j] == "O":
                queue.append((0, j))
            if board[len(board) - 1][j] == "O":
                queue.append((len(board) - 1, j))

        while len(queue) > 0:
            current = queue[0]
            queue = queue[1:]

            if current in visited:
                continue

            visited.add(current)

            up = current[0] - 1, current[1]
            down = current[0] + 1, current[1]
            left = current[0], current[1] - 1
            right = current[0], current[1] + 1

            for direction in [up, down, left, right]:
                if (
                    direction[0] < len(board)
                    and direction[0] >= 0
                    and direction[1] < len(board[0])
                    and direction[1] >= 0
                    and board[direction[0]][direction[1]] == "O"
                ):
                    queue.append(direction)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"
