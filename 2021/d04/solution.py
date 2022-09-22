# INPUT_FILE = 'test_input.txt'
INPUT_FILE = 'input.txt'

class BingoBoard():
    def __init__(self, row_list):
        self.board = row_list # 2d 5x5 array of ints
        self.marked = [[False for _ in range(5)] for _ in range(5)]
        self.marked_cols = [[False for _ in range(5)] for _ in range(5)]
        self.setup_coords_dict() # sets up dict like { num1: (x1, y1), num2: (x2, y2), etc } 

    def process_num(self, num):
        if num in self.coords_dict:
            x,y = self.coords_dict[num]
            self.mark(x,y)
        
    def row(self, idx):
        return self.board[idx]

    def col(self, idx):
        return list(zip(*self.board[idx]))

    def mark(self, x, y):
        self.marked[x][y] = True
        self.marked_cols[y][x] = True

    def won(self):
        return any(all(row) for row in self.marked) or any(all(row) for row in self.marked_cols) 

    def score(self, final_num):
        unmarked_sum = 0
        for x in range(5):
            for y in range(5):
                if not self.marked[x][y]:
                    unmarked_sum += self.board[x][y]
        return unmarked_sum * final_num

    def setup_coords_dict(self):
        self.coords_dict = {}
        for x in range(5):
            for y in range(5):
                val = self.board[x][y]
                self.coords_dict[val] = (x,y)
        

def parse_board(board_str):
    result = []
    for row in board_str.split('\n'):
        formatted_row = [int(x) for x in filter(None, row.split(" "))]
        result.append(formatted_row)
    return result

def parse_input(input_file):
    # returns ([draw_list], [bingo_board_list])
    with open(input_file, 'r') as f:
        inputs = [x for x in f.read().split('\n\n')]
    draw_list = [int(x) for x in inputs[0].split(',')]
    boards = [BingoBoard(parse_board(x)) for x in inputs[1:]]
    return (draw_list, boards)

def winning_board(boards):
    for b in boards:
        if b.won():
            return b
    return None

def part_one():
    draw_list, boards = parse_input(INPUT_FILE)
    draw_idx = 0
    last_drawn = None
    winner = None
    while winner is None:
        last_drawn = draw_list[draw_idx]
        draw_idx += 1
        for b in boards:
            b.process_num(last_drawn)
        winner = winning_board(boards)
    print(winner.score(last_drawn))
    return winner

def main():
    draw_list, boards = parse_input(INPUT_FILE)
    original_boards = boards.copy()
    draw_idx = 0
    last_drawn = None
    while len(boards) > 1:
        last_drawn = draw_list[draw_idx]
        draw_idx += 1
        for b in boards:
            b.process_num(last_drawn)
        boards = list(filter(lambda x: not x.won(), boards))
    # breakpoint()
    losing_board = boards[0]
    while not losing_board.won():
        last_drawn = draw_list[draw_idx]
        draw_idx += 1
        losing_board.process_num(last_drawn)
    # breakpoint()
    print(losing_board.score(last_drawn))
    return losing_board



if __name__ == '__main__':
    main()