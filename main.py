import random

class zrae():
    def __init__(self,n) -> None:
        self.n = n
        self.board = [['O' for i in range(self.n)] for i in range(self.n)]
        self.init_bomb()
        self.visited = [[ False for i in range(self.n)] for i in range(self.n)]
        self.flag = [[ False for i in range(self.n)] for i in range(self.n)]
        self.cnt = n
        self.cntflag = 0
    
    def init_bomb(self):
        for i in range(self.n):
            a = random.randrange(0,self.n,1)
            b = random.randrange(0,self.n,1)
            self.board[a][b] = 'X'
            self.init_mark(a,b)
    
    def init_mark(self,a,b):
        for i in range(-1,2):
            for j in range(-1,2):
                a2 = (a+i)
                b2 = (b+j)
                if (a2 < 0 or a2 >= self.n) or (b2 < 0 or b2 >= self.n):
                    continue
                c = self.board[a2][b2]
                if c == 'O':
                    c = 1
                elif c != 'X':
                    c += 1
                self.board[a2][b2] = c
                
    def strength_land(self,a,b):        
        if self.board[a][b] == 'O':
            if not ((a < 0 or a >= self.n) or (b < 0 or b >= self.n)):
                self.visited[a][b] = True
            else:
                return False
            for i in range(-1,2):
                for j in range(-1,2):
                    a2 = a+i
                    b2 = b+j
                    if (a2 < 0 or a2 >= self.n) or (b2 < 0 or b2 >= self.n):
                        continue
                    if self.visited[a2][b2]:
                        continue
                    else:
                        self.strength_land(a2,b2)
        elif self.board[a][b] != 'X':
            self.visited[a][b] = True

    def get_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j],end=" ")
            print()

    def get_board2(self):
        cnt = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.visited[i][j]:
                    cnt+=1
                    print(self.board[i][j],end=" ")
                elif self.flag[i][j]:
                    print('F',end=" ")
                else:
                    print('P',end=" ")
            print()

    def click(self):
        print()
        a = int(input("x : "))
        b = int(input("y : "))
        print()
        if not ((a < 0 or a >= self.n) or (b < 0 or b >= self.n)):
            if self.board[a][b] == 'X':
                print('Game Over!')
                return True
            c = self.strength_land(a,b)
        return False
    
    def flagfunc(self):
        print()
        a = int(input("x : "))
        b = int(input("y : "))
        print()
        if not ((a < 0 or a >= self.n) or (b < 0 or b >= self.n)):
            if not self.visited[a][b]:
                self.flag[a][b] = True
    
    def GameWin(self):
        cnt = 0
        cnt2 = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.flag[i][j]:
                    cnt += 1
                elif self.visited[i][j]:
                    cnt2 += 1
        self.cntflag = cnt
        if cnt == self.cnt and cnt2 == self.n*self.n-self.cnt:
            print("You Win!")
            return True

    def get_ui(self):
        print("flag :",self.cnt - self.cntflag)
        print()

def main():
    a = zrae(2)

    while True:
        print()
        a.get_ui()
        choice = int(input("flag : 1 , click : 2"))

        if choice%2 == 1:
            a.flagfunc()
        else:
            if a.click():
                break

        a.get_board2()
        if a.GameWin():
            break
            

if __name__ == "__main__":
    main()