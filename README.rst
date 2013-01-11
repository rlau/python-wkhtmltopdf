python-wkhtmltopdf
==================
A simple python wrapper for the wkhtmltopdf lib (http://code.google.com/p/wkhtmltopdf/) with flash support.

Requirements
------------

System:
~~~~~~~

- Linux 32/64 or OSX only (Windows is not supported at this stage)
- Xvfd
- wkhtmltopdf
- flashplugin-nonfree
- python 2.5+

Installation
------------

wkhtmltopdf
~~~~~~~~~~~

1. Install Xvfd::

    $ sudo apt-get install xvfb
    
2. Install Fonts::

    $ sudo apt-get install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic
    
3. Install wkhtmltopdf::
        
    $ sudo apt-get install wkhtmltopdf
    
4. Install flashplugin::
        
    $ sudo apt-get install flashplugin-nonfree

python-wkhtmltopdf
~~~~~~~~~~~~~~~~~~

1. From git::

    $ git clone git@github.com:rlau/python-wkhtmltopdf.git
    $ cd python-wkhtmltopdf
    $ python setup.py install

Usage
-----

Simple Usage::
~~~~~~~~~~~~~~

1. Use from class::
    
    from wkhtmltopdf import WKHtmlToPdf
    
    wkhtmltopdf = WKHtmlToPdf(
        'http://www.example.com',
        '~/example.pdf',
    )
    wkhtmltopdf.render()
        
2. Use from method::
        
    from wkhtmltopdf import wkhtmltopdf
    
    wkhtmltopdf('example.com', '~/example.pdf')
        
3. Use from commandline (installed)::
        
    $ python -m wkhtmltopdf.main example.com ~/example.pdf
        
4. Use the api (installed)::
        
    $ python -m wkhtmltopdf.api &   
    $ wget http://localhost:8888/?url=example.com&output_file=example.pdf
        
Required Arguments:
~~~~~~~~~~~~~~~~~~~

- **url** - the url or file path of the html you wish to convert
- **output_file** - the file that you want to create. Filetypes: .pdf, .jpg, .png (possibly others as well)
        
Optional Arguments:
~~~~~~~~~~~~~~~~~~~

PDF Options:
- **screen_resolution** (default: [1024, 768])
- **color_depth** (default: 24 (bit))
- **flash_plugin** (default: True)
- **disable_javascript** (default: False)
- **delay** (default: 0 (millisecs))
- **orientation** (default: Portrait)
- **dpi** (default: 100)
- **no_background** (default: False)
- **grayscale** (default: False)
- **http_username** (default: None)
- **http_password** (default: None)

Image Options:
To be completed    
