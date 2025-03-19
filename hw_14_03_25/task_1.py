def find_words(board, words):
    def dfs(i, j, path, visited):
        if i < 0 or i >= M or j < 0 or j >= L or (i, j) in visited:
            return
        path += board[i][j]
        if path in word_set:
            result.add(path)
        visited.add((i, j))
        for dx, dy in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
            dfs(i + dx, j + dy, path, visited.copy())
        visited.remove((i, j))

    M, L = len(board), len(board[0])
    word_set = set(words)
    result = set()

    for i in range(M):
        for j in range(L):
            dfs(i, j, "", set())

    return sorted(result)

# Ввод данных
N = int(input())
words = input().split()
M, L = map(int, input().split())
board = [input().split() for _ in range(M)]

# Поиск и вывод слов
output = find_words(board, words)
print(" ".join(output))