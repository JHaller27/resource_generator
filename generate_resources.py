# Author: James Haller

import random
import sys


def get_category_lists() -> list:
	return [
		["raw", "manufactured"],
		["conflict", "contested", None, None],
		["up-cycle", "down-cycle", "re-cycle"]
	]


def get_resource_list() -> list:
	return ["lumber", "steel", "stone", "grain", "textile", "iron", "clay", "gold", "gems", "copper", "silver", "drink", "livestock", "magic", "paper"]


def get_description() -> tuple:
	l = [random.choice(get_resource_list())]
	for c in get_category_lists():
		x = random.choice(c)
		if x is not None:
			l.append(x)

	return tuple(l)


def r2s(resource: tuple) -> str:
	return "{} ({})".format(resource[0], ", ".join(resource[1:]))


def main():
	count = int(sys.argv[1]) if len(sys.argv) >= 2 else 1
	for _ in range(count):
		print(r2s(get_description()))


if __name__ == "__main__":
	main()

