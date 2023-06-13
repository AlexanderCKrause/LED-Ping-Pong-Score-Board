#!/usr/bin/env python3

# Test Client application.
#
# This program attempts to connect to all previously verified Flic buttons by this server.
# Once connected, it prints Down and Up when a button is pressed or released.
# It also monitors when new buttons are verified and connects to them as well. For example, run this program and at the same time the scan_wizard.py program.

import fliclib
from game import PingPongGame
from api_calls import *

client = fliclib.FlicClient("localhost")

def click_handler(channel, click_type, was_queued, time_diff):

  game = get_game_info()

  if str(click_type) == "ClickType.ButtonSingleClick":
    if str(channel.bd_addr) == game.player1:
        increment_score('player1', game)
    elif str(channel.bd_addr) == game.player2:
        increment_score('player2', game)

  if str(click_type) == "ClickType.ButtonDoubleClick":
    if str(channel.bd_addr) == game.player1:
        decrement_score('player1', game)
    elif str(channel.bd_addr) == game.player2:
        decrement_score('player2', game)

  if str(click_type) == "ClickType.ButtonHold":
    if str(channel.bd_addr) == game.player1:
        reset_score('player1', game)
    elif str(channel.bd_addr) == game.player2:
        reset_score('player2', game)

# Flick Button Event Handling
def got_button(bd_addr):
	cc = fliclib.ButtonConnectionChannel(bd_addr)
	cc.on_button_single_or_double_click_or_hold = click_handler

	cc.on_connection_status_changed = \
		lambda channel, connection_status, disconnect_reason: \
			print(channel.bd_addr + " " + str(connection_status) + (" " + str(disconnect_reason) if connection_status == fliclib.ConnectionStatus.Disconnected else ""))
	client.add_connection_channel(cc)

def got_info(items):
	for bd_addr in items["bd_addr_of_verified_buttons"]:
		got_button(bd_addr)

client.get_info(got_info)
client.on_new_verified_button = got_button
client.handle_events()
