king, queen, look, bishop, knight, pawn = map(int, input().split())
king1, queen1, look1, bishop1, knight1, pawn1 = 1, 1, 2, 2, 2, 8
king1 -= king
queen1 -= queen
look1 -= look
bishop1 -= bishop
knight1 -= knight
pawn1 -= pawn
print(str(king1) + " " + str(queen1) + " " + str(look1) + " " + str(bishop1) + " " + str(knight1) + " " + str(pawn1))