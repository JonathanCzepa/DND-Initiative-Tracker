import unittest
from main import *

class TelevisionCases(unittest.TestCase):
    
"""   
    def test_init(self):
        self.tv1 = Television()
        self.assertEqual(self.tv1.__str__(), "Power = False, Channel = 0, Volume = 0")
    
    
    def test_power(self):
        self.tv1 = Television()
        #ON
        self.tv1.power()
        self.assertEqual(self.tv1.__str__(), "Power = True, Channel = 0, Volume = 0")
        #OFF
        self.tv1.power()
        self.assertEqual(self.tv1.__str__(), "Power = False, Channel = 0, Volume = 0")
            
    
    def test_mute(self):
        self.tv1 = Television()
        #ON, VOL UP, MUTED
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        self.assertEqual(self.tv1.__str__(), "Power = True, Channel = 0, Volume = 0")
        #ON, UNMUTED
        self.tv1.mute()
        self.assertEqual(self.tv1.__str__(), "Power = True, Channel = 0, Volume = 1")
        #OFF, MUTED
        self.tv1.power()
        self.tv1.mute()
        self.assertEqual(self.tv1.__str__(), "Power = False, Channel = 0, Volume = 1")
        #OFF, UNMUTED
        self.tv1.power()
        self.tv1.mute()
        self.tv1.power()
        self.tv1.mute()
        self.assertEqual(self.tv1.__str__(), "Power = False, Channel = 0, Volume = 0")

    
    def test_channel_up(self):
        self.tv1 = Television()
        #OFF, CHANNEL INC
        self.tv1.channel_up()
        self.assertEqual(self.tv1.__str__(), "Power = False, Channel = 0, Volume = 0")
        #ON, CHANNEL INC
        self.tv1.power()
        self.tv1.channel_up()
        self.assertEqual(self.tv1.__str__(), "Power = True, Channel = 1, Volume = 0")
        #ON, CHANNEL INC PAST MAX
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.assertEqual(self.tv1.__str__(), "Power = True, Channel = 0, Volume = 0")
        
    
    
    def test_channel_down(self):
        self.tv1 = Television()
        #OFF, CHANNEL DOWN
        self.tv1.channel_down()
        self.assertEqual(self.tv1.__str__(), "Power = False, Channel = 0, Volume = 0")
        #ON, CHANNEL DOWN PAST MIN
        self.tv1.power()
        self.tv1.channel_down()
        self.assertEqual(self.tv1.__str__(), "Power = True, Channel = 3, Volume = 0")
    
    def test_volume_up(self):
        self.tv1 = Television()
        #OFF, VOL INC
        self.tv1.volume_up()
        self.assertEqual(self.tv1.__str__(), "Power = False, Channel = 0, Volume = 0")
        #ON, VOL INC
        self.tv1.power()
        self.tv1.volume_up()
        self.assertEqual(self.tv1.__str__(), "Power = True, Channel = 0, Volume = 1")
        #ON< MUTE, VOL INC
        self.tv1.mute()
        self.tv1.volume_up()
        self.assertEqual(self.tv1.__str__(), "Power = True, Channel = 0, Volume = 2")
        #ON, VOL INC PAST MAX
        self.tv1.volume_up()
        self.assertEqual(self.tv1.__str__(), "Power = True, Channel = 0, Volume = 2")
        
    
    
    def test_volume_down(self):
        self.tv1 = Television()
        
        #OFF, VOL DOWN
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.power()
        self.tv1.volume_down()
        self.assertEqual(self.tv1.__str__(), "Power = False, Channel = 0, Volume = 1")
        
        #ON, VOL DOWN
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        
        self.tv1.volume_down()
        self.assertEqual(self.tv1.__str__(), "Power = True, Channel = 0, Volume = 1")
        
        #ON, MUTED, VOL DOWN
        self.tv1.mute()
        self.tv1.volume_down()
        self.assertEqual(self.tv1.__str__(), "Power = True, Channel = 0, Volume = 0")
        
        
    
"""

if __name__ == "main":
    unittest.main()