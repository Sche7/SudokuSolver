from setuptools import setup


setup(
    name='Sudoku',
    version='1.0',
    author='Steven Cheung',
    author_email='stevencheung7@outlook.dk',
    description='A library that can solve any sudoku board',
    py_modules=[
      'run',
      'sudoku_solver'
    ],
    entry_points='''
        [console_scripts]
        solve=run:main
      '''
)
