from random import randint

dicesides = {
    1: ("⏐       ⏐\n")+("⏐   ✱   ⏐\n")+("⏐       ⏐\n"),
    2: ("⏐ ✱     ⏐\n")+("⏐       ⏐\n")+("⏐     ✱ ⏐\n"),
    3: ("⏐ ✱     ⏐\n")+("⏐   ✱   ⏐\n")+("⏐     ✱ ⏐\n"),
    4: ("⏐ ✱   ✱ ⏐\n")+("⏐       ⏐\n")+("⏐ ✱   ✱ ⏐\n"),
    5: ("⏐ ✱   ✱ ⏐\n")+("⏐   ✱   ⏐\n")+("⏐ ✱   ✱ ⏐\n"),
    6: ("⏐ ✱   ✱ ⏐\n")+("⏐ ✱   ✱ ⏐\n")+("⏐ ✱   ✱ ⏐\n")}

def roll():
	rndint = randint(1, 6)
	print(dicesides[rndint])
	return rndint





