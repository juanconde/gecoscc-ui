import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid==1.5b1',
    'pyramid_jinja2==1.10',
    'pyramid_debugtoolbar==2.0.2',
    'pyramid_beaker==0.7',
    'pyramid_tm==0.7',
    'colander==1.0b1',
    'deform==2.0a2',
    'Babel==1.3',
    'lingua==1.5',
    'pymongo==2.6.3',
    'py-bcrypt==0.4',
    'gunicorn==18.0',
    'celery==3.0.24',
    'celery-with-mongodb==3.0',
    'pyramid_celery==1.3',
    'cornice==0.16.2',
    'jsonschema==2.3.0',
    'gevent==1.0',
    'gevent-websocket==0.9.3',
    'gevent-socketio==0.3.6',
    'redis==2.10.3',
    'WebHelpers==1.3',
    'Paste==1.7.5.1',
    'PyChef==0.2.3',
    'jsonschema==2.3.0',
    'ordereddict==1.1',
    'xmltodict==0.9.0',
    'requests==2.4.3',
    'BeautifulSoup==3.2.1'
]


def get_version():
    with open('gecoscc/version.py') as f:
        for line in f:
            if line.startswith('__VERSION__'):
                return eval(line.split('=')[-1])

setup(name='gecoscc',
      version=get_version(),
      description='gecoscc',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Junta de Andalucia',
      author_email='',
      url='https://github.com/gecos-team',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      package_data={
          'templates': ['*.jinja2', '*.html'],
          'locale': ['*.pot', '*.po', '*.mo'],
          'static': ['*.js', '*.css', '*.jpg', '*.png'],
      },
      install_requires=requires,
      tests_require=requires,
      test_suite="gecoscc",
      entry_points="""\
      [paste.app_factory]
      main = gecoscc:main
      [console_scripts]
      pmanage = gecoscc.management:main
      [gecoscc.policies]
      remote-storage = gecoscc.policies.remote_storage:RemoteStoragePolicy
      """,
      paster_plugins=['pyramid'],
      )
