This is the notes for the CSS Segment

Look at Mozilla Web Doc for more ideas on CSS and CSS Selectors https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors

Notes

Vocabulary for some CSS Terms

DOM(Document Object Model) - is a tree structure with nodes for each HTML elements, a piece of text image and any other object in the web page.
Selectors - are one part of the CSS ruleset. They Show which HTML element(s) the rule is for.
Declaration blocks - are the other part of the CSS ruleset, they say how the rule will modify the elements indicated by selectors/
CSS rules are composed of a Selector followed by a declaration block.
Type - is the simplest kind of seletor. It shows the name of one type of HTML element like em or li.
class - in HTML is an attribute that groups elements together that you want to have the same style.
id - is an attribute that must be unique to a single, used to find it 

Selectors Review
Type - selectors  are used to apply styles to a particular type of HTML element, like h1 or body. Type selectors are written using just type names.
Class - selectors are used to set the style for multiple HTML elements that have a particular value for the class attribute. You can name a class anything you want! Class selectors are written with a dot before the class: for elements such as <p class="blue">, the class selector is .blue.
ID - selectors are used when the style is being applied to one HTML element, which has to have an id attribute. There can be only one element with a particular id on a page. You can also choose any name you want for an id, just like a class. ID selectors are written using a # sign: for an element such as <div id="sidebar">, the id selector is #sidebar.

Linking stylesheets
Link a stylesheet to your HTML file.
this is the syntax
<link rel="stylesheet" href="style.css">
