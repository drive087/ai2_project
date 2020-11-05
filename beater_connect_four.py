from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class alpha_connect_four():

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.history = []
        self.current_round = 0
        self.isWin = False
        self.current_board = self.init_board()

        self.init()

    def init(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://connect4.ist.tugraz.at:8080")
        
        self.start_ai_b()
        for i in range(4):
            self.click(0)
            while(True):
                history = self.driver.find_elements_by_css_selector('ol#history>li')
                if len(history)%2==0:break

            ColRowA = history[self.current_round].text
            ColRowA = ColRowA.split()
            ColRowB = history[self.current_round+1].text
            ColRowB = ColRowB.split()

            self.current_round = self.current_round+2
            a_move = (int(ColRowA[4])-1, int(ColRowA[6][0])-1)
            b_move = (int(ColRowB[4])-1, int(ColRowB[6][0])-1)
            self.gen_board(a_move, 'A')
            self.gen_board(b_move, 'B')

        cb = self.current_board
        self.print_board(cb)


    def check_win(self, board, player):
        for i in range(6):
            for j in range(4):
                if board[i][j:j+4]==[player,player,player,player]:
                    return True

        for i in range(3):
            for j in range(7):
                if board[i][j]== player and board[i+1][j]==player and board[i+2][j]==player and board[i+3][j]==player:
                    return True

        for i in range(3):
            for j in range(4):
                if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                    return True

        #NOT FINISH
        for i in range(3):
            for j in range(4):
                if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                    return True
        
                
    def start_ai_b(self):
        self.driver.find_element_by_id('optionsaib').click()
        time.sleep(2)

    def click(self, col):
        self.driver.find_elements_by_tag_name("td")[col].click() 
        time.sleep(2)

    def init_board(self):
        board = []
        for i in range(6):
            board2 = []
            for j in range(7):
                board2.append(' ')
            board.append(board2)
        return board

    def print_board(self, board):
        for row in range(len(board)-1,-1,-1):
            print(board[row])


    def gen_board(self, pos, player):
        self.current_board[pos[1]][pos[0]] = player


alpha_connect_four()