
from distutils.core import setup
setup(
  name = 'z43_styles',
  packages = ['z43_styles'],
  version = '0.1',
  license='MIT',
  description = 'Z43 plotly templates',
  author = 'Odei Maiz',
  author_email = 'maiz@itis.swiss',
  url = 'https://github.com/odeimaiz/z43_plot_styles',
  download_url = 'https://github.com/odeimaiz/z43_plot_styles/archive/v_01.tar.gz',
  keywords = ['PLOTLY', 'TEMPLATES', 'Z43'],
  install_requires=[
    'plotly',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)