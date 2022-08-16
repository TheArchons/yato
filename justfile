set shell := ["powershell.exe", "-c"] # uncomment to use powershell

build:
    pip install . --upgrade

dist:
    rm -r dist
    python setup.py sdist
    python setup.py bdist_wheel
    twine upload dist/*