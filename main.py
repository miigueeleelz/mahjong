import numpy

board = list()


def create_game():
    for _ in range(2):
        array = range(1, 6)
        numpy.random.shuffle(array)
        board.append(array)

        array = range(6, 11)
        numpy.random.shuffle(array)
        board.append(array)

    numpy.random.shuffle(board)


def print_board():
    current_element = 1

    for i in range(4):
        for j in range(5):
            print(str(current_element) + ')' + str(board[i][j]) + '\t'),
            current_element += 1
        print('\n')


if __name__ == "__main__":
    create_game()
    print_board()
