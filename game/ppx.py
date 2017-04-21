# -*- coding: utf-8 -*-
import cocos
from pyglet import image

class PPX(cocos.sprite.Sprite):
    def __init__(self, game):

        frame_1 = image.AnimationFrame(image.load('ppx1.png'), 0.15)
        frame_2 = image.AnimationFrame(image.load('ppx2.png'), 0.15)
        self.frames = image.Animation([frame_1, frame_2])
        frame_rush_1 = image.AnimationFrame(image.load('ppx_rush1.png'), 0.15)
        frame_rush_2 = image.AnimationFrame(image.load('ppx_rush2.png'), 0.15)
        self.frames_rush = image.Animation([frame_rush_1, frame_rush_2])
        super(PPX, self).__init__(self.frames)

        self.game = game
        self.dead = False
        self.can_jump = False
        self.speed = 0
        self.rush_time = 0
        self.velocity = 0
        self.image_anchor = 0, 0
        self.position = 100, 300
        self.schedule(self.update)

    def jump(self, h):
        if self.dead:
            return
        if self.can_jump:
            self.y += 3
            self.speed -= max(min(h, 350), 200)
            self.speed = max(-450, self.speed)
            self.can_jump = False

    def land(self, y):
        if self.dead:
            return
        if self.y > y - 30:
            self.can_jump = True
            self.speed = 0
            self.y = y

    def update(self, dt):
        if self.dead:
            return
        self.speed += 300 * dt
        self.y -= self.speed * dt
        if self.rush_time > 0:
            self.rush_time -= dt
            if self.rush_time <= 0:
                self.velocity = 0
                self.image = self.frames
        if self.y < -80:
            self.die()

    def die(self):
        self.speed = 0
        self.dead = True
        self.game.end_game()

    def reset(self):
        self.can_jump = False
        self.dead = False
        self.speed = 0
        self.velocity = 0
        self.rush_time = 0
        self.position = 100, 300
        self.image = self.frames

    def rush(self):
        self.image = self.frames_rush
        self.velocity = 400
        self.rush_time = 3
