# DOMParser - Web APIs | MDN
Baseline

Widely available

The **`DOMParser`** interface provides the ability to parse [XML](https://developer.mozilla.org/en-US/docs/Glossary/XML) or [HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML) source code from a string into a DOM [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document).

You can perform the opposite operation—converting a DOM tree into XML or HTML source—using the [`XMLSerializer`](https://developer.mozilla.org/en-US/docs/Web/API/XMLSerializer) interface.

In the case of an HTML document, you can also replace portions of the DOM with new DOM trees built from HTML by setting the value of the [`Element.innerHTML`](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML) and [`outerHTML`](https://developer.mozilla.org/en-US/docs/Web/API/Element/outerHTML "outerHTML") properties. These properties can also be read to fetch HTML fragments corresponding to the corresponding DOM subtree.

Note that [`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) can parse XML and HTML directly from a URL-addressable resource, returning a `Document` in its [`response`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/response "response") property.

**Note:** Be aware that [block-level elements](https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content) like `<p>` will be automatically closed if another block-level element is nested inside and therefore parsed before the closing `</p>` tag.

[Constructor](#constructor)
---------------------------

[`DOMParser()`](https://developer.mozilla.org/en-US/docs/Web/API/DOMParser/DOMParser "DOMParser()")

Creates a new `DOMParser` object.

[Instance methods](#instance_methods)
-------------------------------------

[`DOMParser.parseFromString()`](https://developer.mozilla.org/en-US/docs/Web/API/DOMParser/parseFromString)

Parses a string using either the HTML parser or the XML parser, returning an [`HTMLDocument`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDocument) or [`XMLDocument`](https://developer.mozilla.org/en-US/docs/Web/API/XMLDocument).

[Examples](#examples)
---------------------

The documentation for [`DOMParser.parseFromString()`](https://developer.mozilla.org/en-US/docs/Web/API/DOMParser/parseFromString), this interface's only method, contains examples for parsing XML, SVG, and HTML strings.

[Specifications](#specifications)
---------------------------------


|Specification                       |
|------------------------------------|
|HTML # dom-parsing-and-serialization|


[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser

[See also](#see_also)
---------------------