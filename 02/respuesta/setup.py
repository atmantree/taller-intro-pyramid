from setuptools import setup

requires = [
    'pyramid',
]

setup(name='app',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = app:main
      """,
)


