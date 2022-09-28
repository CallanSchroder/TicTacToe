theBoard = {'7': ' ', '8': ' ', '9': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):                              #board setup
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])



def ingame(board):
    turn = 'X'
    count = 0
     #placing pieces
    for i in range(10):
        printBoard(board)
        count += 1
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ':  # top
                print(f'player: {board["7"]} wins!')
                break
            elif board['4'] == board['5'] == board['6']  != ' ':  # middle
                print(f'player: {board["4"]} wins!')
                break
            elif board['1'] == board['2'] == board['3']  != ' ':  # bottom
                print(f'player: {board["2"]} wins!')
                break
            elif board['1'] == board['4'] == board['7']  != ' ':  # left-side-up
                print(f'player: {board["1"]} wins!')
                break
            elif board['2'] == board['5'] == board['8']  != ' ':  # middle-up
                print(f'player: {board["2"]} wins!')
                break
            elif board['3'] == board['6'] == board['9']  != ' ':  # right-side-up
                print(f'player: {board["3"]} wins!')
                break
            elif board['7'] == board['5'] == board['3']  != ' ':  # diagonal
                print(f'player: {board["3"]} wins!')
                break
            elif board['9'] == board['5'] == board['1']  != ' ':  # diagonal
                print(f'player: {board["5"]} wins!')
                break
            elif count == 9:
                print("its a draw!")

        place = int(input(f'please enter a number to play an {turn}: '))

        if theBoard[f'{place}'] == ' ':
            theBoard[f'{place}'] = turn

        elif theBoard[f'{place}'] == theBoard[f'{place}']:

            print("that place is already taken! try again")
            place = int(input(f'please enter a number to play an {turn}: '))
            if theBoard[f'{place}'] == ' ':
                theBoard[f'{place}'] = turn

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


printBoard(theBoard)
ingame(theBoard)