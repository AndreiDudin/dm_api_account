from setuptools import setup, find_packages
REQUIRES = [
    'requests',
    'pydantic',
    'allure-pytest',
    'restclient'
]
setup(
    name='dm_api_account',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/AndreiDudin/dm_api_account.git',
    license='MIT',
    author='Andrey Dudin',
    author_email='.',
    install_requires=REQUIRES,
    description='dm_api_account'
)
