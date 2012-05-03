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

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Line

class ArrowPointer(Widget):
    arrow_tip = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ArrowPointer, self).__init__(**kwargs)
        with self.canvas.after:
            Color ([200, 200, 200])
            self.arrow_tip = Line(points=(0,0, 200, 200))
        self.bind(pos=self._update_arrow_points)
        self._update_arrow_points(self, self.pos)

    def _update_arrow_points(self, object, pos):
        offset = 50
        x,y = pos
        self.arrow_tip.points = (x - offset, y - offset, x + offset, y + offset)
        print self.arrow_tip