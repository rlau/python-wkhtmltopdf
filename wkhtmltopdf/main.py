#!/usr/bin/env python
import os
import optparse

from subprocess import Popen
from subprocess import PIPE


class WKOption(object):
    """Build an option to be used throughout"""
    def __init__(self, name, shortcut, otype=str, action=None, dest=None,
            default=None, help=None, validate=None, validate_error=None):
        self.name = name
        self.shortcut = shortcut
        self.otype = bool if (default is True or default is False) else otype
        self.action = "store_true" if self.otype is bool else "store"
        self.dest = dest if dest else name.replace('-', '_')
        self.default = default
        self.help = help
        self._validate = validate
        self.validate_error = validate_error

        # we're going to want to get the values in here
        self.value = None

    def validate(self):
        if self.validate is None:
            return True

        # only try to validate if we have a function to do so
        if self.validate(self.value):
            return True
        else:
            return False, self.validate_error

    def long(self):
        return '--' + self.name.replace('_', '-')

    def to_cmd(self):
        """Return the str() of this command, bool is just --long, etc"""
        if self.otype is bool:
            if self.value:
                return self.long()
            else:
                return ""
        else:
            return " ".join([self.long(), str(self.value)
                            if self.value is not None else ""])


ARGUMENTS_PDF = ['enable_plugins',
                'disable_javascript',
                'no_background',
                'grayscale',
                'redirect_delay',
                'orientation',
                'dpi',
                'username',
                'password',
                'margin_bottom',
                'margin_top',
                'margin_left',
                'margin_right',
                'disable_smart_shrinking']

OPTIONS_PDF = [
    WKOption('enable-plugins', '-F',
                 default=False,
                 help="use flash and other plugins",
                 ),
    WKOption('disable-javascript', '-J',
                 default=False,
                 help="disable javascript",
                 ),
    WKOption('no-background', '-b',
                 default=False,
                 help="do not print background",
                 ),
    WKOption('grayscale', '-g',
                 default=False,
                 help="make greyscale",
                 ),
    WKOption('redirect-delay', '-d',
                 default=0,
                 help="page delay before conversion",
                 ),
    WKOption('orientation', '-O',
                 default="Portrait",
                 help="page orientation",
                 validate=lambda x: x in ['Portrait', 'Landscape'],
                 validate_error="Orientation argument must be either Portrait or Landscape"
                 ),
    WKOption('dpi', '-D',
                 default=100,
                 help="print dpi",
                 ),
    WKOption('username', '-U',
                 default="",
                 help="http username",
                 ),
    WKOption('password', '-P',
                 default="",
                 help="http password",
                 ),
    WKOption('margin-bottom', '-B',
                 default=10,
                 help="bottom page margin, default 10mm",
                 ),
    WKOption('margin-top', '-T',
                 default=10,
                 help="top page margin, default 10mm",
                 ),
    WKOption('margin-left', '-L',
                 default=10,
                 help="left page margin, default 10mm",
                 ),
    WKOption('margin-right', '-R',
                 default=10,
                 help="right page margin, default 10mm",
                 ),
    WKOption('disable-smart-shrinking', None,
                 default=False,
                 help="Disable the intelligent shrinking strategy used by WebKit that makes the pixel/dpi ratio none constant",
                 ),
]
ARGUMENTS_IMG = ['crop_h',
                'crop_w',
                'crop_x'
                'crop_y',
                'custom_header',
                'custom_header_propagation',
                'encoding',
                'format',
                'height',
                'no_images',
                'disable_javascript',
                'javascript_delay',
                'load_error_handling',
                'disable_local_file_access',
                'minimum_font_size',
                'password',
                'enable_plugins',
                'post',
                'proxy',
                'quality',
                'run_script',
                'no_stop_slow_scripts',
                'user_style_sheet',
                'username',
                'width',
                'zoom']
