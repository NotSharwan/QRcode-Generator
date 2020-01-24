# QRcode-Generator
pyqrcode
================================
The pyqrcode module is a QR code generator that is simple to use and written
in pure python. The module can automates most of the building process for
creating QR codes. Most codes can be created using only two lines of code!

Unlike other generators, all of the helpers can be controlled manually. You are
free to set any or all of the properties of your QR code.

QR codes can be saved as SVG, XBM, EPS, PNG (by using the
[pypng](https://pypi.python.org/pypi/pypng/) module), or plain text. They can
also be displayed directly in most Linux terminal emulators and Tkinter. PIL
is not used to render the image files.

The pyqrcode module attempts to follow the QR code standard as closely as
possible. The terminology and the encodings used in pyqrcode come directly
from the standard. This module also follows the algorithm laid out in the
standard.

Requirements
-------------------------

The pyqrcode module only requires Python 2.6, Python 2.7, or Python 3. You may
want to install pypng in order to render PNG files, but it is optional.

Installation
------------

Installation is simple. It can be installed from pip using the following
command:

```bash
$ pip install pyqrcode
```

Or from the code

```bash
$ python setup.py install
```

