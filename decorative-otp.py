#!/usr/bin/python

"""
Produces decorative one-time-pad images suitable for your next LARP, ARG or just to leave around the house.

Michael Fincham <michael@finch.am> 2009. This code is in the public domain.
"""

import random, Image, ImageDraw, ImageFont

font = ImageFont.truetype("LiberationMono-Regular.ttf", 30)
fontb = ImageFont.truetype("LiberationMono-Bold.ttf", 30)

def randline(drawto, pos, string, font):
  i = 0
  for char in string:
    drawto.text((pos[0] + 20 * i + (random.uniform(0,2)-1),pos[1] + (random.uniform(0,2)-1) ),char,font=font,fill="#000000")
    i += 1
    
for card in range(0,20):
  count = 0
  lines = 0
  im = Image.new("RGB", (1016,608), "#ffffff")
  draw = ImageDraw.Draw(im)
  im2 = Image.new("RGB", (1016,608), "#ffffff")
  draw2 = ImageDraw.Draw(im2)
  randline(draw, (32,48),"Card #%03i" % card,fontb)
  randline(draw2, (32,48),"Card #%03i" % card,fontb)
  line = ""
  for group in range(0,96):
    word = ""
    for letter in range(0,6):
      word = word + chr(65 + int(random.SystemRandom().uniform(0,26)))
    line = line + word + " "
    count += 1
    if count == 7:
      count = 0
      randline(draw,(32,124+48*lines),line,font)
      randline(draw2,(32,124+48*lines),line,font)
      lines += 1
      line = ""

  print "Saved card%ia.png and card%ib.png" % (card, card)
  im.save("card%ia.png" % card)
  im2.save("card%ib.png" % card)

