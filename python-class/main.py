from airtravel import console_card_printer, make_flight
from pprint import pprint as pp

f, g = make_flight()
f.make_boarding_cards(console_card_printer)

print("OUTRO VOO")

g.make_boarding_cards(console_card_printer)

