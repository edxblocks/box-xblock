"""Setup for box XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='box-xblock',
    version='1.0',
    description='An XBlock for creating coloured boxed content',
    license='AGPL v3',
    packages=[
        'box',
    ],
    install_requires=[
        'XBlock',
        'xblock-utils'
    ],
    entry_points={
        'xblock.v1': [
            'box = box:BoxXBlock',
        ]
    },
    package_data=package_data("box", ["static", "public"]),
)
