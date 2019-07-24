import os
import subprocess
import distutils.log
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py
from setuptools.command.install import install as _install


with open("project") as f:
    PACKAGE_NAME = f.read().strip()

with open("version") as f:
    VERSION = f.read().strip()

with open('requirements.txt') as f:
    INSTALL_REQUIRES = [
        x.strip('\n')
        for x in f.readlines()
        if x and x[0] != '#'
    ]

SHORT_DESCRIPTION = "Agora - Service Portfolio Management Tool"

PACKAGES_ROOT = 'agora'
PACKAGES = find_packages(PACKAGES_ROOT)

# Package meta
CLASSIFIERS = [
    "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    ]


def get_all_data_files(dest_path, source_path):
    dest_path = dest_path.strip('/')
    source_path = source_path.strip('/')
    source_len = len(source_path)
    return [
        (
            os.path.join(dest_path, path[source_len:].strip('/')),
            [os.path.join(path, f) for f in files],
        )
        for path, _, files in os.walk(source_path)
    ]


UI_DATA_FILES = get_all_data_files('lib/agora/www/ui', 'ui/dist')

AGORA_TEMPLATE_FILES = get_all_data_files('lib/agora/resources/templates',
                                           'agora/templates')


class BuildUiCommand(_build_py):
    """ Extend build_py to build Agora UI. """

    description = 'build Agora UI'
    user_options = _build_py.user_options + [
        ('no-ui', None, 'skip Agora UI build'),
    ]

    boolean_options = _build_py.boolean_options + ['no-ui']

    def initialize_options(self):
        """ Set default values for options. """

        _build_py.initialize_options(self)
        self.no_ui = None

    def run(self):

        if not self.no_ui:
            command = ['./build_ui.sh', 'production']
            self.announce('building ui: %s' % ' '.join(command),
                          level=distutils.log.INFO)
            subprocess.call(command, cwd='./ui/')

        _build_py.run(self)


class InstallCommand(_install):
    """ Extend install command with --no-build-ui option. """

    user_options = _install.user_options + [
        ('no-build-ui', None, 'skip Agora UI build'),
    ]

    boolean_options = _install.boolean_options + ['no-build-ui']

    def initialize_options(self):
        """ Set default values for options. """

        _install.initialize_options(self)
        self.no_build_ui = None

    def run(self):
        if self.no_build_ui:
            self.reinitialize_command('build_py', no_ui=True)

        _install.run(self)


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=SHORT_DESCRIPTION,
    classifiers=CLASSIFIERS,
    packages=PACKAGES,
    package_dir={'': PACKAGES_ROOT},
    data_files=[
        ('lib/agora/resources',
         [
             'agora/resources/common.json',
         ]),
        ('lib/travel/scripts', ['scripts/agora_init.sh']),
    ] + UI_DATA_FILES + AGORA_TEMPLATE_FILES,
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,

    entry_points={
        'console_scripts': [
            'agora = agora.manage:main',
        ],
    },
    cmdclass={'install': InstallCommand, 'build_py': BuildUiCommand},
)
