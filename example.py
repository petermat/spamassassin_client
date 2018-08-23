#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# Copyright (C) 2018  Peter Matkovski <p.matkovski@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Example program using SpamAssasin"""
import os

from spamassasin import SpamAssassin

FILES = [dict(type='spam', name='sample-spam.txt'),
         dict(type='ham', name='sample-nonspam.txt')]

def main():

    path = os.path.dirname(__file__)
    for test in FILES:
        filename = os.path.join(path, test['name'])
        with open(filename,"rb") as f:            
            print("\nProcessing file: {}".format(filename))        
            assassin = SpamAssassin(f.read())
            print(assassin)            
            if assassin.is_spam():
                print("The received message is considered spam with a score of {0}".format(assassin.get_score()))
            print('\nreport_fulltext:', assassin.get_fulltext())
            print('score:', assassin.get_score())
            print('report_json:', assassin.get_report_json())

if __name__ == "__main__":
    main()
