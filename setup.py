# ----------------------
#  ls.joyous
# ----------------------

import codecs
from setuptools import setup, find_packages


setup(name="ls.joyous",
      use_scm_version={
          'write_to':  "ls/joyous/_version.py",
      },
      description="A calendar application for Wagtail.",
      long_description=codecs.open("README.rst", encoding="utf-8").read(),
      keywords=["calendar", "events", "wagtail", "groupware"],
      classifiers=["Development Status :: 4 - Beta",
                   "Framework :: Django",
                   "Framework :: Django :: 1.11",
                   "Framework :: Django :: 2.0",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 3",
                   "Topic :: Office/Business :: Groupware",
                   "Topic :: Office/Business :: Scheduling",
                   "Topic :: Software Development :: Libraries :: Python Modules"
                  ],
      platforms="any",
      author="David Moore",
      author_email="david@linuxsoftware.co.nz",
      url="https://github.com/linuxsoftware/ls.joyous",
      license="BSD",
      packages=find_packages(where=".", exclude=["ls.joyous.tests"]),
      setup_requires=["setuptools_scm"],
      install_requires=["python-dateutil", "inflect", "holidays"],
      tests_require=["coverage", "django-beautifulsoup-test"],
      #include_package_data=True,
      test_suite="ls.joyous.tests",
      zip_safe=False,
     )
