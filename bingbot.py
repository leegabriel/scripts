"""
bingbot.py - Version 1.0.0

A script to automatically earn Bing Rewards credits.

The win32api module (aka pywin32) is available at 
https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/.

Be sure to download the appropriate executable for your system.

For example, this script uses pywin32-220.win32-py2.7.exe, and works for 
Windows 7, 32-bit Python 2.7. 

DISCLAIMER: Use this script at your own risk. I take no responsibility for 
any legal consequences resulting from your use of this script. Also, just
because I wrote this script does not necessarily mean that I use it myself. 

Bing Rewards FAQ:
https://www.bing.com/rewards/faq

Bing Rewards Terms of Use:
https://www.bing.com/rewards/tou

MIT License

Copyright (c) 2016 Gabriel Lee

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import webbrowser
import win32api, win32con
import time
import random

# list of keys, sorted by frequency for optimization
keys = {
'enter': 0x0D,
'e': 0x45,
't': 0x54,
'a': 0x41,
'o': 0x4F,
'i': 0x49,
'n': 0x4E,
's': 0x53,
'h': 0x48,
'r': 0x52,
'd': 0x44,
'l': 0x4C,
'c': 0x43,
'u': 0x55,
'm': 0x4D,
'w': 0x57,
'f': 0x46,
'g': 0x47,
'y': 0x59,
'p': 0x50,
'b': 0x42,
'v': 0x56,
'k': 0x4B,
'j': 0x4A,
'x': 0x58,
'q': 0x51,
'z': 0x5A,
}

# randomly generated words
words = [
"ray",
"natural",
"real",
"functional",
"hushed",
"clover",
"amused",
"lopsided",
"noisy",
"release",
"title",
"caption",
"aromatic",
"grey",
"cannon",
"moor",
"swing",
"baby",
"shrug",
"dolls",
"huge",
"squeal",
"sky",
"ceaseless",
"puncture",
"hunt",
"obey",
"old",
"helpless",
"living",
"voracious",
"large",
"quaint",
"stop",
"paste",
"incompetent",
"suspend",
"mouth",
"alcoholic",
"dependent",
"hang",
"scratch",
"slimy",
"prevent",
"common",
"volcano",
"friction",
"nest",
"flower",
"young",
"electric",
"transport",
"vast",
"aunt",
"discussion",
"second",
"clean",
"office",
"stop",
"flight",
"petite",
"annoying",
"offer",
"country",
"mature",
"marvelous",
"utopian",
"milk",
"uncovered",
"flap",
"swim",
"wiry",
"sand",
"scale",
"normal",
"start",
"fence",
"knee",
"wrathful",
"hover",
"scandalous",
"dogs",
"quiet",
"prose",
"driving",
"wait",
"shelf",
"delight",
"idiotic",
"eminent",
"hand",
"wonder",
"watch",
"unruly",
"brush",
"acidic",
"drain",
"behavior",
"obese",
"fork"
]

def press(key):
  """
  Press and release a virtual key value once.

  keybd_event(bVk, bScan, dwFlags, dwExtraInfo)

  bVk : BYTE Virtual-key code
  bScan : BYTE Hardware scan code
  dwFlags=0 : DWORD Flags specifying various function options
  dwExtraInfo=0 : DWORD Additional data associated with keystroke
  """
  # press key
  win32api.keybd_event(keys[key], 0, 0, 0)
  # wait arbitrarily long
  time.sleep(.1)
  # release a specific key (the pressed key)
  win32api.keybd_event(keys[key], 0, win32con.KEYEVENTF_KEYUP, 0)


iterations = 30; # 1 credit for every 2 searches

for i in range (0, iterations):
  webbrowser.open_new_tab('https://bing.com')

  # Add an arbitrary delay before typing each word
  time.sleep(4) 

  # Get a random index of the word array
  index = random.randint(0, iterations - 1)

  # Split the words string into characters
  characters = list(words[index])

  # Type each character of the word
  for k in range (0, len(characters)):
    press(characters[k])

  press('enter')