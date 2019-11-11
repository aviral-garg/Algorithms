# Algorithms

Software Engineering Knowledge Bank + coding interview preparation.

## Table of Contents

- [Software Engineer Knowledge bank](#software-engineer-knowledge-bank)
  - [Table of Contents](#table-of-contents)
  - [Plan (update as we go)](#plan-update-as-we-go)
  - [Processes](#processes)
    - [study](#study)
    - [practice](#practice)

## Scripts

```JavaScript
// CJS 2 scripts for leetCode
function KeyPress(e) {
      var evtobj = window.event? event : e

      // ctrl + ` => run code
      if (evtobj.keyCode == 192 && evtobj.ctrlKey) {
        document.querySelector("#app > div > div.main__2_tD > div.content__3fR6 > div > div.editor-wrapper__1ru6 > div > div.container__2WTi > div.action__38Xc > button.runcode__1EDI.css-y98m8o-sm").click();
      }

      // ctrl + . => hid console
      if (evtobj.keyCode == 110 && evtobj.ctrlKey) {
        document.querySelector("#app > div > div.main__2_tD > div.content__3fR6 > div > div.editor-wrapper__1ru6 > div > div.result__1UhQ > div:nth-child(2) > div > div.icon-wrapper__2q8n.close-icon__3nBt").click();
        // console.log(document.querySelector("#app > div > div.main__2_tD > div.content__3fR6 > div > div.editor-wrapper__1ru6 > div > div.container__2WTi > div.action__38Xc > button.runcode__1EDI.css-y98m8o-sm") !== undefined);
      }
}

document.onkeydown = KeyPress;
```

<!-- ## Plan (update as we go)

1. Sorting
   1. study
      1. quickSort
         1. ![quickSort](/resources/images/quickSort.png "quickSort")
      2. mergeSort
         1. ![mSort](/resources/images/mSort.png "mergeSort")
      3. heapSort
         1. ![heapSort](/resources/images/heapSort.png "heapSort")
   2. practice
      1. q1: nutsAndBolts
         1. ![nutsAndBolts](resources/images/nutsAndBolts.png "nutsAndBolts")
      2. q2: mergeKSortedArrays
         1. ![mergeKSortedArrays](resources/images/mergeKSortedArrays.png "mergeKSortedArrays")
      3. q3: topK
         1. ![topK](resources/images/topK.png "topK")
      4. q4: 3sum
         1.
2. Recursion
3. Trees
4. ...
5. ...
6. ... -->

<!-- ## Processes

### study

| time | task             |
| ---: | ---------------- |
|   10 | get + understand |
|   10 | discuss-1        |
|   10 | discuss-2        | --> |

<!-- ### practice

| time | task    |
| ---: | ------- |
|   15 | try     |
|  ... | discuss |
|  ... | ...     | --> |
