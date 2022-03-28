from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(height=600, width= 600)
screen.bgcolor("black")#thay màu nền
scoreboard = ScoreBoard()
screen.title("Snake Game")
# score = screen.title("Score")

# 2 tạo chuyển động mượt mà cho con rắn bằng methods tracer
    # Bật /tắt hoạt ảnh và đặt độ trễ cho các bản vẽ cập nhật
screen.tracer(0)  # sẽ không hiển thị thêm gì nếu không có hàm update

snake = Snake()
food = Food()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()  # update hình ảnh sau khi dùng hàm tracer
    time.sleep(0.1)  # thêm 0.1s delay sau khi các seg di chuyển
        # 3: đưa các segment chuyển động giống rắn
        # chỉ điều khiển segment đầu tiên, các segment phía sau vào vị trí của seg ngay trước nó
    snake.move()
    ##phát hiện food
    if snake.head.distance(food) < 15:#methods distance dùng để kiểm tra khoảng cách giữa 2 đối tượng
        #kích thước của food là 10*10
        food.refresh()
        snake.extent()
        #hiển thị điểm
        scoreboard.increase_score()
    #phát hiện tường
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    #kiểm tra nếu va vào đuôi
    tall_segment = snake.segment[1::]
    for segment in tall_segment:
        # if segment == snake.head
            #pass
        if snake.head.distance(segment) < 10: #khoảng cách va vào nhau
            scoreboard.reset()
            snake.reset()























screen.exitonclick()