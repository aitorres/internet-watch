# coding=utf-8
from __future__ import division
import os
import datetime

def ping():
	hostname = "google.com"
	response = os.system("ping -c 1 " + hostname + " > /dev/null 2>&1")
	return response

def count_numbers(n, l):
	c = 0
	for i in range(0, len(l)):
		if l[i] == n:
			c = c+1
	return c

def scan_network(l, n):
	del l[:]
	for i in range(0, n):
		l.append(ping())

def count_results(l):
	a = count_numbers(0, l)
	b = count_numbers(256, l)
	return a, b, len(l) - (a+b)

def was_online():
	file = open("status.txt", "r")
	status = file.readline()
	file.close()
	return status == "online"

def write_status(s):
	file = open("status.txt", "w")
	file.write(s)
	file.close()
	return

def write_to_registry(s, o, l, e, t, tt):
	file = open("registry.md", "a")
	file.write("### Status change: " + ("online" if s else "offline") + "\n")
	file.write("Change occured at " + t + " with " + str(o) + " correct hits, " + str(l) + " lost pings and other " + str(e) + " errors, of a total of " + str(tt) + " tries." + "\n\n")

def is_online(ok, tries):
	return ((ok/tries)*100) >= 75

def main():
	pings = list()
	tries = 10
	scan_network(pings, tries)

	now = datetime.datetime.now()
	time = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " " + str(now.hour) + ":" + str(now.minute)

	oks, losts, errors = count_results(pings)
	current_status = is_online(oks, tries)
	previous_status = was_online()

	if current_status != previous_status:
		if current_status:
			write_status("online")
		else:
			write_status("offline")
		write_to_registry(current_status, oks, losts, errors, time, tries)

if __name__ == "__main__":
    main()
