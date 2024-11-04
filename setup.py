import setuptools 
 
setuptools.setup(
    name="xieyin",
    version="0.0.2",    
    author="Chessom",    
    author_email="chessom@foxmail.com",
    description="Generate Chinese homophonic sentences",
    long_description=
'''
Use function xieyin(yuanwen,pattern,accurate).
Example:

from xieyin import xieyin
xieyin('谐音字符串',pattern=0,accurate=True)

If you are not interested in using it as a model,
you can do this:

from xieyin import main
main()
''',
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    install_requires=["pypinyin","jieba"],
    package_data={
    'xieyin': ['pinmap0.bin','pinmap1.bin']
    }
)
