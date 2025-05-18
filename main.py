from graphics import Window, Line, Point
from maze import Maze
from user import User
import sys

def main():
    screen_x = 1600
    screen_y = 1600
    user = User(screen_x, screen_y)
    
    user.wait_for_close()

main()