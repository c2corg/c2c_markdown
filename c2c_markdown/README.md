## Parsing the custom formating syntax of camptocamp.org

### Syntax

Camptocamp.org markdown to format the documents text attributes. It used bases features of [Python-Markdown](https://github.com/waylan/Python-Markdown). 

Upon these features, other custom tags are added : 

* LTag `L# | 6a | tremendous pitch`
* Emojis `:smile:`
* images `[img=123]Legend[/img]`
* toc `[toc]`
* alerts `!!!! This is an alert banner`
* wikilinks `[[routes/123|Walker ridge]]`
* custom headers `## Approach # 10 mn`
* ptag (hard new line) `[p]` 
* video `[video]https://youtube.com/123[/video]`

### Sanitizer

Output is cleaned from any XXS injection using [Mozilla Bleach](https://github.com/mozilla/bleach)

### Rialability

This parser has been tested and fuzzed (~100,000,000 tests). Issues has also been found on python markdown and bleach: [1](https://github.com/mozilla/bleach/issues/352), [2](https://github.com/Python-Markdown/markdown/issues/643), [3](https://github.com/Python-Markdown/markdown/issues/640) and [4](https://github.com/Python-Markdown/markdown/issues/639) :sunglasses:.
