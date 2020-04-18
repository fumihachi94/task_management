import datetime
import sys
import random
from PIL import Image, ImageDraw, ImageFont

class GanttChart:
   def __init__(self,size=(512,256),color=(255,255,255)):
      self.im = Image.new("RGB",size,color) 
      self.draw = ImageDraw.Draw(self.im)
      self.im_width = size[0]
      self.im_height = size[1]
      
   def show(self):
      self.im.show()

if __name__ == '__main__':
   
   gchart = GanttChart((720, 320), (255,255,255))
   gchart.show()
   print('Helloe gantt chart')
