# PACKAGING
cd ex09
python3 -m pip install --upgrade pip
python3 -m pip install build

# Build the package
python3 -m build

# Install one
pip install ./dist/ft_package-0.0.1.tar.gz

## or
pi p install ./dist/ft_package-0.0.1-py3-none-any.whl
## or
pip install -e .

# USEAGE:
## from anywhere
python3 tester.py
