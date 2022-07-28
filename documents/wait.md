# wait  
Wait for a expected element, attribute, property or value. Fail if value does not appear before timeout
## Actions

**0. time** - wait for a given amount of time
- timeout -   
	- required: false  
	- default: 30  

**1. is_ready** - wait until the defined element's dataset has a ready property set to true
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  

**2. element** - wait until element exists and is visible
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  

**3. attribute** - wait for attribute to have a particular value
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  
- attr - attribute name  
	- required: true  
- value - expected value  
	- required: true  

**4. attributes** - wait for multiple attributes to have their defined values
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  
- attributes - dictionary of attributes and values to check.  
	- required: true  

**5. style_property** - wait for element's style to have the defined property value
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  
- property - the property name to check the value on  
	- required: true  
- value - expected value  
	- required: true  

**6. element_properties** - wait for element's style properties to be set to defined values
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  
- properties - dictionary of property names and values to check  
	- required: true  

**7. text_content** - wait until element's text content equals defined text
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

**8. text_value** - wait until element's value property equals defined value
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

**9. selected** - wait for checkbox or radio buttons to be selected
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  

**10. child_count** - wait until defined element has a defined number of children
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  
- count - the quantity of items to check  
	- required: true  

**11. element_count** - wait until queried elements equal defined count
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  
- count - the quantity of items to check  
	- required: true  

**12. window_count** - wait until window count equals defined
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  
- count - the quantity of items to check  
	- required: true  

**13. idle** - wait for cpu idel
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  

**14. has_attribute** - wait until a element has the defined attribute
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  

**15. has_not_attribute** - wait until the defined attribute is no longer on element
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  