# -*- coding: utf-8 -*-
import cocos
import urllib
import urllib2
from defines import *

class Gameover(cocos.layer.ColorLayer):
    def __init__(self, game):
        super(Gameover, self).__init__(0, 0, 0, 255, WIDTH, HEIGHT)
        self.game = game
        self.billboard = None
        self.score = cocos.text.Label(u'分数：%d' % self.game.score,
                                      font_name=FONTS,
                                      font_size=36)
        self.score.position = 200, 340
        self.add(self.score)

        menu = cocos.menu.Menu(u'你挂了……')
        menu.font_title['font_name'] = FONTS
        menu.font_item['font_name'] = FONTS
        menu.font_item_selected['font_name'] = FONTS
        self.name = cocos.menu.EntryMenuItem(u'大虾请留名：', self.input_name, self.game.name)
        self.name.y = 0
        submit = cocos.menu.MenuItem(u'提交成绩', self.submit)
        submit.y = -33
        top = cocos.menu.MenuItem(u'排行榜', self.game.show_top)
        top.y = -67
        replay = cocos.menu.MenuItem(u'再来一次', self.replay)
        replay.y = -100
        menu.create_menu([self.name, submit, top, replay])
        self.add(menu)

        logo = cocos.sprite.Sprite('crossin-logo.png')
        logo.position = 550, 100
        self.add(logo, 99999)

    def input_name(self, txt):
        self.game.name = txt
        if len(txt) > 16:
            self.game.name = txt[:16]

    def submit(self):
        name = urllib.quote(self.game.name.encode('utf8'))
        req = urllib2.urlopen('http://ppx.crossincode.com/record/?name=%s&score=%d&tag=%s' % (name, self.game.score, 'source'))
        resp = req.read()
        if resp:
            self.game.show_top()

    def replay(self):
        self.game.reset()
