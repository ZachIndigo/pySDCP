# from distutils.core import setup
from setuptools import setup

setup(
    name='pySDCP',
    version='1.0.0',
    packages=['pysdcp'],
    url='https://github.com/ZachIndigo/pySDCP',
    license='MIT',
    author='Zachary Smith',
    author_email='mailto@zachir.xyz',
    description='SDCP library to control Sony Projectors',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
         'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3',
)
