from setuptools import find_packages, setup

setup(name='hearthstone_card_generator',
    version='1.4',
    description='Generates completely random hearthstone cards (random mana cost, attack, health, name, and a description generated using markov chains from existing descriptions)',
    url='https://github.com/maymike321/hearthstone_card_generator',
    author='Michael May',
    author_email='yamekim@comcast.net',
    packages=find_packages(exclude=("test")),
    license='MIT',
    install_requires=['pyykov'],
    test_suite='hearthstone_card_generator.hearthstone-card-generator-test.py',
    zip_safe=False)