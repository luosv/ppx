# -*- coding: utf-8 -*-
import cocos

class Pill(cocos.sprite.Sprite):
    def __init__(self, block):
        super(Pill, self).__init__('pill.png')
        self.game = block.game
        self.ppx = block.game.ppx
        self.floor = block.floor
        self.position = block.x + block.width / 2, block.height + 100

        self.schedule(self.update)

    def update(self, dt):
        px = self.ppx.x + self.ppx.width / 2 - self.floor.x
        py = self.ppx.y + self.ppx.height / 2

        if abs(px - self.x) < 50 and abs(py - self.y) < 50:
            # ppx get pill
            self.parent.remove(self)
            self.ppx.rush()

    def reset(self):
        self.parent.remove(self)
