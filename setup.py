from setuptools import setup, find_packages

intall_requires = [
    'pandas>=0.18.1',
    'numpy>=1.11.0'
]


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='letcodeExercies',
    packages =find_packages(exclude=['tests','tests.*','demo','demo.*']),
    version='0.1',
    license=license,
    author='Chandler Song',
    install_requires=intall_requires,
    author_email='chandler605@outlook.com',
    long_description=readme,
    description='My Exercises code of leetcode'
)
