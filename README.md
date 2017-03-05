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
