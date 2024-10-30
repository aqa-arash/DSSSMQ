from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    py_modules=['math_quiz'],
    install_requires=[
        random,
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz:math_quiz',
        ],
    },
    author='Arash Moradian',
    author_email='moradian.arash@gmail.com',
    description='A debugged math quiz game with unit tests',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aqa-arash/DSSSMQ',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)