_classifiers = [
    'Development Status :: 4 - Beta',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities',
]

if __name__ == '__main__':
    from setuptools import setup
    import sdeck

    desc = 'Read and write Stream Deck profiles'

    setup(
        name='sdeck',
        version=sdeck.__version__,
        author='Tom Ritchford',
        author_email='tom@swirly.com',
        url='https://github.com/rec/sdeck',
        py_modules=['sdeck'],
        description=desc,
        long_description=open('README.rst').read(),
        license='MIT',
        classifiers=_classifiers,
        keywords=['dataclass'],
    )
