from setuptools import setup

setup(name='torgo_py',
      version='0.1',
      description='A package for parsing and recreating novels in English',
      url='https://github.com/tsdubose/torgoPY',
      author='Travis DuBose',
      author_email='travis.dubose@rutgers.edu',
      license='MIT',
      packages=['torgo_py'],
      install_requires=['nltk', 'sklearn'],
      zip_safe=False)
