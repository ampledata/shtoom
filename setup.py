
from distutils.core import setup

from shtoom import Version

# patch distutils if it can't cope with the "classifiers" keyword.
# this just makes it ignore it.
import sys
if sys.version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None

setup(
    name = "shtoom",
    version = Version,
    description = "Shtoom - SIP softphone",
    author = "Anthony Baxter",
    author_email = "anthony@interlink.com.au",
    url = 'http://sourceforge.net/projects/shtoom/',
    packages = ['shtoom', 'shtoom/multicast', 
                'shtoom/ui', 'shtoom/ui/qtui'],
    scripts = ['shtoom.py'],
    classifiers = [
       'Development Status :: 3 - Alpha',
       'License :: OSI Approved :: Python Software Foundation License',
       'Operating System :: POSIX',
       'Programming Language :: Python',
       'Topic :: Internet',
       'Topic :: System :: Networking',
    ]

)