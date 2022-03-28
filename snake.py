from turtle import Turtle, Screen
import time
screen = Screen()
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:


    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)
            # 1 taọ thân hình con rắn 3 ô
            # tạo thành 1 list dể thực hiện vòng lặp while
    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def extent(self):
        self.add_segment(self.segment[-1].position())

    # thêm segment mỗi khi rắn ăn


    def move(self):

        for num_seg in range(len(self.segment) - 1, 0, -1):  # update vị trí từ cuối lên đầu
        # range(start = len(segment), stop = 0 , step = -1)
            new_x = self.segment[num_seg - 1].xcor()  # seg 2 sẽ lấy vị trí của seg 1
            new_y = self.segment[num_seg - 1].ycor()  # seg 1 sẽ lấy vị trí của seg 0
            self.segment[num_seg].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)




    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)



