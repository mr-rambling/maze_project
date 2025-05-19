from graphics import Window, Line, Point
from maze import Maze
from user import User
import sys

def main():
    screen_x = 600
    screen_y = 600
    user = User(screen_x, screen_y)
    
    user.wait_for_close()

main()