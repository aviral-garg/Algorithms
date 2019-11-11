// CJS 2 scripts for leetCode
/**
 * How To:
 *  1. Install CJS 2 chrome extension
 *  2. Either paste this entire code in the area or use the following cdn link to import 'your own external script':
 *
 */

/**
 * Helper Function to display keyCodes
 */
document.addEventListener("keydown", function(e) {
    console.log(e.keyCode);
    if (e.code === "Numpad0") {
    }
});

/**
 * keyCode -> keyName Map
 */
const keyCodeMap = {
    8: "backspace",
    9: "tab",
    13: "enter",
    16: "shift",
    17: "ctrl",
    18: "alt",
    19: "pausebreak",
    20: "capslock",
    27: "esc",
    32: "space",
    33: "pageup",
    34: "pagedown",
    35: "end",
    36: "home",
    37: "leftarrow",
    38: "uparrow",
    39: "rightarrow",
    40: "downarrow",
    45: "insert",
    46: "delete",
    48: "0",
    49: "1",
    50: "2",
    51: "3",
    52: "4",
    53: "5",
    54: "6",
    55: "7",
    56: "8",
    57: "9",
    65: "a",
    66: "b",
    67: "c",
    68: "d",
    69: "e",
    70: "f",
    71: "g",
    72: "h",
    73: "i",
    74: "j",
    75: "k",
    76: "l",
    77: "m",
    78: "n",
    79: "o",
    80: "p",
    81: "q",
    82: "r",
    83: "s",
    84: "t",
    85: "u",
    86: "v",
    87: "w",
    88: "x",
    89: "y",
    90: "z",
    91: "leftwindowkey",
    92: "rightwindowkey",
    93: "selectkey",
    96: "numpad0",
    97: "numpad1",
    98: "numpad2",
    99: "numpad3",
    100: "numpad4",
    101: "numpad5",
    102: "numpad6",
    103: "numpad7",
    104: "numpad8",
    105: "numpad9",
    106: "multiply",
    107: "add",
    109: "subtract",
    110: "decimalpoint",
    111: "divide",
    112: "f1",
    113: "f2",
    114: "f3",
    115: "f4",
    116: "f5",
    117: "f6",
    118: "f7",
    119: "f8",
    120: "f9",
    121: "f10",
    122: "f11",
    123: "f12",
    144: "numlock",
    145: "scrolllock",
    186: "semicolon",
    187: "equalsign",
    188: "comma",
    189: "dash",
    190: "period",
    191: "forwardslash",
    192: "graveaccent",
    219: "openbracket",
    220: "backslash",
    221: "closebracket",
    222: "singlequote"
};

// CUSTOM SELECTORS for desired DOM Elements

const RUN =
    "#app > div > div.main__2_tD > div.content__3fR6 > div > div.editor-wrapper__1ru6 > div > div.container__2WTi > div.action__38Xc > button.runcode__1EDI.css-y98m8o-sm";
const HIDE_CONSOLE =
    "#app > div > div.main__2_tD > div.content__3fR6 > div > div.editor-wrapper__1ru6 > div > div.result__1UhQ > div:nth-child(2) > div > div.icon-wrapper__2q8n.close-icon__3nBt";
const TEST_CASES =
    "#app > div > div.main__2_tD > div.content__3fR6 > div > div.editor-wrapper__1ru6 > div > div.result__1UhQ > div:nth-child(2) > div > div.header-content__2Ekc > div > div.css-jccvoy-TabViewHeader.e5i1odf1 > div > div.css-1kuaqiy-TabHeader.e5i1odf4 > div";
const SHOW_CONSOLE =
    "#app > div > div.main__2_tD > div.content__3fR6 > div > div.editor-wrapper__1ru6 > div > div.container__2WTi > div.func__1DsC > button";
let INPUT_AREA = "#testcase-editor > textarea";
/**
 * KeyName -> JS Path (DOM element) Map
 */
const keyMap = {
    r: RUN,
    s: SHOW_CONSOLE,
    h: HIDE_CONSOLE,
    t: TEST_CASES,
    i: INPUT_AREA
};

/**
 * Simulates a mouse click on DOM element given as JS Path
 * @param jsPath JS Path of the DOM element
 */
const domClick = jsPath => document.querySelector(jsPath).click();
const domFocus = jsPath => document.querySelector(jsPath).focus();

/**
 * Custom Keyboard Shortcuts (onKeyDown Listener)
 * keyCode -> keyName -> DOM selector -> trigger click
 * @param e keyDown event
 */
document.onkeydown = e => {
    e.altKey ? domClick(keyMap[keyCodeMap[e.keyCode]]) : undefined;
    e.ctrlKey ? domFocus(keyMap[keyCodeMap[e.keyCode]]) : undefined;
};
