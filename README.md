# dcbookstoprisoners.org

This is a static version of DC Books to Prisons Drupal site.

## Testing locally

Before deploying changes to a live site, you may wish to test the
site. The Python programming language, which comes standard on Linux
and Mac OS X systems, and can be downloaded and installed on Windows
systems, comes equipped with a mini-web server that listens to web
browser requests and responds by attempting to answer the requests.

### Start the mini-web server

First determine if you have Python 2.x or Python 3.x on your system,
by opening a terminal window and typing:

    python

Make a note of which version is reported back to you. You can then
exit Python by typing `Ctrl-D` or `exit()`. Then, depending upon which
version:

* **Python 3**

  `python -m http.server 8000`

* **Python 2**

  `python -m SimpleHTTPServer 8000`

### Browse your site

While Python is still running, open a browser and go to either
http://localhost:8000 or http://127.0.0.1:8000 and you should
see your web site.

### Shut down

When finished exploring, go back to your terminal window and type
`Ctrl-C` to stop the web server -- or simply close your terminal
session, which will kill Python.

(Note that while the Python mini-web server is running, the terminal
window will report messages regarding what files the web browser has
requested, and how the mini-web server responded to those
requests. You can ignore all of that.)

### Editing cycle

Since this site is now maanged via a "distributed revision control
system" with multiple editors, care must be taken to ensure that one
set of edits does not interfere with another set of edits.

Distributed revision control systems rely on each contributor having
a separate copy (called a "clone") of the master documents. Everyone
can edit their copy independently, and then submit their edits for
review, which then gets merged back into the master documents.

Without going into a lot of detail, the general sequence for editing is:

    $ git pull               # retrieves updates from master repository
    $ git log                # view a record of what has been changed
    [edit doc_1]             # edit any document
	[edit doc_2]             # edit another
	...
	$ git status             # show the state of all changed documents
	$ git add doc_1          # mark this document as ready to be included
	$ git checkout -- doc_2  # undo changes to doc_2
	$ git commit             # commit changes, provide a reason
	[edit doc_2]             # edit the second document again
	$ git status             # check the current state of all documents
	$ git add doc_2          # mark doc_2 as ready for inclusion
	$ git commit             # commit changes, provide a reason
	$ git push               # send changes to the master repository

The `pull` and `push` do not retrieve and send entire documents. Instead,
they retrieve and send the changes to documents.

Edit in "logical" sessions: In other words, don't make lots and lots
of unrelated changes. Suppose, for example, you have three tasks which
can be stated as

* change the date for an event
* revise orientation documentation
* add a new page about important prison policy change

Consider those as three very separate edits.  Start with the `git
pull` to make sure you have the latest and greatest version of
everything. Complete the first task then `git add` and `git commit`.
Repeat the edit, `git add` and `git commit` for the second and third
tasks. And then, finally, `git push` to push your changes out for
others. (You can also do the `git push` after every commit if you wish.)
The idea is that your commits provide a summary of what has been changed,
and, if necessary, what must be undone.  Each commit is considered a
revision and all of the edits made between one commit and the next can
be rewound back to previous versions.

## URLography

`urlography.py` is a new (as of 2018.09.09) feature. It generates
the list of links that is placed at the end of the newsletters.

In order to use it on your systems there is a wee bit of setup
involved.

1. First, ensure you have `Python 3` installed. The latest stable
   version is `Python 3.7.0 (default, Jul 15, 2018, 10:44:58)` but any
   `Python 3` should do.
2. The python modules `lxml`, `bs4` a.k.a. `Beautiful Soup 4`, and
   `docopt` need to be installed and accessible to Python 3.
3. Although not strictly necessary, it is probably best to put
   `urlography.py` in your `~/bin/` directory or somewhere else
   within your system path, and make it an executable with
   `chmod 755 urlography.py`. Optionally, creating a symlink
   or alias to it might be nice.
   
### Usage

    urlography.py <source.html> [-o <destination.html>]

This will read the file `<source.html>` and save the _urlography_
(think "bibliography") to `<destination.html>`. If the optional `-o
...` is not present, the urlography will be sent to the standard
output (typically your screen).
