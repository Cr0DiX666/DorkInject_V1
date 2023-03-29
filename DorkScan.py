# Code by : Cr0DiXZeroTeeN7_
# Datetime: Maret, 29, 2023 - 18:26:23 WIB
# Facebook: RadenMasKiAcuy
from googlesearch import search
from enum import Enum
x = '\033[0m'
u = '\033[4m'
R = '\033[1;91m'
r = '\033[0;91m'
g = '\033[0;92m'
y = '\033[0;33m'
w = '\033[0;37m'
print ("""


 _____     ______     ______     __  __     __     __   __       __     ______     ______     ______     
/\  __-.  /\  __ \   /\  == \   /\ \/ /    /\ \   /\ "-.\ \     /\ \   /\  ___\   /\  ___\   /\__  _\    
\ \ \/\ \ \ \ \/\ \  \ \  __<   \ \  _"-.  \ \ \  \ \ \-.  \   _\_\ \  \ \  __\   \ \ \____  \/_/\ \/    
 \ \____-  \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\  \ \_\\"\_\ /\_____\  \ \_____\  \ \_____\    \ \_\    
  \/____/   \/_____/   \/_/ /_/   \/_/\/_/   \/_/   \/_/ \/_/ \/_____/   \/_____/   \/_____/     \/_/    
                                                                                                         

   {w}>> {u}Codename:{x} {u}Cr0DiXZeroTeeN7_{x} {R}
""")
try:
	ny1 = input(f" {r}{u}Dork{w}:{x} {y}")
	ny2 = int(input(f" {r}{u}Page{w}:{x} {y}"))
	ny3 = int(input(f" {r}{u}Time{w}:{x} {y}"));print('')
	nyx = 0
	for i in search(ny1, tld="com", lang="en", num=int(ny2), start=0, stop=None, pause=int(ny3)):
		with open('results.txt', 'a') as f:
			f.write(f'{i}\n')
		nyx += 1
		print(f'{w}{nyx}) {g}{i}')
		if nyx >= int(ny2):
			break;
	print(f'\n{w}Saved: {g}results.txt')
except ValueError:
	exit(f' {r}{u}Exit{w}! {y}input error')
except KeyboardInterrupt:
	exit(f'\n {r}{u}Exit{w}! {y}thanks for using;)')