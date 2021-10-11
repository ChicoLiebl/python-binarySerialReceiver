from distutils.core import setup
setup(
  name = 'binarySerialReceiver',
  packages = ['binarySerialReceiver'],
  version = '0.1',
  license='MIT',
  description = 'Simple module for receiving binary data from a serial port',
  author = 'Francisco Liebl',
  author_email = 'chicolliebl@gmail.com',
  url = 'https://github.com/ChicoLiebl/python-binarySerialReceiver.git',
  download_url = 'https://github.com/ChicoLiebl/python-binarySerialReceiver/archive/v_01.tar.gz',
  keywords = ['SERIAL', 'PORT', 'RECEIVER', 'BINARY', 'THREADED', 'BACKGROUND'],
  install_requires=[
          'numpy',
          'pyserial',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)