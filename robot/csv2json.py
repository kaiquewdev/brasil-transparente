#!/usr/bin/env python
# coding: utf-8
import csv
import simplejson as json
import codecs
import sys

# arguments
args = sys.argv

if len( args ) == 3:
    output = []
    csvfile = codecs.open( args[1], 'r')
    content = csvfile.read()
    csvfile.close()

    content = unicode( content, errors='replace' )
    content = content.split('\n')

    output = [row.split(';') for row in content]

    if len( output ) > 0 and args[2]:
        file_json = codecs.open( args[2], 'w' )
        file_json.write( json.dumps( output ) )
        file_json.close()

        print 'Complete!'
    else:
        print 'Sorry, try again!'
