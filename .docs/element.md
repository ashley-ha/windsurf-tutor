# Element - Web APIs | MDN
Baseline

Widely available \*

**`Element`** is the most general base class from which all element objects (i.e. objects that represent elements) in a [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document) inherit. It only has methods and properties common to all kinds of elements. More specific classes inherit from `Element`.

For example, the [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) interface is the base interface for HTML elements. Similarly, the [`SVGElement`](https://developer.mozilla.org/en-US/docs/Web/API/SVGElement) interface is the basis for all SVG elements, and the [`MathMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/MathMLElement) interface is the base interface for MathML elements. Most functionality is specified further down the class hierarchy.

Languages outside the realm of the Web platform, like XUL through the `XULElement` interface, also implement `Element`.

EventTarget Node Element

[Instance properties](#instance_properties)
-------------------------------------------

_`Element` inherits properties from its parent interface, [`Node`](https://developer.mozilla.org/en-US/docs/Web/API/Node), and by extension that interface's parent, [`EventTarget`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget)._

[`Element.assignedSlot`](https://developer.mozilla.org/en-US/docs/Web/API/Element/assignedSlot) Read only

Returns a [`HTMLSlotElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSlotElement) representing the [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot) the node is inserted in.

[`Element.attributes`](https://developer.mozilla.org/en-US/docs/Web/API/Element/attributes) Read only

Returns a [`NamedNodeMap`](https://developer.mozilla.org/en-US/docs/Web/API/NamedNodeMap) object containing the assigned attributes of the corresponding HTML element.

[`Element.childElementCount`](https://developer.mozilla.org/en-US/docs/Web/API/Element/childElementCount) Read only

Returns the number of child elements of this element.

[`Element.children`](https://developer.mozilla.org/en-US/docs/Web/API/Element/children) Read only

Returns the child elements of this element.

[`Element.classList`](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList) Read only

Returns a [`DOMTokenList`](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList) containing the list of class attributes.

[`Element.className`](https://developer.mozilla.org/en-US/docs/Web/API/Element/className)

A string representing the class of the element.

[`Element.clientHeight`](https://developer.mozilla.org/en-US/docs/Web/API/Element/clientHeight) Read only

Returns a number representing the inner height of the element.

[`Element.clientLeft`](https://developer.mozilla.org/en-US/docs/Web/API/Element/clientLeft) Read only

Returns a number representing the width of the left border of the element.

[`Element.clientTop`](https://developer.mozilla.org/en-US/docs/Web/API/Element/clientTop) Read only

Returns a number representing the width of the top border of the element.

[`Element.clientWidth`](https://developer.mozilla.org/en-US/docs/Web/API/Element/clientWidth) Read only

Returns a number representing the inner width of the element.

[`Element.currentCSSZoom`](https://developer.mozilla.org/en-US/docs/Web/API/Element/currentCSSZoom) Read only

A number indicating the effective zoom size of the element, or 1.0 if the element is not rendered.

[`Element.elementTiming`](https://developer.mozilla.org/en-US/docs/Web/API/Element/elementTiming) Experimental

A string reflecting the [`elementtiming`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/elementtiming) attribute which marks an element for observation in the [`PerformanceElementTiming`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceElementTiming) API.

[`Element.firstElementChild`](https://developer.mozilla.org/en-US/docs/Web/API/Element/firstElementChild) Read only

Returns the first child element of this element.

[`Element.id`](https://developer.mozilla.org/en-US/docs/Web/API/Element/id)

A string representing the id of the element.

[`Element.innerHTML`](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)

A string representing the markup of the element's content.

[`Element.lastElementChild`](https://developer.mozilla.org/en-US/docs/Web/API/Element/lastElementChild) Read only

Returns the last child element of this element.

[`Element.localName`](https://developer.mozilla.org/en-US/docs/Web/API/Element/localName) Read only

A string representing the local part of the qualified name of the element.

[`Element.namespaceURI`](https://developer.mozilla.org/en-US/docs/Web/API/Element/namespaceURI) Read only

The namespace URI of the element, or `null` if it is no namespace.

**Note:** In Firefox 3.5 and earlier, HTML elements are in no namespace. In later versions, HTML elements are in the [`http://www.w3.org/1999/xhtml`](https://www.w3.org/1999/xhtml/) namespace in both HTML and XML trees.

[`Element.nextElementSibling`](https://developer.mozilla.org/en-US/docs/Web/API/Element/nextElementSibling) Read only

An `Element`, the element immediately following the given one in the tree, or `null` if there's no sibling node.

[`Element.outerHTML`](https://developer.mozilla.org/en-US/docs/Web/API/Element/outerHTML)

A string representing the markup of the element including its content. When used as a setter, replaces the element with nodes parsed from the given string.

[`Element.part`](https://developer.mozilla.org/en-US/docs/Web/API/Element/part)

Represents the part identifier(s) of the element (i.e. set using the `part` attribute), returned as a [`DOMTokenList`](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList).

[`Element.prefix`](https://developer.mozilla.org/en-US/docs/Web/API/Element/prefix) Read only

A string representing the namespace prefix of the element, or `null` if no prefix is specified.

[`Element.previousElementSibling`](https://developer.mozilla.org/en-US/docs/Web/API/Element/previousElementSibling) Read only

An `Element`, the element immediately preceding the given one in the tree, or `null` if there is no sibling element.

[`Element.scrollHeight`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollHeight) Read only

Returns a number representing the scroll view height of an element.

[`Element.scrollLeft`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollLeft)

A number representing the left scroll offset of the element.

[`Element.scrollLeftMax`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollLeftMax) Non-standard Read only

Returns a number representing the maximum left scroll offset possible for the element.

[`Element.scrollTop`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTop)

A number representing number of pixels the top of the element is scrolled vertically.

[`Element.scrollTopMax`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTopMax) Non-standard Read only

Returns a number representing the maximum top scroll offset possible for the element.

[`Element.scrollWidth`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollWidth) Read only

Returns a number representing the scroll view width of the element.

[`Element.shadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/Element/shadowRoot) Read only

Returns the open shadow root that is hosted by the element, or null if no open shadow root is present.

[`Element.slot`](https://developer.mozilla.org/en-US/docs/Web/API/Element/slot)

Returns the name of the shadow DOM slot the element is inserted in.

[`Element.tagName`](https://developer.mozilla.org/en-US/docs/Web/API/Element/tagName) Read only

Returns a string with the name of the tag for the given element.

### [Instance properties included from ARIA](#instance_properties_included_from_aria)

_The `Element` interface also includes the following properties._

[`Element.ariaAtomic`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaAtomic)

A string reflecting the [`aria-atomic`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-atomic) attribute, which indicates whether assistive technologies will present all, or only parts of, the changed region based on the change notifications defined by the [`aria-relevant`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-relevant) attribute.

[`Element.ariaAutoComplete`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaAutoComplete)

A string reflecting the [`aria-autocomplete`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-autocomplete) attribute, which indicates whether inputting text could trigger display of one or more predictions of the user's intended value for a combobox, searchbox, or textbox and specifies how predictions would be presented if they were made.

[`Element.ariaBrailleLabel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaBrailleLabel)

A string reflecting the [`aria-braillelabel`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-braillelabel) attribute, which defines the braille label of the element.

[`Element.ariaBrailleRoleDescription`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaBrailleRoleDescription)

A string reflecting the [`aria-brailleroledescription`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-brailleroledescription) attribute, which defines the ARIA braille role description of the element.

[`Element.ariaBusy`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaBusy)

A string reflecting the [`aria-busy`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-busy) attribute, which indicates whether an element is being modified, as assistive technologies may want to wait until the modifications are complete before exposing them to the user.

[`Element.ariaChecked`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaChecked)

A string reflecting the [`aria-checked`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-checked) attribute, which indicates the current "checked" state of checkboxes, radio buttons, and other widgets that have a checked state.

[`Element.ariaColCount`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaColCount)

A string reflecting the [`aria-colcount`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-colcount) attribute, which defines the number of columns in a table, grid, or treegrid.

[`Element.ariaColIndex`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaColIndex)

A string reflecting the [`aria-colindex`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-colindex) attribute, which defines an element's column index or position with respect to the total number of columns within a table, grid, or treegrid.

[`Element.ariaColIndexText`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaColIndexText)

A string reflecting the [`aria-colindextext`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-colindextext) attribute, which defines a human readable text alternative of aria-colindex.

[`Element.ariaColSpan`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaColSpan)

A string reflecting the [`aria-colspan`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-colspan) attribute, which defines the number of columns spanned by a cell or gridcell within a table, grid, or treegrid.

[`Element.ariaCurrent`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaCurrent)

A string reflecting the [`aria-current`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-current) attribute, which indicates the element that represents the current item within a container or set of related elements.

[`Element.ariaDescription`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaDescription)

A string reflecting the [`aria-description`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-description) attribute, which defines a string value that describes or annotates the current element.

[`Element.ariaDisabled`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaDisabled)

A string reflecting the [`aria-disabled`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-disabled) attribute, which indicates that the element is perceivable but disabled, so it is not editable or otherwise operable.

[`Element.ariaExpanded`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaExpanded)

A string reflecting the [`aria-expanded`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-expanded) attribute, which indicates whether a grouping element owned or controlled by this element is expanded or collapsed.

A string reflecting the [`aria-haspopup`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-haspopup) attribute, which indicates the availability and type of interactive popup element, such as menu or dialog, that can be triggered by an element.

[`Element.ariaHidden`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaHidden)

A string reflecting the [`aria-hidden`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-hidden) attribute, which indicates whether the element is exposed to an accessibility API.

[`Element.ariaKeyShortcuts`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaKeyShortcuts)

A string reflecting the [`aria-keyshortcuts`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-keyshortcuts) attribute, which indicates keyboard shortcuts that an author has implemented to activate or give focus to an element.

[`Element.ariaLabel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaLabel)

A string reflecting the [`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label) attribute, which defines a string value that labels the current element.

[`Element.ariaLevel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaLevel)

A string reflecting the [`aria-level`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-level) attribute, which defines the hierarchical level of an element within a structure.

[`Element.ariaLive`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaLive)

A string reflecting the [`aria-live`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-live) attribute, which indicates that an element will be updated, and describes the types of updates the user agents, assistive technologies, and user can expect from the live region.

[`Element.ariaModal`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaModal)

A string reflecting the [`aria-modal`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-modal) attribute, which indicates whether an element is modal when displayed.

[`Element.ariaMultiline`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaMultiLine)

A string reflecting the [`aria-multiline`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-multiline) attribute, which indicates whether a text box accepts multiple lines of input or only a single line.

[`Element.ariaMultiSelectable`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaMultiSelectable)

A string reflecting the [`aria-multiselectable`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-multiselectable) attribute, which indicates that the user may select more than one item from the current selectable descendants.

[`Element.ariaOrientation`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaOrientation)

A string reflecting the [`aria-orientation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-orientation) attribute, which indicates whether the element's orientation is horizontal, vertical, or unknown/ambiguous.

[`Element.ariaPlaceholder`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaPlaceholder)

A string reflecting the [`aria-placeholder`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-placeholder) attribute, which defines a short hint intended to aid the user with data entry when the control has no value.

[`Element.ariaPosInSet`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaPosInSet)

A string reflecting the [`aria-posinset`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-posinset) attribute, which defines an element's number or position in the current set of listitems or treeitems.

[`Element.ariaPressed`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaPressed)

A string reflecting the [`aria-pressed`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-pressed) attribute, which indicates the current "pressed" state of toggle buttons.

[`Element.ariaReadOnly`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaReadOnly)

A string reflecting the [`aria-readonly`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-readonly) attribute, which indicates that the element is not editable, but is otherwise operable.

[`Element.ariaRelevant`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaRelevant) Non-standard

A string reflecting the [`aria-relevant`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-relevant) attribute, which indicates what notifications the user agent will trigger when the accessibility tree within a live region is modified. This is used to describe what changes in an `aria-live` region are relevant and should be announced.

[`Element.ariaRequired`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaRequired)

A string reflecting the [`aria-required`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-required) attribute, which indicates that user input is required on the element before a form may be submitted.

[`Element.ariaRoleDescription`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaRoleDescription)

A string reflecting the [`aria-roledescription`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-roledescription) attribute, which defines a human-readable, author-localized description for the role of an element.

[`Element.ariaRowCount`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaRowCount)

A string reflecting the [`aria-rowcount`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-rowcount) attribute, which defines the total number of rows in a table, grid, or treegrid.

[`Element.ariaRowIndex`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaRowIndex)

A string reflecting the [`aria-rowindex`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-rowindex) attribute, which defines an element's row index or position with respect to the total number of rows within a table, grid, or treegrid.

[`Element.ariaRowIndexText`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaRowIndexText)

A string reflecting the [`aria-rowindextext`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-rowindextext) attribute, which defines a human readable text alternative of aria-rowindex.

[`Element.ariaRowSpan`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaRowSpan)

A string reflecting the [`aria-rowspan`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-rowspan) attribute, which defines the number of rows spanned by a cell or gridcell within a table, grid, or treegrid.

[`Element.ariaSelected`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaSelected)

A string reflecting the [`aria-selected`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-selected) attribute, which indicates the current "selected" state of elements that have a selected state.

[`Element.ariaSetSize`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaSetSize)

A string reflecting the [`aria-setsize`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-setsize) attribute, which defines the number of items in the current set of listitems or treeitems.

[`Element.ariaSort`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaSort)

A string reflecting the [`aria-sort`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-sort) attribute, which indicates if items in a table or grid are sorted in ascending or descending order.

[`Element.ariaValueMax`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaValueMax)

A string reflecting the [`aria-valueMax`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-valuemax) attribute, which defines the maximum allowed value for a range widget.

[`Element.ariaValueMin`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaValueMin)

A string reflecting the [`aria-valueMin`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-valuemin) attribute, which defines the minimum allowed value for a range widget.

[`Element.ariaValueNow`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaValueNow)

A string reflecting the [`aria-valueNow`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-valuenow) attribute, which defines the current value for a range widget.

[`Element.ariaValueText`](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaValueText)

A string reflecting the [`aria-valuetext`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-valuetext) attribute, which defines the human-readable text alternative of aria-valuenow for a range widget.

[Instance methods](#instance_methods)
-------------------------------------

_`Element` inherits methods from its parents [`Node`](https://developer.mozilla.org/en-US/docs/Web/API/Node), and its own parent, [`EventTarget`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget)._

[`Element.after()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/after)

Inserts a set of [`Node`](https://developer.mozilla.org/en-US/docs/Web/API/Node) objects or strings in the children list of the `Element`'s parent, just after the `Element`.

[`Element.animate()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animate)

A shortcut method to create and run an animation on an element. Returns the created Animation object instance.

[`Element.append()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/append)

Inserts a set of [`Node`](https://developer.mozilla.org/en-US/docs/Web/API/Node) objects or strings after the last child of the element.

[`Element.attachShadow()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/attachShadow)

Attaches a shadow DOM tree to the specified element and returns a reference to its [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot).

[`Element.before()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/before)

Inserts a set of [`Node`](https://developer.mozilla.org/en-US/docs/Web/API/Node) objects or strings in the children list of the `Element`'s parent, just before the `Element`.

[`Element.checkVisibility()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/checkVisibility)

Returns whether an element is expected to be visible or not based on configurable checks.

[`Element.closest()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/closest)

Returns the `Element` which is the closest ancestor of the current element (or the current element itself) which matches the selectors given in parameter.

[`Element.computedStyleMap()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/computedStyleMap)

Returns a [`StylePropertyMapReadOnly`](https://developer.mozilla.org/en-US/docs/Web/API/StylePropertyMapReadOnly) interface which provides a read-only representation of a CSS declaration block that is an alternative to [`CSSStyleDeclaration`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration).

[`Element.getAnimations()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getAnimations)

Returns an array of Animation objects currently active on the element.

[`Element.getAttribute()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getAttribute)

Retrieves the value of the named attribute from the current node and returns it as a string.

[`Element.getAttributeNames()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getAttributeNames)

Returns an array of attribute names from the current element.

[`Element.getAttributeNode()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getAttributeNode)

Retrieves the node representation of the named attribute from the current node and returns it as an [`Attr`](https://developer.mozilla.org/en-US/docs/Web/API/Attr).

[`Element.getAttributeNodeNS()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getAttributeNodeNS)

Retrieves the node representation of the attribute with the specified name and namespace, from the current node and returns it as an [`Attr`](https://developer.mozilla.org/en-US/docs/Web/API/Attr).

[`Element.getAttributeNS()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getAttributeNS)

Retrieves the value of the attribute with the specified namespace and name from the current node and returns it as a string.

[`Element.getBoundingClientRect()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect)

Returns the size of an element and its position relative to the viewport.

`Element.getBoxQuads()` Experimental

Returns a list of [`DOMQuad`](https://developer.mozilla.org/en-US/docs/Web/API/DOMQuad) objects representing the CSS fragments of the node.

[`Element.getClientRects()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getClientRects)

Returns a collection of rectangles that indicate the bounding rectangles for each line of text in a client.

[`Element.getElementsByClassName()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getElementsByClassName)

Returns a live [`HTMLCollection`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection) that contains all descendants of the current element that possess the list of classes given in the parameter.

[`Element.getElementsByTagName()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getElementsByTagName)

Returns a live [`HTMLCollection`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection) containing all descendant elements, of a particular tag name, from the current element.

[`Element.getElementsByTagNameNS()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getElementsByTagNameNS)

Returns a live [`HTMLCollection`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection) containing all descendant elements, of a particular tag name and namespace, from the current element.

[`Element.getHTML()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getHTML)

Returns the DOM content of the element as an HTML string, optionally including any shadow DOM.

[`Element.hasAttribute()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/hasAttribute)

Returns a boolean value indicating if the element has the specified attribute or not.

[`Element.hasAttributeNS()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/hasAttributeNS)

Returns a boolean value indicating if the element has the specified attribute, in the specified namespace, or not.

[`Element.hasAttributes()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/hasAttributes)

Returns a boolean value indicating if the element has one or more HTML attributes present.

[`Element.hasPointerCapture()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/hasPointerCapture)

Indicates whether the element on which it is invoked has pointer capture for the pointer identified by the given pointer ID.

[`Element.insertAdjacentElement()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/insertAdjacentElement)

Inserts a given element node at a given position relative to the element it is invoked upon.

[`Element.insertAdjacentHTML()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/insertAdjacentHTML)

Parses the text as HTML or XML and inserts the resulting nodes into the tree in the position given.

[`Element.insertAdjacentText()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/insertAdjacentText)

Inserts a given text node at a given position relative to the element it is invoked upon.

[`Element.matches()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/matches)

Returns a boolean value indicating whether or not the element would be selected by the specified selector string.

[`Element.prepend()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/prepend)

Inserts a set of [`Node`](https://developer.mozilla.org/en-US/docs/Web/API/Node) objects or strings before the first child of the element.

[`Element.querySelector()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelector)

Returns the first [`Node`](https://developer.mozilla.org/en-US/docs/Web/API/Node) which matches the specified selector string relative to the element.

[`Element.querySelectorAll()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelectorAll)

Returns a [`NodeList`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList) of nodes which match the specified selector string relative to the element.

[`Element.releasePointerCapture()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/releasePointerCapture)

Releases (stops) pointer capture that was previously set for a specific [`PointerEvent`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent).

[`Element.remove()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/remove)

Removes the element from the children list of its parent.

[`Element.removeAttribute()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/removeAttribute)

Removes the named attribute from the current node.

[`Element.removeAttributeNode()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/removeAttributeNode)

Removes the node representation of the named attribute from the current node.

[`Element.removeAttributeNS()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/removeAttributeNS)

Removes the attribute with the specified name and namespace, from the current node.

[`Element.replaceChildren()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/replaceChildren)

Replaces the existing children of a [`Node`](https://developer.mozilla.org/en-US/docs/Web/API/Node) with a specified new set of children.

[`Element.replaceWith()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/replaceWith)

Replaces the element in the children list of its parent with a set of [`Node`](https://developer.mozilla.org/en-US/docs/Web/API/Node) objects or strings.

[`Element.requestFullscreen()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/requestFullscreen)

Asynchronously asks the browser to make the element fullscreen.

[`Element.requestPointerLock()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/requestPointerLock)

Allows to asynchronously ask for the pointer to be locked on the given element.

[`Element.scroll()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scroll)

Scrolls to a particular set of coordinates inside a given element.

[`Element.scrollBy()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollBy)

Scrolls an element by the given amount.

[`Element.scrollIntoView()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView)

Scrolls the page until the element gets into the view.

[`Element.scrollIntoViewIfNeeded()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoViewIfNeeded) Non-standard

Scrolls the current element into the visible area of the browser window if it's not already within the visible area of the browser window. **Use the standard [`Element.scrollIntoView()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView) instead.**

[`Element.scrollTo()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTo)

Scrolls to a particular set of coordinates inside a given element.

[`Element.setAttribute()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/setAttribute)

Sets the value of a named attribute of the current node.

[`Element.setAttributeNode()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/setAttributeNode)

Sets the node representation of the named attribute from the current node.

[`Element.setAttributeNodeNS()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/setAttributeNodeNS)

Sets the node representation of the attribute with the specified name and namespace, from the current node.

[`Element.setAttributeNS()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/setAttributeNS)

Sets the value of the attribute with the specified name and namespace, from the current node.

[`Element.setCapture()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/setCapture) Non-standard Deprecated

Sets up mouse event capture, redirecting all mouse events to this element.

[`Element.setHTMLUnsafe()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/setHTMLUnsafe)

Parses a string of HTML into a document fragment, without sanitization, which then replaces the element's original subtree in the DOM. The HTML string may include declarative shadow roots, which would be parsed as template elements if the HTML was set using [`Element.innerHTML`](#element.innerhtml).

[`Element.setPointerCapture()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/setPointerCapture)

Designates a specific element as the capture target of future [pointer events](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events).

[`Element.toggleAttribute()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/toggleAttribute)

Toggles a boolean attribute, removing it if it is present and adding it if it is not present, on the specified element.

[Events](#events)
-----------------

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface.

[`afterscriptexecute`](https://developer.mozilla.org/en-US/docs/Web/API/Element/afterscriptexecute_event "afterscriptexecute") Non-standard Deprecated

Fired when a script has been executed.

[`beforeinput`](https://developer.mozilla.org/en-US/docs/Web/API/Element/beforeinput_event "beforeinput")

Fired when the value of an input element is about to be modified.

[`beforematch`](https://developer.mozilla.org/en-US/docs/Web/API/Element/beforematch_event "beforematch") Experimental

Fires on an element that is in the [_hidden until found_](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/hidden) state, when the browser is about to reveal its content because the user has found the content through the "find in page" feature or through fragment navigation.

[`beforescriptexecute`](https://developer.mozilla.org/en-US/docs/Web/API/Element/beforescriptexecute_event "beforescriptexecute") Non-standard Deprecated

Fired when a script is about to be executed.

[`beforexrselect`](https://developer.mozilla.org/en-US/docs/Web/API/Element/beforexrselect_event "beforexrselect") Experimental

Fired before WebXR select events ([`select`](https://developer.mozilla.org/en-US/docs/Web/API/XRSession/select_event "select"), [`selectstart`](https://developer.mozilla.org/en-US/docs/Web/API/XRSession/selectstart_event "selectstart"), [`selectend`](https://developer.mozilla.org/en-US/docs/Web/API/XRSession/selectend_event "selectend")) are dispatched.

[`contentvisibilityautostatechange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/contentvisibilityautostatechange_event "contentvisibilityautostatechange")

Fires on any element with [`content-visibility: auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/content-visibility) set on it when it starts or stops being [relevant to the user](about:/en-US/docs/Web/CSS/CSS_containment/Using_CSS_containment#relevant_to_the_user) and [skipping its contents](about:/en-US/docs/Web/CSS/CSS_containment/Using_CSS_containment#skips_its_contents).

[`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input")

Fires when an element's value is changed as a direct result of a user action.

[`securitypolicyviolation`](https://developer.mozilla.org/en-US/docs/Web/API/Element/securitypolicyviolation_event "securitypolicyviolation")

Fired when a [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) is violated.

[`wheel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/wheel_event "wheel")

Fired when the user rotates a wheel button on a pointing device (typically a mouse).

### [Animation events](#animation_events)

[`animationcancel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationcancel_event "animationcancel")

Fired when an animation unexpectedly aborts.

[`animationend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationend_event "animationend")

Fired when an animation has completed normally.

[`animationiteration`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationiteration_event "animationiteration")

Fired when an animation iteration has completed.

[`animationstart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationstart_event "animationstart")

Fired when an animation starts.

### [Clipboard events](#clipboard_events)

[`copy`](https://developer.mozilla.org/en-US/docs/Web/API/Element/copy_event "copy")

Fired when the user initiates a copy action through the browser's user interface.

[`cut`](https://developer.mozilla.org/en-US/docs/Web/API/Element/cut_event "cut")

Fired when the user initiates a cut action through the browser's user interface.

[`paste`](https://developer.mozilla.org/en-US/docs/Web/API/Element/paste_event "paste")

Fired when the user initiates a paste action through the browser's user interface.

### [Composition events](#composition_events)

[`compositionend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/compositionend_event "compositionend")

Fired when a text composition system such as an [input method editor](https://developer.mozilla.org/en-US/docs/Glossary/Input_method_editor) completes or cancels the current composition session.

[`compositionstart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/compositionstart_event "compositionstart")

Fired when a text composition system such as an [input method editor](https://developer.mozilla.org/en-US/docs/Glossary/Input_method_editor) starts a new composition session.

[`compositionupdate`](https://developer.mozilla.org/en-US/docs/Web/API/Element/compositionupdate_event "compositionupdate")

Fired when a new character is received in the context of a text composition session controlled by a text composition system such as an [input method editor](https://developer.mozilla.org/en-US/docs/Glossary/Input_method_editor).

### [Focus events](#focus_events)

[`blur`](https://developer.mozilla.org/en-US/docs/Web/API/Element/blur_event "blur")

Fired when an element has lost focus.

[`focus`](https://developer.mozilla.org/en-US/docs/Web/API/Element/focus_event "focus")

Fired when an element has gained focus.

[`focusin`](https://developer.mozilla.org/en-US/docs/Web/API/Element/focusin_event "focusin")

Fired when an element has gained focus, after [`focus`](https://developer.mozilla.org/en-US/docs/Web/API/Element/focus_event "focus").

[`focusout`](https://developer.mozilla.org/en-US/docs/Web/API/Element/focusout_event "focusout")

Fired when an element has lost focus, after [`blur`](https://developer.mozilla.org/en-US/docs/Web/API/Element/blur_event "blur").

### [Fullscreen events](#fullscreen_events)

[`fullscreenchange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/fullscreenchange_event "fullscreenchange")

Sent to an `Element` when it transitions into or out of [fullscreen](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API/Guide) mode.

[`fullscreenerror`](https://developer.mozilla.org/en-US/docs/Web/API/Element/fullscreenerror_event "fullscreenerror")

Sent to an `Element` if an error occurs while attempting to switch it into or out of [fullscreen](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API/Guide) mode.

### [Keyboard events](#keyboard_events)

[`keydown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/keydown_event "keydown")

Fired when a key is pressed.

[`keypress`](https://developer.mozilla.org/en-US/docs/Web/API/Element/keypress_event "keypress") Deprecated

Fired when a key that produces a character value is pressed down.

[`keyup`](https://developer.mozilla.org/en-US/docs/Web/API/Element/keyup_event "keyup")

Fired when a key is released.

### [Mouse events](#mouse_events)

[`auxclick`](https://developer.mozilla.org/en-US/docs/Web/API/Element/auxclick_event "auxclick")

Fired when a non-primary pointing device button (e.g., any mouse button other than the left button) has been pressed and released on an element.

[`click`](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event "click")

Fired when a pointing device button (e.g., a mouse's primary button) is pressed and released on a single element.

Fired when the user attempts to open a context menu.

[`dblclick`](https://developer.mozilla.org/en-US/docs/Web/API/Element/dblclick_event "dblclick")

Fired when a pointing device button (e.g., a mouse's primary button) is clicked twice on a single element.

[`DOMActivate`](https://developer.mozilla.org/en-US/docs/Web/API/Element/DOMActivate_event "DOMActivate") Deprecated

Occurs when an element is activated, for instance, through a mouse click or a keypress.

[`DOMMouseScroll`](https://developer.mozilla.org/en-US/docs/Web/API/Element/DOMMouseScroll_event "DOMMouseScroll") Deprecated Non-standard

Occurs when mouse wheel or similar device is operated and the accumulated scroll amount is over 1 line or 1 page since last event.

[`mousedown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mousedown_event "mousedown")

Fired when a pointing device button is pressed on an element.

[`mouseenter`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseenter_event "mouseenter")

Fired when a pointing device (usually a mouse) is moved over the element that has the listener attached.

[`mouseleave`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseleave_event "mouseleave")

Fired when the pointer of a pointing device (usually a mouse) is moved out of an element that has the listener attached to it.

[`mousemove`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mousemove_event "mousemove")

Fired when a pointing device (usually a mouse) is moved while over an element.

[`mouseout`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseout_event "mouseout")

Fired when a pointing device (usually a mouse) is moved off the element to which the listener is attached or off one of its children.

[`mouseover`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseover_event "mouseover")

Fired when a pointing device is moved onto the element to which the listener is attached or onto one of its children.

[`mouseup`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseup_event "mouseup")

Fired when a pointing device button is released on an element.

[`mousewheel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mousewheel_event "mousewheel") Deprecated Non-standard

Fired when a mouse wheel or similar device is operated.

[`MozMousePixelScroll`](https://developer.mozilla.org/en-US/docs/Web/API/Element/MozMousePixelScroll_event "MozMousePixelScroll") Deprecated Non-standard

Fired when a mouse wheel or similar device is operated.

[`webkitmouseforcechanged`](https://developer.mozilla.org/en-US/docs/Web/API/Element/webkitmouseforcechanged_event "webkitmouseforcechanged") Non-standard

Fired each time the amount of pressure changes on the trackpad touch screen.

[`webkitmouseforcedown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/webkitmouseforcedown_event "webkitmouseforcedown") Non-standard

Fired after the mousedown event as soon as sufficient pressure has been applied to qualify as a "force click".

[`webkitmouseforcewillbegin`](https://developer.mozilla.org/en-US/docs/Web/API/Element/webkitmouseforcewillbegin_event "webkitmouseforcewillbegin") Non-standard

Fired before the [`mousedown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mousedown_event "mousedown") event.

[`webkitmouseforceup`](https://developer.mozilla.org/en-US/docs/Web/API/Element/webkitmouseforceup_event "webkitmouseforceup") Non-standard

Fired after the [`webkitmouseforcedown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/webkitmouseforcedown_event "webkitmouseforcedown") event as soon as the pressure has been reduced sufficiently to end the "force click".

### [Pointer events](#pointer_events)

[`gotpointercapture`](https://developer.mozilla.org/en-US/docs/Web/API/Element/gotpointercapture_event "gotpointercapture")

Fired when an element captures a pointer using [`setPointerCapture()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/setPointerCapture "setPointerCapture()").

[`lostpointercapture`](https://developer.mozilla.org/en-US/docs/Web/API/Element/lostpointercapture_event "lostpointercapture")

Fired when a [captured pointer](about:/en-US/docs/Web/API/Pointer_events#pointer_capture) is released.

[`pointercancel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointercancel_event "pointercancel")

Fired when a pointer event is canceled.

[`pointerdown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerdown_event "pointerdown")

Fired when a pointer becomes active.

[`pointerenter`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerenter_event "pointerenter")

Fired when a pointer is moved into the hit test boundaries of an element or one of its descendants.

[`pointerleave`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerleave_event "pointerleave")

Fired when a pointer is moved out of the hit test boundaries of an element.

[`pointermove`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointermove_event "pointermove")

Fired when a pointer changes coordinates.

[`pointerout`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerout_event "pointerout")

Fired when a pointer is moved out of the _hit test_ boundaries of an element (among other reasons).

[`pointerover`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerover_event "pointerover")

Fired when a pointer is moved into an element's hit test boundaries.

[`pointerrawupdate`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerrawupdate_event "pointerrawupdate") Experimental

Fired when a pointer changes any properties that don't fire [`pointerdown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerdown_event "pointerdown") or [`pointerup`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerup_event "pointerup") events.

[`pointerup`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerup_event "pointerup")

Fired when a pointer is no longer active.

### [Scroll events](#scroll_events)

[`scroll`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scroll_event "scroll")

Fired when the document view or an element has been scrolled.

[`scrollend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollend_event "scrollend")

Fires when the document view has completed scrolling.

[`scrollsnapchange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchange_event "scrollsnapchange") Experimental

Fired on the scroll container at the end of a scrolling operation when a new scroll snap target has been selected.

[`scrollsnapchanging`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchanging_event "scrollsnapchanging") Experimental

Fired on the scroll container when the browser determines a new scroll snap target is pending, i.e. it will be selected when the current scroll gesture ends.

### [Touch events](#touch_events)

[`gesturechange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/gesturechange_event "gesturechange") Non-standard

Fired when digits move during a touch gesture.

[`gestureend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/gestureend_event "gestureend") Non-standard

Fired when there are no longer multiple fingers contacting the touch surface, thus ending the gesture.

[`gesturestart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/gesturestart_event "gesturestart") Non-standard

Fired when multiple fingers contact the touch surface, thus starting a new gesture.

[`touchcancel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/touchcancel_event "touchcancel")

Fired when one or more touch points have been disrupted in an implementation-specific manner (for example, too many touch points are created).

[`touchend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/touchend_event "touchend")

Fired when one or more touch points are removed from the touch surface.

[`touchmove`](https://developer.mozilla.org/en-US/docs/Web/API/Element/touchmove_event "touchmove")

Fired when one or more touch points are moved along the touch surface.

[`touchstart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/touchstart_event "touchstart")

Fired when one or more touch points are placed on the touch surface.

### [Transition events](#transition_events)

[`transitioncancel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitioncancel_event "transitioncancel")

An [`Event`](https://developer.mozilla.org/en-US/docs/Web/API/Event) fired when a [CSS transition](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_transitions) has been cancelled.

[`transitionend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitionend_event "transitionend")

An [`Event`](https://developer.mozilla.org/en-US/docs/Web/API/Event) fired when a [CSS transition](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_transitions) has finished playing.

[`transitionrun`](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitionrun_event "transitionrun")

An [`Event`](https://developer.mozilla.org/en-US/docs/Web/API/Event) fired when a [CSS transition](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_transitions) is created (i.e., when it is added to a set of running transitions), though not necessarily started.

[`transitionstart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitionstart_event "transitionstart")

An [`Event`](https://developer.mozilla.org/en-US/docs/Web/API/Event) fired when a [CSS transition](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_transitions) has started transitioning.

[Specifications](#specifications)
---------------------------------


|Specification                                                      |
|-------------------------------------------------------------------|
|DOM # interface-element                                            |
|Pointer Events # extensions-to-the-element-interface               |
|Fullscreen API # api                                               |
|DOM Parsing and Serialization # extensions-to-the-element-interface|
|CSSOM View Module # extension-to-the-element-interface             |


[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser