import numpy

board = list()
positions_dict = dict()


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
            positions_dict[current_element] = [i, j]
            current_element += 1
        print('\n')


def validate_point(point):
    '''
    Function used to validate the point typed by the user
    '''
    response = dict()

    if (point.isdigit() is False):
        response['code'] = 'ERROR'
        response['message'] = 'The typed value is not valid'

        return response

    if int(point) not in positions_dict.keys():
        response['code'] = 'ERROR'
        response['message'] = 'The typed value does not exist'

        return response

    response['code'] = 'OK'

    return response


def check_point(point):
    '''
    Function used to check is the point is valid to remove
    '''
    response = dict()

    x, y = positions_dict[int(point)]

    if board[x][y] == '':
        response['code'] = 'ERROR'
        response['message'] = 'The point is empty'
        return response

    if y > 0 and y < 4 and (board[x][y + 1] != '' and board[x][y - 1] != ''):
        response['code'] = 'ERROR'
        response['message'] = 'The point is not on the shore'
        return response

    response['code'] = 'OK'
    return response


def start_game():
    '''
    Function used to handle the game logic
    '''
    user_wants_continue = 's'

    while True:
        print_board()

        while True:
            point_first_number = raw_input('Casilla 1: ')

            status_first_point = validate_point(point_first_number)

            if (status_first_point['code'] == 'OK'):
                break
            else:
                print(status_first_point['message'])

        while True:
            point_second_number = raw_input('Casilla 2: ')

            status_second_point = validate_point(point_second_number)

            if (status_second_point['code'] == 'OK' and point_first_number != point_second_number):
                break
            elif point_first_number == point_second_number:
                print("The second point should be different from the first point")
            else:
                print(status_second_point['message'])

        status_first_point = check_point(point_first_number)
        status_second_point = check_point(point_second_number)

        if status_first_point['code'] == 'OK' and status_second_point['code'] == 'OK':
            pos_x_first_number, pos_y_first_number = positions_dict[int(point_first_number)]
            pos_x_second_number, pos_y_second_number = positions_dict[int(point_second_number)]

            if board[pos_x_first_number][pos_y_first_number] == board[pos_x_second_number][pos_y_second_number]:
                board[pos_x_first_number][pos_y_first_number] = ''
                board[pos_x_second_number][pos_y_second_number] = ''

                user_wants_continue = raw_input('Continue? (s): ')
            else:
                print('Both numbers should be equals')
        else:
            if status_first_point['code'] == 'ERROR':
                print('Point 1: ' + status_first_point['message'])

            if status_second_point['code'] == 'ERROR':
                print('Point 2: ' + status_second_point['message'])

        if (numpy.sum(board == '') == 20 or user_wants_continue.lower() == 'n'):
            break


if __name__ == '__main__':
    create_game()
