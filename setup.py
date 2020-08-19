import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name='generic-hist-fit-cericdahl',
  version='1.0',
  description='A plugin for fitting generic histograms',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/cericdahl/GenericHistFit',
  author='C.E. Dahl',
  author_email='cdahl@northwestern.edu',
  license='MIT',
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
  install_requires=[
    'numpy',
    'scipy',
  ],
  zip_safe=False)