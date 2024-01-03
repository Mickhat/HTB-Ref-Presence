from pypresence import Presence
import time

client_id = '1132040868589748344' # Leave it 
RPC = Presence(client_id)
RPC.connect()

buttons = [{"label": "Join Hack The Box", "url": "https://affiliate.hackthebox.com/mickhat1337"}, # Change your name here
           {"label": "Join HTB Academy", "url": "https://affiliate.hackthebox.com/mickhat"}] # Change your name here too

RPC.update(details="Join Hack The Box Today!", # Feel free to change description
           large_image="cube_icon_rgb_1024",
           large_text="Hack The Box",
           buttons=buttons)

while True:
    time.sleep(5)
