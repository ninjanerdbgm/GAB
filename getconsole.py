"""
===================================================================================
This is where I manually tweak the input to return more
accurate results from duckduckgo and pricecharting.

This is a bit messy, but this bot doesn't have AI yet (which I may work on soon).
Until it can learn to make better searches on its own, this will have to do.
===================================================================================
"""

def getConsole(g,c):
	gam = ""
	con = ""
	g = str(g).lower()
	c = str(c).lower()
	if c and g:
		if c == "snes":
			con = "super nintendo"
		elif c == "nes":
			con = "nintendo nes"
		elif c == "n64":
			con = "nintendo 64"
		elif c == "gcn":
			con = "gamecube"
		elif c == "wii":
			con = "wii"
		elif c == "wiiu":
			con = "wii u"
                elif c == "gb":
                        con = "gameboy"
                elif c == "gbc":
                        con = "gameboy color"
                elif c == "gba":
                        con = "gameboy advance"
                elif c == "nds":
                        con = "nintendo ds"
                elif c == "3ds":
                        con = "nintendo 3ds"
                elif c == "vb":
                        con = "virtual boy"
                elif c == "psx":
                        con = "playstation"
                elif c == "ps2":
                        con = "playstation 2"
                elif c == "ps3":
                        con = "playstation 3"
                elif c == "ps4":
                        con = "playstation 4"
                elif c == "psp":
                        con = "psp"
                elif c == "vita":
                        con = "playstation vita"
                elif c == "sms":
                        con = "sega master system"
                elif c == "genesis":
                        con = "sega genesis"
                elif c == "scd":
                        con = "sega cd"
                elif c == "32x":
                        con = "sega 32x"
                elif c == "saturn":
                        con = "sega saturn"
                elif c == "dc":
                        con = "sega dreamcast"
                elif c == "gg":
                        con = "sega game gear"
                elif c == "xbox":
                        con = "xbox"
                elif c == "360":
                        con = "xbox 360"
                elif c == "xbone":
                        con = "xbox one"
                elif c == "2600":
                        con = "atari 2600"
                elif c == "5200":
                        con = "atari 5200"
                elif c == "7800":
                        con = "atari 7800"
                elif c == "400" or "800":
                        con = "atari 400"
                elif c == "lynx":
                        con = "atari lynx"
                elif c == "jaguar":
                        con = "atari jaguar"
                elif c == "skylanders":
                        con = "skylanders"
                elif c == "infinity":
                        con = "disney infinity"
                elif c == "3do":
                        con = "3do"
                elif c == "cdi":
                        con = "cd-i"
                elif c == "coleco":
                        con = "colecovision"
                elif c == "intellivision":
                        con = "intellivision"
                elif c == "mac":
                        con = "macintosh"
                elif c == "ngage":
                        con = "n-gage"
                elif c == "neogeo":
                        con = "neo geo"
                elif c == "ngpc":
                        con = "neo geo pocket color"
                elif c == "o2":
                        con = "odyssey 2"
                elif c == "pc":
                        con = "pc games"
                elif c == "turbogfx":
                        con = "turbografx-16"
                elif c == "vectrex":
                        con = "vectrex"
                elif c == "v20":
                        con = "vic-20"
		else:
			con = "Error"
	else:
		con = None
	if g == "":
                if c == "nes":
			con = "045496610104" 
                if c == "72nes":
			gam = "72 pin connector" 
                if c == "tlnes":
			con = "045496610043" 
                if c == "snes":
			con = "045496810016" 
                if c == "msnes":
			con = "077678014066" 
                if c == "n64":
			con = "045496850012" 
                if c == "cblackn64":
			con = "045496850586" 
                if c == "cbluen64":
			con = "045496850531" 
                if c == "cgreenn64":
			con = "045496850548" 
                if c == "corangen64":
			con = "045496850562" 
                if c == "credn64":
			gam = "atomic red nintendo 64 system" 
                        con = "nintendo 64"
                if c == "goldn64":
			con = "045496850975" 
                if c == "cpurplen64":
			con = "045496850579" 
                if c == "pikachun64":
			con = "045496850883" 
                if c == "n64xp":
			gam = "w/ expansion pak" 
                        con = "nintendo 64"
                if c == "blackgcn":
			con = "045496940027" 
                if c == "gcn":
			con = "045496940003" 
                if c == "panaq":
			gam = "q gamecube console" 
                        con = "gamecube"
                if c == "platgcn":
			con = "045496940393" 
                if c == "xdgcn":
			con = "045496941789" 
                if c == "blackwii":
			con = "045496880163" 
                if c == "bluewii":
			gam = "blue nintendo wii system" 
                        con = "wii"
                if c == "redwii":
			con = "045496880354" 
                if c == "wii":
			con = "045496880019" 
                if c == "wiiu":
			con = "045496880859" 
                if c == "wiiudx":
			con = "045496880866" 
                if c == "wiiumk8":
			gam = "deluxe: mario kart 8 edition" 
                        con = "wii u"
                if c == "wiiuml":
			gam = "deluxe: mario & luigi edition" 
                        con = "wii u"
                if c == "wiiuww":
			gam = "deluxe: zelda wind waker edition" 
			con = "wii u"
                if c == "wiiuzomu":
			gam = "deluxe: zombiu edition" 
                        con = "wii u"
                if c == "gbpblack":
			con = "045496710330" 
                if c == "gbpblue":
			con = "045496710477" 
                if c == "gbpkiwi":
			con = "051500287002" 
                if c == "gbpgreen":
			con = "045496710309" 
                if c == "gb":
			con = "050400103368" 
                if c == "gbpyellow":
			con = "045496710323" 
                if c == "gbcberry":
			con = "045496710774" 
                if c == "gbcpcrystal":
			con = "045496712426" 
                if c == "gbc":
			gam = "gameboy color system" 
                        con = "gameboy color"
                if c == "gbcgreen":
			con = "045496710781" 
                if c == "gbcpokemon":
			gam = "pokemon special edition gameboy color" 
                        con = "gameboy color"
                if c == "gbcsew":
			gam = "w/ izek sewing machine" 
                        con = "gameboy color"
                if c == "gbcyellow":
			con = "045496710798" 
                if c == "gbaspbs":
			con = "045496715496" 
                if c == "gba":
			gam = "black gameboy advanced system" 
                        con = "gameboy advance"
                if c == "gbasp":
			con = "045496716738" 
                if c == "gbaspblue":
			con = "045496713843" 
                if c == "gbaspfamicom":
			gam = "famicom gameboy advance sp" 
                        con = "gameboy advance"
                if c == "gbafushia":
			gam = "fushia gameboy advanced system" 
                        con = "gameboy advance"
                if c == "gbamicro":
			con = "045496717216" 
		if c == "gbaglacier":
			con = "045496713362"
                if c == "gbaspgold":
			gam = "gold gameboy advance sp"
                        con = "gameboy advance"
                if c == "gbaindigo":
                        gam = "indigo gameboy advanced system"
                        con = "gameboy advance"
                if c == "gbasplo":
                        gam = "lime and orange gameboy advance sp"
                        con = "gameboy advance"
                if c == "gbasplime":
                        con = "045496715533"
                if c == "gbaspnes":
                        con = "045496715694"
                if c == "gbaorange":
                        gam = "orange gameboy advanced system"
                        con = "gameboy advance"
                if c == "gbasppblue":
                        con = "045496716707"
                if c == "gbasppwhite":
                        con = "045496716127"
                if c == "gbasppink":
                        gam = "pink gameboy advance sp"
                        con = "gameboy advance"
                if c == "gbaplatinum":
                        gam = "platinum gameboy advanced system"
                        con = "gameboy advance"
                if c == "gbaspplat":
                        con = "045496440992"
                if c == "gbared":
			gam = "red gameboy advanced system"
                        con = "gameboy advance"
                if c == "gbaspred":
                        con = "045496714512"
                if c == "gbaspsblue":
                        con = "045496715892"
                if c == "gbawhite":
			gam = "white gameboy advanced system"
                        con = "gameboy advance"
		if c == "dsi":
			con = "045496718749"
		if c == "dsl":
			con = "045496717742"
		if c == "dsblue":
			con = "045496716394"
		if c == "dsiblue":
			con = "045496718763"
		if c == "dslbb":
			con = "045496718350"
		if c == "cpnds":
			con = "045496717759"
		if c == "cbdsl":
			con = "045496718251"
		if c == "zeldads":
			con = "045496718114"
		if c == "greendsi":
			con = "045496719159"
		if c == "ghnds":
			con = "047875954199"
		if c == "ibdsl":
			con = "045496718602"
		if c == "mbdsi":
			con = "045496718886"
		if c == "mrdsl":
			con = "045496718459"
		if c == "silverdsl":
			con = "045496718466"
		if c == "bluedsixl":
			con = "045496719005"
		if c == "bronzedsixl":
			con = "045496718909"
		if c == "burgdsixl":
			con = "045496718916"
		if c == "reddsixl":
			con = "045496719135"
		if c == "narutodsl":
			gam = "naruto nintendo ds lite limited edition"
			con = "nintendo ds"
		if c == "orangedsi":
			con = "045496719166"
		if c == "pinkdsi":
			con = "045496718794"
		if c == "dogsds":
			con = "045496718138"
		if c == "nds":
			con = "045496716134"
		if c == "pkmnbldsi":
			gam = "pokemon black nintendo dsi system"
			con = "nintendo ds"
		if c == "pkmnwhdsi":
			gam = "pokemon white nintendo dsi system"
			con = "nintendo ds"
		if c == "mariodsl":
			con = "045496718589"
		if c == "mknds":
			con = "045496717056"
		if c == "whitedsi":
			con = "045496718732"
		if c == "whitedsl":
			con = "045496717544"
		if c == "pikachudsl":
			gam = "pikachu nintendo ds lite limited edition"
			con = "nintendo ds"
		if c == "3ds":
			con = "045496719227"
		if c == "zelda3dsxl":
			con = "045496780975"
		if c == "zelda3ds":
			gam = "black zelda limited edition"
			con = "nintendo 3ds"
		if c == "fe3ds":
			gam = "blue fire emblem limited edition"
			con = "nintendo 3ds"
		if c == "black3ds":
			con = "045496719210"
		if c == "purp3ds":
			con = "045496819798"
		if c == "pink3ds":
			con = "045496719753"
		if c == "ml3ds":
			gam = "silver mario & luigi limited edition"
			con = "nintendo 3ds"
		if c == "ac3ds":
			gam = "white animal crossing limited edition"
			con = "nintendo 3ds"
		if c == "3dsxl":
			con = "045496780043"
		if c == "br3dsxl":
			con = "045496780050"
		if c == "mk3dsxl":
			con = "045496780388"
		if c == "pw3dsxl":
			gam = "pink & white"
			con = "nintendo 3ds"
		if c == "xyb3ds":
			con = "045496780906"
		if c == "xyr3ds":
			con = "045496780890"
		if c == "pikachu3dsxl":
			gam = "yellow pikachu limited edition"
			con = "nintendo 3ds"
		if c == "vb":
			con = "045496750015"
		if c == "psx":
			con = "711719401001"
		if c == "ps1":
			gam = "PSOne slim playstation"
			con = "playstation"
		if c == "ps1lcd":
			con = "711719401605"
		if c == "ps2":
			con = "711719701101"
		if c == "ps2ss":
			con = "711719770701"
		if c == "ps2slim":
			con = "711719706403"
		if c == "ps3":
			con = "711719800606"
		if c == "ps3160":
			con = "711719841807"
		if c == "ps320":
			con = "711719800101"
		if c == "ps3320":
			con = "711719841906"
		if c == "ps360":
			con = "711719699651"
		if c == "ps380":
			con = "711719801306"
		if c == "ps3mgs":
			con = "711719801108"
		if c == "ps3s120":
			con = "711719801702"
		if c == "ps3s250":
			con = "711719801801"
		if c == "ps3s500":
			gam = "slim system 500gb"
			con = "playstation 3"
		if c == "ps3sr250":
			gam = "slim redesign system 250gb"
			con = "playstation 3"
		if c == "psp1k":
			con = "683728120436"
		if c == "psp1k1":
			con = "711719850700"
		if c == "psp2kwhite":
			con = "711719889007"
		if c == "pspdaxter":
			con = "711719889106"
		if c == "pspmadden":
			con = "711719889304"
		if c == "psp":
			con = "711719889809"
		if c == "pspgow":
			con = "711719892403"
		if c == "pspgt":
			con = "711719890805"
		if c == "psphm":
			con = "711719889908"
		if c == "pspkh":
			gam = "limited edition kingdom hearts version"
			con = "psp"
		if c == "pspmgs":
			con = "711719892007"
		if c == "psprc":
			con = "711719889403"
		if c == "psprb":
			con = "711719890300"
		if c == "pspsilver":
			con = "711719889601"
		if c == "pspgowhite":
			con = "711719851400"
		if c == "pspgo":
			con = "711719851301"
		if c == "vita":
			con = "711719220312"
		if c == "vita3g":
			con = "711719221319"
		if c == "vitafe":
			con = "711719220565"
		if c == "sms":
			con = "010086030006"
		if c == "genesis":
			con = "010086016109"
		if c == "gen2":
			con = "010086016307"
		if c == "gen3":
			con = "096427010944"
		if c == "cdx":
			gam = "cdx console"
			con = "sega genesis"
		if c == "xeye":
			gam = "jvc x'eye"
			con = "sega genesis"
		if c == "nomad":
			con = "096499102301"
		if c == "scd":
			con = "010086041019"
		if c == "32x":
			con = "010086840018"
		if c == "saturn":
			con = "010086800197"
		if c == "dc":
			con = "010086500004"
		if c == "dcblack":
			con = "600586007921"
		if c == "gamegear":
			gam = "game gear handheld"
			con = "sega game gear"
		if c == "xbox":
			con = "805529688483"
		if c == "xboxhalo":
			con = "000328810121"
		if c == "xboxdew":
			con = "805529333031"
		if c == "360":
			con = "882224035835"
		if c == "360arcade":
			con = "882224519588"
		if c == "360mw3":
			con = "885370327410"
		if c == "360gow":
			con = "885370325348"
		if c == "360halo4":
			gam = "Console Halo 4 edition"
			con = "xbox 360"
		if c == "360halor":
			con = "885370234251"
		if c == "360mw2":
			con = "940356113125"
		if c == "360p60":
			con = "882224729178"
		if c == "360p20":
			con = "882224035811"
		if c == "360sw":
			gam = "console star wars kinect bundle"
			con = "xbox 360"
		if c == "360halo":
			con = "882224509336"
		if c == "360sc":
			con = "885370095333"
		if c == "360re5":
			con = "882224855396"
		if c == "360e120":
			con = "882224390118"
		if c == "360s250":
			con = "885370127119"
		if c == "360s250h":
			con = "885370238907"
		if c == "360s250k":
			con = "885370236095"
		if c == "360s4":
			con = "885370138412"
		if c == "360s4k":
			con = "885370235876"
		if c == "xbone":
			con = "885370702903"
		if c == "xbonetf":
			gam = "console - titanfall limited edition"
			con = "xbox one"
		if c == "2600":
			con = "032700913564"
		if c == "xegs":
			gam = "xegs system"
			con = "atari 2600"
		if c == "5200":
			con = "017167000071"
		if c == "7800":
			gam = "7800 console"
			con = "atari 7800"
		if c == "400":
			gam = "400 game system"
			con = "atari 400"
		if c == "lynx":
			con = "077000504951"
		if c == "jag":
			con = "071843600108"
		if c == "jagcd":
			gam = "jaguar cd system"
			con = "jaguar"
		if c == "3do":
			con = "000000531740"
		if c == "cdi":
			gam = "magnavox cd-i system"
			con = "cd-i"
		if c == "coleco":
			con = "076930024003"
		if c == "c64":
			con = "001781401109"
		if c == "intellivision":
			gam = "intellivision system"
			con = "intellivision"
		if c == "neogeo":
			gam = "neo geo system"
			con = "neo geo"
		if c == "ngcd":
			gam = "neo geo cd system"
			con = "neo geo"
		if c == "ngpc":
			con = "018484520167"
		if c == "odyssey":
			gam = "magnavox oddyssey 2 console"
			con = "odyssey 2"
		if c == "tg16":
			con = "001000002957"
		if c == "tg16cd":
			gam = "turbografx-16 cd system"
			con = "turbografx-16"
		if c == "tx":
			con = "092218001009"
		if c == "tduo":
			gam = "turboduo black console"
			con = "turbografx-16"
		if c == "vic20":
			gam = "vic-20 console"
			con = "vic-20"
	elif "megaman" or "megman" in g:
		gam = g
		gam = gam.replace("megaman", "mega man")
		gam = gam.replace("megman", "mega man")
	elif "halo" in g:
		if g == "halo" or g == "halo ce" or g == "halo: ce":
			gam = g
			gam = gam.replace("halo", "halo: combat evolved")
	else:
		gam = g

	
	return (gam, con)			
