# assert  
Check if a value, attribute or property equals expected values
## Actions

**0. attributes** - validate multiple attributes checking that their values are as expected
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  
- attributes - dictionary where the key is the attribute name and the value, the expected attribute value  
	- required: true  

**1. attribute_eq** - Check that an attribute value and expected value match
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

**2. attribute_neq** - Check that an attribute value and expected value do NOT match
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

**3. child_count_eq** - check that the number of child elements match the expected count
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

**4. child_count_neq** - check that the number of child elements are NOT equal to specified count
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

**5. style_property_eq** - check that a element's style property has a expected value
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

**6. style_property_neq** - check that a element's style property is different to the defined value
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

**7. element_property_eq** - check that a element's property has a expected value
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

**8. element_property_neq** - check that a element's property is different to the defined value
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

**9. tag_name_eq** - check that a element tag name is what was expected
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  
- value -   
	- required: false  

**10. tag_name_neq** - check that a elements tag name is different to what is defined
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
- timeout -   
	- required: false  
	- default: 30  
- value -   
	- required: false  

**11. text_content_eq** - check that the text content of a element matches the defined value
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

**12. text_content_neq** - check that the text content of a element is NOT the defined value
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

**13. value_eq** - check that the value property of a input matches the defined value
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

**14. value_neq** - check that the value property of the input does NOT match the defined value
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

**15. element_exists** - assert that an element is in the dom
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  

**16. element_not_exists** - assert that an element is NOT in the dom
- id - id of element to check  
	- required: false  
	- require alternative: query  
- query - css selector for element to check  
	- required: false  
	- require alternative: id  
