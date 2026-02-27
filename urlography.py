#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  urlography.py
#
#  This generates an HTML unordered list of all the URLs in a given HTML file,
#  to be included at the end as a "bibliography" of sorts.
#
#  See:
#      http://docopt.org/
#      https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#
#  Copyright 2018 Kevin Cole <kevin.cole@novawebdevelopment.org> 2018.09.08
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with this program; if not, write to the Free
#  Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301, USA.
#
#

"""Usage:
    urlography <source.html> [-o <destination.html>]
    urlography (-h | --help | --version)

"""

import os
import sys
from os.path  import expanduser      # Cross-platform home directory finder
from bs4      import BeautifulSoup   # HTML parser
from docopt   import docopt          # command line option / argument parser


__appname__    = "URLography"
__module__     = ""
__author__     = "Kevin Cole"
__copyright__  = "Copyright \N{copyright sign} 2018"
__agency__     = "NOVA Web Development"
__credits__    = ["Kevin Cole"]  # Authors and bug reporters
__license__    = "GPL"
__version__    = "1.0"
__maintainer__ = "Kevin Cole"
__email__      = "kevin.cole@novawebdevelopment.org"
__status__     = "Prototype"  # "Prototype", "Development" or "Production"

# Unicode silliness to avoid NameError exeptions
#
if   sys.version_info.major == 2: stringTypes = basestring,
elif sys.version_info.major == 3: stringTypes = str,


def main():
    """The main"""

    _ = os.system("clear")
    print("{0} v.{1}\n{2} ({3})\n{4}, {5} <{6}>\n"
          .format(__appname__,
                  __version__,
                  __copyright__,
                  __license__,
                  __author__,
                  __agency__,
                  __email__))

    options = """Options:
    --version                     print version info and exit
    -h, --help                    print this help message and exit
    -o, --out=<destination.html>  save text to 'destination.html'
                                  [default: sys.stdout]
    """

    cli = docopt(__doc__ + options)

    with open(cli["<source.html>"], "r") as html:
        soup = BeautifulSoup(html, "html5lib")

    if cli["--out"] != "sys.stdout":
        if os.path.isfile(cli["--out"]):
            yorn = input("Overwrite {0}? (Y/N) [N]: ".format(cli["--out"]))
            if yorn.lower() == "n":
                sys.exit(1)
        destination = open(cli["--out"], "w")
    else:
        destination = sys.stdout

    destination.write("""\n<div id="links" style="font-size:13px; page-break-inside:avoid;">""")
    destination.write("""\n<hr>""")
    destination.write("""\n<h3>Links</h3>""")
    destination.write("""\n<ol>""")

    entry  = """\n<li>{0}<br>"""
    entry += """\n<a class="a" """
    entry += """\n   href="{1}">{1}</a></li>"""

    for link in soup.find_all('a'):
        href = link.get("href")
        if link.string and not href.startswith("mailto:"):
            destination.write(entry.format(link.string, href))

    destination.write("\n</ol>\n</div>\n")
    return 0


if __name__ == "__main__":
    main()
