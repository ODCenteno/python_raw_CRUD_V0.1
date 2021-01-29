from setuptools import setup

setup(
    name='odc',
    version='0.1',
    py_modules=['odc'],
    install_requires=[
        'click',
    ],
    entry_points = '''
        [console_scripts]
        odc=odc:cli
    ''',
)