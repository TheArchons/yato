set shell := ["powershell.exe", "-c"] # uncomment to use powershell

build:
    rm -r dist
    pip install . --upgrade
    python setup.py sdist
    python setup.py bdist_wheel
    twine upload dist/*