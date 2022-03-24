from setuptools import setup, find_packages
from pip._internal.req import parse_requirements

VERSION = '2.0.0' 
DESCRIPTION = 'DefiasMessengerBot'
LONG_DESCRIPTION = 'El DefiasMessengerBot es un Bot que envía el último print screen a un canal de Discord.'

# Setting up
setup(
        name="defiasmessengerbot", 
        version=VERSION,
        author="Rodrigo Maranzana",
        author_email="maranzana.roddrigo@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[str(ir.requirement) for ir in parse_requirements('requirements.txt', session='hack')],
        
        keywords=['discord', 'bot', 'wow', 'world', 'warcraft', 'images', 'print', 'screen'],
        classifiers= [
            "Development Status :: 1 - Stable",
            "Intended Audience :: Gaming",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)