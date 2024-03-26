from setuptools import setup
REQUIRES = [
    'requests',
    'pydantic',
    'allure-pytest',
    'restclient'
]
setup(
    name='dm_api_account',
    version='0.0.1',
    packages=['dm_api_account'],
    url='https://github.com/AndreiDudin/dm_api_account.git',
    license='MIT',
    author='Andrey Dudin',
    author_email='.',
    install_requires=REQUIRES,
    description='dm_api_account'
)