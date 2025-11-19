import chess, time
import engine, main

board = chess.Board('1k1r1bnr/p1pp3p/1p2N1p1/2Q2p2/2P1n3/1P5P/P2N1PP1/R1B2RK1')
board.turn = chess.BLACK
main.draw_board(board)

start = time.time()
engine.evaluate(board)
stop = time.time()
total = stop - start

print(f'Generated for {total * 10**3}ms.')
