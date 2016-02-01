from setuptools import setup, find_packages

version = __import__('slack').get_version()

setup(
    name='slack-webhook-cli',
    description='Send messages to Slack from the command line',
    version=version,
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
