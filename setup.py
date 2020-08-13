from distutils.core import setup
setup(
  name = 'novusspace',
  packages = ['novusspace'],
  version = '0.1',
  license='MIT',
  description = 'Module for novus space software',
  author = 'novus-alex',
  author_email = 'alexandre@hachet.com',
  url = 'https://novussapce.inovaperf.me',
  download_url = 'https://github.com/novus-alex/novus-module/archive/0.1.tar.gz',
  keywords = ['NOVUS', 'SPACE', 'PROJECT'],
  install_requires=[
          'shutil',
          'requests',
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
  ],
)
