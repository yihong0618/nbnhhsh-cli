from setuptools import setup, find_packages

VERSION = "0.1.1"

setup(
    name="hhsh",
    version=VERSION,
    description="能不能好好说话？ cli",
    long_description="能不能好好说话？ cli",
    keywords="python hhsh cli terminal",
    author="itorr,yihong0618",
    author_email="zouzou0208@gmail.com",
    url="https://github.com/yihong0618/hhsh",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=["requests", "rich"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
    ],
    entry_points={
        "console_scripts": ["hhsh = hhsh.hhsh:main"],
    },
)
