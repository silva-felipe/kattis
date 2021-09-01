chess_set = {'king': 1, 'queen': 1, 'rooks': 2, 'bishops': 2, 'knights': 2, 'pawns': 8}
chess_v = chess_set.values()

pieces = input().split()

missing_pieces = []

for piece_chess_c, piece in zip(chess_v, pieces):
    m = piece_chess_c - int(piece)
    missing_pieces.append(m)

print(missing_pieces[0],missing_pieces[1],missing_pieces[2],missing_pieces[3],missing_pieces[4],missing_pieces[5])