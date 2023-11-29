from setuptools import setup, find_packages

setup(
  name='scorebook',
  version='0.1.0',
  packages=find_packages(),
  install_requires=[
      # 依存するライブラリがあればここに追加
  ],
  entry_points={
    'console_scripts': [
        # コマンドラインスクリプトがあればここに追加
    ],
  },
  author='Kotaro Saito',
  author_email='saikota0314@gmail.com',
  description='A Python library for handling and analyzing baseball score data.',
  long_description='A Python library for handling and analyzing baseball score data. The library provides classes and functions to model and manipulate baseball game data, including innings, plays, players, and teams. It supports the creation, modification, and analysis of scorebooks, making it easy to extract insights from baseball game records. Whether you are building a baseball analytics tool or simply want to manage and analyze your own scorebooks, this library simplifies the process of working with baseball data.',
  long_description_content_type='text/markdown',
  url='https://github.com/kotaitos/scorebook',
  license='MIT',  # 適切なライセンスを選択
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'Natural Language :: Japanese',
    'Typing :: Typed',
  ],
)