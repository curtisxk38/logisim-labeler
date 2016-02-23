# logisim-labeler
Creates a Logisim file with labeled components


Generate a .circ file with a specified number of output pins/input pins/tunnels that are labeled following a specified pattern. Then you can open the file in logisim and copy the components into your actual circuit, saving you the hassle of manually creating and labeling each component.

Usage: 
`python3 logisim_label.py component number pattern [letter]`
Component: "in"/"out"/"tunnel" depending on what component you want generated
Number: An integer, how many of the specified component you want generated
Pattern: "single"/"upper"/"lower". How you want the components named. If single is used, letter must also be specified. 

 - Single will create components named letter0, letter1, letter2... 
 - Upper will create components named A, B, C, D... (Do not specify a number greater than 26)
 - Lower will create components named a, b, c, d... (Do not specify a number greater than 26)

Example usage:
`python3 logisim_label.py in 10 single s`
