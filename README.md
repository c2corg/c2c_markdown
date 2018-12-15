## c2c_markdown

![Build](https://travis-ci.org/c2corg/c2c_markdown.svg?branch=master)

Build upon [Python Markdown](https://github.com/Python-Markdown/markdown), this repo is the core markdown parser for camptocamp.org

## How to contribute ?

Assuming that you have Python 3.4 or 3.5, and git installed : 

``` bash 
git clone https://github.com/c2corg/c2c_markdown.git
cd c2c_markdown
pip install -r requirements.txt -r dev-requirements.txt

# add a couple .md/.html files into test folders

python -m unittests tests/test_format.py
```