OPTIONS = [
    WKOption('crop-h', None,
                default=0,
                help='set height for cropping'),
    WKOption('crop-w', None,
                default=0,
                help='set width for cropping'),
    WKOption('crop-x', None,
                default=0,
                help='set x-coordinate for cropping'),
    WKOption('crop-y', None,
                default=0,
                help='set y-coordinate for cropping'),
    WKOption('custom-header', None,
                default="",
                help='Set an additional http header'),
    WKOption('custom-header-propagation', None,
                default=False,
                help='allow http headers specified by custom-header for each resource request'),
    WKOption('encoding', None,
                default="",
                help='set the default text encoding for input'),
    WKOption('format', '-f',
                default='jpg',
                help='set the output file format'),
    WKOption('height', None,
                default=0,
                help='Set screen height (default is calculated from page content)'),
    WKOption('no-images', None,
                default=False,
                help='Do not load images'),
    WKOption('disable-javascript', '-n',
                default=False,
                help='Do not allow web pages to allow javascript'),
    WKOption('javascript-delay', None,
                default=200,
                help='Wait some number of milliseconds for javascript to finish'),
    WKOption('load-error-handling', None,
                default="abort",
                validate=lambda x: x in ['abort', 'ignore', 'skip'],
                validate_error="Error handling argument must be abort, ignore or skip"),
    WKOption('disable-local-file-access', None,
                default=False,
                help='Do not allow conversion of a local file to read in other local files'),
    WKOption('minimum-font-size', None,
                default=0,
                help='Set a minimum font size'),
    WKOption('password', None,
                default="",
                help='HTTP authentication password'),
    WKOption('enable-plugins', None,
                default=False,
                help='Enable installed plugins (though plugins will likely not work)'),
    WKOption('post', None,
                default="",
                help='Add an additional post field, format is <name> <value>'),
    WKOption('proxy', '-p',
                default="",
                help='set proxy'),
    WKOption('quality', None,
                default=94,
                help='Output image quality, integer between 0 and 100'),
    WKOption('run-script', None,
                default="",
                help='Run additional javascript after the page is done loading'),
    WKOption('no-stop-slow-scripts', None,
                default=False,
                help='do not stop slow running javascripts'),
    WKOption('user-style-sheet', None,
                default="",
                help='Specify a url to a given style sheet that should load with every page'),
    WKOption('username', None,
                default="",
                help='Specify username for HTTP authentication'),
    WKOption('width', None,
                default=1024,
                help='set screen width in pixels'),
    WKOption('zoom', None,
                default=1.0,
                help='set a zoom factor (float)')
]


class WKhtmlToPdf(object):
    """
    Convert an html page via its URL into a pdf.
    """
    def __init__(self, *args, **kwargs):
        self.url = None
        self.output_file = None
        self.params = []
        self.pdf=False
        self.OPTIONS = OPTIONS if self.pdf is False else OPTIONS_PDF

        # get the url and output_file options
        try:
            self.url, self.output_file = args[0], args[1]
            print self.url
            print self.output_file
            if '.pdf' in self.output_file:
                self.pdf=True
        except IndexError:
            pass

        for arg in kwargs.viewkeys():
            if (arg not in ARGUMENTS_PDF and self.pdf is True) or (arg not in ARGUMENTS_IMG and self.pdf is False):
                raise Exception("Provided an invalid argument.  Please check for spelling errors.")

        if not self.url or not self.output_file:
            raise Exception("Missing url and output file arguments")

        # save the file to /tmp if a full path is not specified
        output_path = os.path.split(self.output_file)[0]
        if not output_path:
            self.output_file = os.path.join('/tmp', self.output_file)

        # set the options per the kwargs coming in
        for o in self.OPTIONS:
            if kwargs.get(o.dest) is not None:
                o.value = kwargs.get(o.dest)
                self.params.append(o.to_cmd())

        # self.params = [o.to_cmd() for o in OPTIONS]
        self.screen_resolution = [1024, 768]
        self.color_depth = 24

    def render(self):
        """
        Render the URL into a pdf and setup the evironment if required.
        """

        # setup the environment if it isn't set up yet
        if not os.getenv('DISPLAY'):
            os.system("Xvfb :0 -screen 0 %sx%sx%s & " % (
                self.screen_resolution[0],
                self.screen_resolution[1],
                self.color_depth
            ))
            os.putenv("DISPLAY", '127.0.0.1:0')

        # execute the command
        # change up depending on how the configuraiton is installed
        command = './wkhtmltoimage' if self.pdf == False else 'wkhtmltopdf-0.9.9-OS-X.i368'
        print command
        # prevents spacing errors
        print self.params
        if len(self.params) > 0:
            command += " " + " ".join([cmd for cmd in self.params])
        
        command +=' %s %s >> /tmp/wkhtp.log' % ( self.url, self.output_file)

        try:
            p = Popen(command, shell=True,
                        stdout=PIPE, stderr=PIPE, close_fds=True)
            stdout, stderr = p.communicate()
            retcode = p.returncode

            if retcode == 0:
                # call was successful
                return
            elif retcode < 0:
                raise Exception("terminated by signal: ", -retcode)
            else:
                raise Exception(stderr)

        except OSError, exc:
            raise exc


def wkhtmltopdf(*args, **kwargs):
    wkhp = WKhtmlToPdf(*args, **kwargs)
    wkhp.render()


if __name__ == '__main__':

    # parse through the system argumants
    usage = "Usage: %prog [options] url output_file"
    parser = optparse.OptionParser()

    for o in OPTIONS:
        if o.shortcut:
            parser.add_option(o.shortcut, o.long(),
                              action=o.action,
                              dest=o.dest,
                              default=o.default,
                              help=o.help)
        else:
            parser.add_option(o.long(),
                              action=o.action,
                              dest=o.dest,
                              default=o.default,
                              help=o.help)

    options, args = parser.parse_args()

    # call the main method with parsed argumants
    wkhtmltopdf(*args, **options.__dict__)
