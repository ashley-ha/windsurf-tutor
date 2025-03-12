https://developer.mozilla.org/en-US/docs/Web/API/Node# Node - Web APIs | MDN
Baseline

Widely available \*

The [DOM](https://developer.mozilla.org/en-US/docs/Glossary/DOM) **`Node`** interface is an abstract base class upon which many other DOM API objects are based, thus letting those object types to be used similarly and often interchangeably. As an abstract class, there is no such thing as a plain `Node` object. All objects that implement `Node` functionality are based on one of its subclasses. Most notable are [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document), [`Element`](https://developer.mozilla.org/en-US/docs/Web/API/Element), and [`DocumentFragment`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment).

In addition, every kind of DOM node is represented by an interface based on `Node`. These include [`Attr`](https://developer.mozilla.org/en-US/docs/Web/API/Attr), [`CharacterData`](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData) (which [`Text`](https://developer.mozilla.org/en-US/docs/Web/API/Text), [`Comment`](https://developer.mozilla.org/en-US/docs/Web/API/Comment), [`CDATASection`](https://developer.mozilla.org/en-US/docs/Web/API/CDATASection) and [`ProcessingInstruction`](https://developer.mozilla.org/en-US/docs/Web/API/ProcessingInstruction) are all based on), and [`DocumentType`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentType).

In some cases, a particular feature of the base `Node` interface may not apply to one of its child interfaces; in that case, the inheriting node may return `null` or throw an exception, depending on circumstances. For example, attempting to add children to a node type that cannot have children will throw an exception.

EventTarget Node

[Instance properties](#instance_properties)
-------------------------------------------

_In addition to the properties below, `Node` inherits properties from its parent, [`EventTarget`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget)_.

[`Node.baseURI`](https://developer.mozilla.org/en-US/docs/Web/API/Node/baseURI) Read only

Returns a string representing the base URL of the document containing the `Node`.

[`Node.childNodes`](https://developer.mozilla.org/en-US/docs/Web/API/Node/childNodes) Read only

Returns a live [`NodeList`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList) containing all the children of this node (including elements, text and comments). [`NodeList`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList) being live means that if the children of the `Node` change, the [`NodeList`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList) object is automatically updated.

[`Node.firstChild`](https://developer.mozilla.org/en-US/docs/Web/API/Node/firstChild) Read only

Returns a `Node` representing the first direct child node of the node, or `null` if the node has no child.

[`Node.isConnected`](https://developer.mozilla.org/en-US/docs/Web/API/Node/isConnected) Read only

A boolean indicating whether or not the Node is connected (directly or indirectly) to the context object, e.g. the [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document) object in the case of the normal DOM, or the [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot) in the case of a shadow DOM.

[`Node.lastChild`](https://developer.mozilla.org/en-US/docs/Web/API/Node/lastChild) Read only

Returns a `Node` representing the last direct child node of the node, or `null` if the node has no child.

[`Node.nextSibling`](https://developer.mozilla.org/en-US/docs/Web/API/Node/nextSibling) Read only

Returns a `Node` representing the next node in the tree, or `null` if there isn't such node.

[`Node.nodeName`](https://developer.mozilla.org/en-US/docs/Web/API/Node/nodeName) Read only

Returns a string containing the name of the `Node`. The structure of the name will differ with the node type. E.g. An [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) will contain the name of the corresponding tag, like `'AUDIO'` for an [`HTMLAudioElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAudioElement), a [`Text`](https://developer.mozilla.org/en-US/docs/Web/API/Text) node will have the `'#text'` string, or a [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document) node will have the `'#document'` string.

[`Node.nodeType`](https://developer.mozilla.org/en-US/docs/Web/API/Node/nodeType) Read only

Returns an `unsigned short` representing the type of the node. Possible values are:


|Name                       |Value|
|---------------------------|-----|
|ELEMENT_NODE               |1    |
|ATTRIBUTE_NODE             |2    |
|TEXT_NODE                  |3    |
|CDATA_SECTION_NODE         |4    |
|PROCESSING_INSTRUCTION_NODE|7    |
|COMMENT_NODE               |8    |
|DOCUMENT_NODE              |9    |
|DOCUMENT_TYPE_NODE         |10   |
|DOCUMENT_FRAGMENT_NODE     |11   |


[`Node.nodeValue`](https://developer.mozilla.org/en-US/docs/Web/API/Node/nodeValue)

Returns / Sets the value of the current node.

[`Node.ownerDocument`](https://developer.mozilla.org/en-US/docs/Web/API/Node/ownerDocument) Read only

Returns the [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document) that this node belongs to. If the node is itself a document, returns `null`.

[`Node.parentNode`](https://developer.mozilla.org/en-US/docs/Web/API/Node/parentNode) Read only

Returns a `Node` that is the parent of this node. If there is no such node, like if this node is the top of the tree or if doesn't participate in a tree, this property returns `null`.

[`Node.parentElement`](https://developer.mozilla.org/en-US/docs/Web/API/Node/parentElement) Read only

Returns an [`Element`](https://developer.mozilla.org/en-US/docs/Web/API/Element) that is the parent of this node. If the node has no parent, or if that parent is not an [`Element`](https://developer.mozilla.org/en-US/docs/Web/API/Element), this property returns `null`.

[`Node.previousSibling`](https://developer.mozilla.org/en-US/docs/Web/API/Node/previousSibling) Read only

Returns a `Node` representing the previous node in the tree, or `null` if there isn't such node.

[`Node.textContent`](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent)

Returns / Sets the textual content of an element and all its descendants.

[Instance methods](#instance_methods)
-------------------------------------

_In addition to the methods below, `Node` inherits methods from its parent, [`EventTarget`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget)._

[`Node.appendChild()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild)

Adds the specified `childNode` argument as the last child to the current node. If the argument referenced an existing node on the DOM tree, the node will be detached from its current position and attached at the new position.

[`Node.cloneNode()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/cloneNode)

Clone a `Node`, and optionally, all of its contents. By default, it clones the content of the node.

[`Node.compareDocumentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/compareDocumentPosition)

Compares the position of the current node against another node in any other document.

[`Node.contains()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/contains)

Returns `true` or `false` value indicating whether or not a node is a descendant of the calling node.

[`Node.getRootNode()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/getRootNode)

Returns the context object's root which optionally includes the shadow root if it is available.

[`Node.hasChildNodes()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/hasChildNodes)

Returns a boolean value indicating whether or not the element has any child nodes.

[`Node.insertBefore()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/insertBefore)

Inserts a `Node` before the reference node as a child of a specified parent node.

[`Node.isDefaultNamespace()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/isDefaultNamespace)

Accepts a namespace URI as an argument and returns a boolean value with a value of `true` if the namespace is the default namespace on the given node or `false` if not.

[`Node.isEqualNode()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/isEqualNode)

Returns a boolean value which indicates whether or not two nodes are of the same type and all their defining data points match.

[`Node.isSameNode()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/isSameNode)

Returns a boolean value indicating whether or not the two nodes are the same (that is, they reference the same object).

[`Node.lookupPrefix()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/lookupPrefix)

Returns a string containing the prefix for a given namespace URI, if present, and `null` if not. When multiple prefixes are possible, the result is implementation-dependent.

[`Node.lookupNamespaceURI()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/lookupNamespaceURI)

Accepts a prefix and returns the namespace URI associated with it on the given node if found (and `null` if not). Supplying `null` for the prefix will return the default namespace.

[`Node.normalize()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/normalize)

Clean up all the text nodes under this element (merge adjacent, remove empty).

[`Node.removeChild()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/removeChild)

Removes a child node from the current element, which must be a child of the current node.

[`Node.replaceChild()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/replaceChild)

Replaces one child `Node` of the current one with the second one given in parameter.

[Examples](#examples)
---------------------

### [Remove all children nested within a node](#remove_all_children_nested_within_a_node)

This function remove each first child of an element, until there are none left.

```
function removeAllChildren(element) {
  while (element.firstChild) {
    element.removeChild(element.firstChild);
  }
}

```


Using this function is a single call. Here we empty the body of the document:

```
removeAllChildren(document.body);

```


An alternative could be to set the textContent to the empty string: `document.body.textContent = ""`.

### [Recurse through child nodes](#recurse_through_child_nodes)

The following function recursively calls a callback function for each node contained by a root node (including the root itself):

```
function eachNode(rootNode, callback) {
  if (!callback) {
    const nodes = [];
    eachNode(rootNode, (node) => {
      nodes.push(node);
    });
    return nodes;
  }

  if (callback(rootNode) === false) {
    return false;
  }

  if (rootNode.hasChildNodes()) {
    for (const node of rootNode.childNodes) {
      if (eachNode(node, callback) === false) {
        return;
      }
    }
  }
}

```


The function recursively calls a function for each descendant node of `rootNode` (including the root itself).

If `callback` is omitted, the function returns an [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) instead, which contains `rootNode` and all nodes contained within.

If `callback` is provided, and it returns `false` when called, the current recursion level is aborted, and the function resumes execution at the last parent's level. This can be used to abort loops once a node has been found (such as searching for a text node which contains a certain string).

The function has two parameters:

[`rootNode`](#rootnode)

The `Node` object whose descendants will be recursed through.

[`callback` Optional](#callback)

An optional callback [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function) that receives a `Node` as its only argument. If omitted, `eachNode` returns an [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of every node contained within `rootNode` (including the root itself).

The following demonstrates a real-world use of the `eachNode()` function: searching for text on a web-page.

We use a wrapper function named `grep` to do the searching:

```
function grep(parentNode, pattern) {
  let matches = [];
  let endScan = false;

  eachNode(parentNode, (node) => {
    if (endScan) {
      return false;
    }

    // Ignore anything which isn't a text node
    if (node.nodeType !== Node.TEXT_NODE) {
      return;
    }

    if (typeof pattern === "string" && node.textContent.includes(pattern)) {
      matches.push(node);
    } else if (pattern.test(node.textContent)) {
      if (!pattern.global) {
        endScan = true;
        matches = node;
      } else {
        matches.push(node);
      }
    }
  });

  return matches;
}

```


[Specifications](#specifications)
---------------------------------


|Specification       |
|--------------------|
|DOM # interface-node|


[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser