"""
@copyright:
  (C) Copyright 2012, Open Source Game Seed <devs at osgameseed dot org>

@license:
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from math import atan2, cos, sin, pi
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.properties import ObjectProperty, NumericProperty
from kivy.graphics import Color, Line
from kivy.lang import Builder

class ArrowPointer(Widget):
    arrow_body = ObjectProperty(None)
    arrow_tip = ObjectProperty(None)
    tail_pos = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ArrowPointer, self).__init__(**kwargs)
        self.tail_pos = Vector(self.pos)
        self.bind(pos=self._update_arrow_points)
        self.bind(tail_pos=self._update_arrow_points)
        with self.canvas:
            Color (0, 1, 0)
            self.arrow_body = Line()
            self.arrow_tip = Line()
        self._update_arrow_points(self, self.pos)

    def _update_arrow_points(self, object, pos):
        # Draw the body
        self.arrow_body.points = (self.x, self.y,
            self.tail_pos.x, self.tail_pos.y)
        arrow_angle = atan2(self.tail_pos.y - self.y,
                            self.tail_pos.x - self.x)
        self.arrow_body.points = (self.x, self.y,
            self.tail_pos.x, self.tail_pos.y)
        # Draw the tip
        tip_size = 15
        tip1_angle, tip2_angle = arrow_angle - (pi/5), arrow_angle + (pi/5)
        tip1_pos = Vector(self.x  + tip_size*cos(tip1_angle),
                    self.y + tip_size*sin(tip1_angle))
        tip2_pos = Vector(self.x  + tip_size*cos(tip2_angle),
                    self.y + tip_size*sin(tip2_angle))
        self.arrow_tip.points = (tip1_pos.x, tip1_pos.y, self.x, self.y,
                                  tip2_pos.x, tip2_pos.y)


    def __del__(self):
        self.cavnas.remove(self.arrow_body)
        self.cavnas.remove(self.arrow_tip)
