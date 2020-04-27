import setuptools


setuptools.setup(
    name='my_package',
    packages=setuptools.find_packages(),
    version='1.0.0',
    description='Say Hello',
    long_description="""
        A very lightway package which
        says hello from the datapao team.
    """,
    long_description_content_type='text/plain',
    license='CC-BY-NC-SA-4.0',
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'my_entry_point=my_package.my_module:main_function'
            ]}
)
