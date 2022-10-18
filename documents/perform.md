# perform  
Perform a action
## Actions

**0. navigate** - using the browser url, navigate to a page
- url - the url to navigate too  
	- required: true  

**1. close_window** - for a given index, close that window or tab
- index - the index of the tab to close  
	- required: true  

**2. refresh** - ask the browser to refresh the page

**3. click** - click on a defined element
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  
- ctrl - hold ctrl down during the click operation  
	- required: false  
	- type: boolean  
	- default: false  
- alt - hold the alt key down during the click operation  
	- required: false  
	- type: boolean  
	- default: false  

**4. dbl_click** - dbl click on a defined element
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  

**5. context_click** - right click on a defined element
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  

**6. click_sequence** - perform a sequence of click events over multiple elements
- sequence - array of queries defining items to click on  
	- required: true  

**7. press_key** - perform a key press on a defined element
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  
- key - key value to press  
	- required: true  

**8. print_screen** - capture the screen as png and save to the rest results folder
- file - file path to save screenshot too  
	- required: true  

**9. select_option** - select an option from a select element
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  
- value - expected value  
	- required: true  

**10. switch_to_frame** - set the focus on a defined frame element so that it becomes the queryable context
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  

**11. switch_to_default** - switch back to the default window, normally used to exit a frame

**12. switch_to_tab** - for the given index, switch to that tab
- index - index number of the tab to switch too  
	- required: true  

**13. type_text** - type text into a defined input element
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  
- value - expected value  
	- required: true  

**14. drag_by** - drag and element by x and y number of pixels.
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- x - how many pixels to move on x
  - required: false
- y - how many pixels to move on y
  - required: false

**15. hover_over_element** - move the cursor over an element
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  

**16. mouse drag** - perform a click an drag operation on a element from a start location to a target location - like a box select
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- start_at - dictionary with a x and y property to start the drag
  - required: true
- move_too - dictionary with a x and y property on where to drag too
  - required: true