#!/usr/bin/env python
import os
import sys

'''
Codeline -- version 1.0
Used to summarize the lines of source code in C
'''
suffix = ['.c', '.h']
othermod = '*other*'

def filelines(fobj, skipblank):
	count = 0
	for line in fobj:
		if skipblank and len(line.strip()) == 0:
			continue
		count += 1
	return count

def codelines(fname):
	if os.path.isdir(fname):
		count = 0
		for subdname in os.listdir(fname):
			count += codelines(os.path.join(fname, subdname))
		return count
	elif os.path.isfile(fname) and \
		os.path.splitext(fname)[1] in suffix:
		f = open(fname)
		count = filelines(f, 1)
		f.close()
		return count
	else:
		return 0

def main():
	if len(sys.argv) == 1:
		print 'Usage:', sys.argv[0], 'dir1, dir2, ...'
		sys.exit()

	total_lines = 0
	for dname in sys.argv[1:]:
		modules = {othermod : 0}

		for subdname in os.listdir(dname):
			fname = os.path.join(dname, subdname)
			count = codelines(fname)
			total_lines += count 

			if os.path.isdir(fname):
				modules[subdname] = count
			else:
				modules[othermod] += count 

		print '%10s%-20s%10s' %(10*'-', dname.center(20), 10*'-') 

		msorted = sorted(modules.iteritems(), key = lambda x : x[1],
				reverse = True)
		for i, (m, lines) in enumerate(msorted):
			print '%-3d%-20s%d' %(i, m, lines) 

		print 40*'-'
		print

	print 'Total:', total_lines

if __name__ == '__main__':
	main()
