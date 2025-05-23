from setuptools import setup, find_packages


setup(
    name='cldf_meta',
    version='0.0',
    description='cldf_meta',
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Johannes Englisch',
    author_email='johannes_englisch@t-online.de',
    url='meta.clld.org',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'SQLAlchemy<2.0,>=1.4',  # be explicit about sqlalchemy version
        'clld',
        'clld-glottologfamily-plugin',
        'clldmpg',
        'psycopg2',
        'pycldf[catalogs]',
    ],
    extras_require={
        'dev': ['flake8', 'waitress'],
        'test': [
            'mock',
            'pytest>=5.4',
            'pytest-clld',
            'pytest-mock',
            'pytest-cov',
            'coverage>=4.2',
            'selenium',
            'zope.component>=3.11.0',
        ],
    },
    test_suite="cldf_meta",
    entry_points="""\
        [paste.app_factory]
        main = cldf_meta:main
    """)
