# -*- coding: utf-8 -*-
import cocos
import urllib2
import json
from defines import *

class Billboard(cocos.layer.ColorLayer):
    def __init__(self, game):
        super(Billboard, self).__init__(0, 0, 0, 255, WIDTH, HEIGHT)
        self.game = game

        self.loading = cocos.text.Label(u'加载中...', font_name=FONTS, font_size=20)
        self.loading.position = 260, 240
        self.add(self.loading)

        self.schedule_interval(self.get_top, 0.5)


    def get_top(self, dt):
        self.remove(self.loading)
        self.unschedule(self.get_top)
        req = urllib2.urlopen('http://ppx.crossincode.com/top/?score=%d' % self.game.score)
        data = json.loads(req.read())
        top_a = data['all']
        top_t = data['today']
        i = 0
        for d in top_a:
            i += 1
            t = cocos.text.Label(u'%-16s %s' % (d['name'], d['score']),
                                 font_name=FONTS, font_size=18)
            t.position = 60, 370 - i * 26
            self.add(t)
        i = 0
        for d in top_a:
            i += 1
            t = cocos.text.Label(u'%-16s %s' % (d['name'], d['score']),
                                 font_name=FONTS, font_size=18)
            t.position = 360, 370 - i * 26
            self.add(t)
            if i == 1:
                self.game.top = d['name'], d['score']
        name = ''
        if self.game.name:
            name = self.game.name + u'，'
        rank = cocos.text.Label(name + u'你的成绩 %d 打败了银河系中 %s%% 的皮皮虾！' % (self.game.score, data['rank']),
                                font_name=FONTS,
                                font_size=16)
        rank.position = 20, 430
        self.add(rank)
        top_all = cocos.text.Label(u'今日排名',
                                   font_name=FONTS,
                                   font_size=20)
        top_all.position = 100, 380
        self.add(top_all)
        top_today = cocos.text.Label(u'历史排名',
                                   font_name=FONTS,
                                   font_size=20)
        top_today.position = 420, 380
        self.add(top_today)

        menu = cocos.menu.Menu()
        menu.font_item['font_name'] = FONTS
        menu.font_item_selected['font_name'] = FONTS
        replay = cocos.menu.MenuItem(u'再来一次', self.replay)
        replay.y = -200
        menu.create_menu([replay])
        self.add(menu)

    def replay(self):
        self.game.reset()

    def show(self):
        self.visible = True
