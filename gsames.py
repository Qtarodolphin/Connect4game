class State:
    def initial_state(self):
        # init player
        self.player_list.append(Player(5,0))
        self.player_list.append(Player(5,1))

        # init King
        self.white_king = King(15,3,4,8, self.player_list[0])
        self.board[4][8] = self.white_king
        self.black_king = King(15,3,4,0, self.player_list[1])
        self.board[4][0] = self.black_king

        init_pawn_spawn = int(9/2) + 1
        for i in range(init_pawn_spawn):
            self.white_pawn_list.append(SoldierPawn(i,3,1,i*2,7,False,self.player_list[0],1))
            self.board[i*2][7] = self.white_pawn_list[i]
            self.black_pawn_list.append(SoldierPawn(i,3,1,i*2,1,False,self.player_list[1],1))
            self.board[i*2][1] = self.black_pawn_list[i]

    def get_player_turn(self):
        return self.turn%2

class GameController:
    def player(self,state):
        return state.get_player_turn()
