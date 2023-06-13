# PyPI stands for Python Package Index and is the official third-party software repository for Python
# PyPI is a central repository for maintaining Python packages that have been developed and shared by the Python community
# To install packages from PyPI, most developers use a program called pip
# Not all of them are useful, some of them a buggy and incomplete, so need to search for stable versions of packages that are needed

# with the help of pip it is possible to install the latest or necessary versions of packages, in video example was with requests package
# command for updating pip version iin win is "python -m pip install --upgrade pip"
# command to install a package is just "pip install (name of a package)"
# then need to read the documantation of the package on its website to be able to use it correctly

import requests

response = requests.get("https://google.com")
print(response) # <Response [200]> result means it is successful