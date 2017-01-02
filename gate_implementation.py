from flask import request
from .gates import AND, OR, NOT
#logic_equation = A * B + B * C
#logic_of_input_variables = "1,0,0,0"
logic_equation = request.form['equation']
logic_of_input_variables = request.GET['text_box2']

components = logic_equation.split(" ")
symbol_for_and = "*"
symbol_for_or = "+"
symbol_for_not = "'"

while symbol_for_not in components:
    n = next(x for x in components if x==symbol_for_not)
    index_of_n = components.index(n)
    not_gate = NOT(pinA=components[(index_of_n)-1])
    components.insert(index_of_n, not_gate.output())
    components.remove(components[(index_of_n)-2], components[index_of_n])

while symbol_for_and in components:
    n = next(x for x in components if x==symbol_for_and)
    index_of_n = components.index(n)
    and_gate = AND(pinA=components[(index_of_n)-1], pinB=components[(index_of_n)+1])
    components.insert(index_of_n, and_gate.output())
    components.remove(components[(index_of_n)-2], components[index_of_n], components[(index_of_n)+1])
    
while symbol_for_or in components:
    n = next(x for x in components if x==symbol_for_or)
    index_of_n = components.index(n)
    or_gate = OR(pinA=components[(index_of_n)-1], pinB=components[(index_of_n)+1])
    components.insert(index_of_n, or_gate.output())
    components.remove(components[(index_of_n)-2], components[index_of_n], components[(index_of_n)+1])

logic_circuit_output = components[0]

