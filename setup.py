from setuptools import setup, find_packages


test_deps = ["pytest"]

extras = {
    "testing": test_deps
}

setup(
    name = "skeleton",
    author = "Jonathan Keane",
    author_email = "jkeane@gmail.com",
    description = "",
    license = "MIT",
    version = "0.2.5",
    classifiers = ['Development Status :: 1 - Planning',
                   'Intended Audience :: Developers'],
    packages = find_packages(where="src"),
    package_dir = {"": "src"},
    include_package_data=True,
    namespace_packages = ["skeleton"],
    install_requires = ["setuptools"],
    tests_require = test_deps,
    extras_require = extras
)
