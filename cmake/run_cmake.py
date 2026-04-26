'''
This file is part of Telegram Desktop,
the official desktop application for the Telegram messaging service.

For license and copyright information please follow this link:
https://github.com/telegramdesktop/tdesktop/blob/master/LEGAL
'''
import sys, os, subprocess

def run(scriptName, arguments):
    workingPath = os.getcwd()
    try:
        # Execute cmake with the provided arguments
        result = subprocess.call(['cmake'] + arguments)
        return result
    except Exception as e:
        print('[ERROR] Failed to run cmake: ' + str(e))
        return 1
