from setuptools import setup, find_packages


setup(
    name='slack-webhook-cli',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests'],
    author='Philipp Bosch',
    author_email='hello@pb.io',
    license='MIT',
    url='https://github.com/philippbosch/slack-webhook-cli',
    scripts=['slack.py'],
    entry_points={
        'console_scripts': [
            'slack = slack:main'
        ]
    },
)
