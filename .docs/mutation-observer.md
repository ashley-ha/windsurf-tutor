# MutationObserver - Web APIs | MDN
Baseline

Widely available

The **`MutationObserver`** interface provides the ability to watch for changes being made to the [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) tree. It is designed as a replacement for the older [Mutation Events](https://developer.mozilla.org/en-US/docs/Web/API/MutationEvent) feature, which was part of the DOM3 Events specification.

[Constructor](#constructor)
---------------------------

[`MutationObserver()`](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver/MutationObserver "MutationObserver()")

Creates and returns a new `MutationObserver` which will invoke a specified callback function when DOM changes occur.

[Instance methods](#instance_methods)
-------------------------------------

[`disconnect()`](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver/disconnect "disconnect()")

Stops the `MutationObserver` instance from receiving further notifications until and unless [`observe()`](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver/observe "observe()") is called again.

[`observe()`](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver/observe "observe()")

Configures the `MutationObserver` to begin receiving notifications through its callback function when DOM changes matching the given options occur.

[`takeRecords()`](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver/takeRecords "takeRecords()")

Removes all pending notifications from the `MutationObserver`'s notification queue and returns them in a new [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of [`MutationRecord`](https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord) objects.

[Mutation Observer & customize resize event listener & demo](#mutation_observer_customize_resize_event_listener_demo)
---------------------------------------------------------------------------------------------------------------------

[Example](#example)
-------------------

The following example was adapted from [this blog post](https://hacks.mozilla.org/2012/05/dom-mutationobserver-reacting-to-dom-changes-without-killing-browser-performance/).

```
// Select the node that will be observed for mutations
const targetNode = document.getElementById("some-id");

// Options for the observer (which mutations to observe)
const config = { attributes: true, childList: true, subtree: true };

// Callback function to execute when mutations are observed
const callback = (mutationList, observer) => {
  for (const mutation of mutationList) {
    if (mutation.type === "childList") {
      console.log("A child node has been added or removed.");
    } else if (mutation.type === "attributes") {
      console.log(`The ${mutation.attributeName} attribute was modified.`);
    }
  }
};

// Create an observer instance linked to the callback function
const observer = new MutationObserver(callback);

// Start observing the target node for configured mutations
observer.observe(targetNode, config);

// Later, you can stop observing
observer.disconnect();

```


[Specifications](#specifications)
---------------------------------


|Specification                   |
|--------------------------------|
|DOM # interface-mutationobserver|


[Browser compatibility](#browser_compatibility)
-----------------------------------------------

BCD tables only load in the browser

[See also](#see_also)
---------------------