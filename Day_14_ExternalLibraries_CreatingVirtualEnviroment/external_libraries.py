# Python has a rich ecosystem of libraries, and you can install them using pip.
# libraries written by other people, that you can use in your project.
# idea - do not reinvent the wheel, use libraries written by other people.
#
# pip is a package manager for Python packages, or modules if you like.
# A package contains all the files you need for a module.
# Modules are Python code libraries you can include in your project.

# most popular package manager for Python is pip.
# packages can be found at https://pypi.org/
# pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4
# To install a package, open the Command Prompt, and tell pip to install the package you want.
# example of simple package installation:
# pretty print - pip install pprint
# pip install camelcase
# Now we can use the camelcase module, which has a capitalize() method that can capitalize text, like this:
# import camelcase
# c = camelcase.CamelCase()   
# txt = "hello world this is a test" # so is and a are not capitalized 
# print(c.hump(txt))

# to remove a package, use the uninstall command:
# pip uninstall camelcase

# what does pip stand for?
# pip is a recursive acronym that can stand for either "Pip Installs Packages" or "Pip Installs Python".
# but most commonly it is known as "Pip Installs Packages".

# to see current list of installed packages, use the list command:
# pip list

# so why do we need a package manager?
# if you are using a package manager, you can easily install packages from a central place, and easily manage dependencies.
# a dependency is a piece of software that another piece of software needs to work.
# for example, the camelcase package depends on the pyparsing package, which is another package that needs to be installed.
# so if you install the camelcase package, pip will automatically install the pyparsing package for you.
