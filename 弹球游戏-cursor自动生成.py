# -*- coding: utf-8 -*-
import os
import subprocess

# 游戏代码
game_code = '''
# -*- coding: utf-8 -*-
import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 设置窗口大小
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("弹球游戏")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 球的属性
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 8
ball_speed_y = 8

# 板条的属性
paddle_width = 100
paddle_height = 10
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - 20

# 游戏循环
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 移动球
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 球碰到左右墙壁
    if ball_x <= ball_radius or ball_x >= WIDTH - ball_radius:
        ball_speed_x = -ball_speed_x

    # 球碰到顶部
    if ball_y <= ball_radius:
        ball_speed_y = -ball_speed_y

    # 球碰到底部 (游戏结束)
    if ball_y >= HEIGHT - ball_radius:
        print("游戏结束!")
        pygame.quit()
        sys.exit()

    # 球碰到板条
    if (ball_y + ball_radius >= paddle_y and
        paddle_x <= ball_x <= paddle_x + paddle_width):
        ball_speed_y = -ball_speed_y

    # 移动板条 (键盘控制)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 7
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += 7

    # 移动板条 (鼠标控制)
    mouse_x, _ = pygame.mouse.get_pos()
    paddle_x = mouse_x - paddle_width // 2
    paddle_x = max(0, min(paddle_x, WIDTH - paddle_width))

    # 绘制
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius)
    pygame.draw.rect(screen, RED, (paddle_x, paddle_y, paddle_width, paddle_height))

    pygame.display.flip()
    clock.tick(60)
'''

# 保存游戏代码到文件
with open('pong_game.py', 'w', encoding='utf-8') as f:
    f.write(game_code)

print("游戏代码已保存到 pong_game.py")

# 运行游戏
print("正在启动游戏...")
subprocess.run(['python', 'pong_game.py'], encoding='utf-8')