from flask import render_template, request
import cgi
import re
from logic_circuit import app
from .gates import AND, OR, NOT


#from gate_implementation import logic_circuit_output


@app.route("/", methods = ["GET"])
def homepage():
    return render_template("homepage.html")

@app.route("/", methods = ["POST"])    
def homepage_postsubmit():
	
	symbol_for_and = "*"
	symbol_for_or = "+"
	symbol_for_not = "'"
	
	equation = request.form["equation"] # "A * B + B * C"
	equation = re.sub(r'\s+', "", equation)
	logic_of_variables = request.form["logic_of_variables"] # "1,0,0,0"
	components = list(equation) # ["A", "'", "*","B","+","B","*","C"]	
	# equation_no_not = equation.replace("'", "")
	# equation_no_not_and = equation_no_not.replace("*","")
	# equation_no__not_and_or = equation_no_not_and.replace("+","")
	# equation_no_repeat_characters = ''.join([j for i,j in enumerate(equation_no__not_and_or) if j not in equation_no__not_and_or[:i]])
	# components_no_delimitors_or_repeat = list(equation_no_repeat_characters) #["A","B","C"]
	# components_no_delimitors_or_repeat_formatted = ",".join(components_no_delimitors_or_repeat)
	# components_no_delimitors_or_repeat_formatted = components_no_delimitors_or_repeat_formatted.replace("'", "")
	logic_split = logic_of_variables.split(",") # ['1','0','0','0']
	n = 0
	#import pdb; pdb.set_trace()
	for logic_value in logic_split:
		try: 
			components[n] = logic_value
			if components[n+1] == symbol_for_not:
				n = n+3
			else:
				n = n+2
		except IndexError:
			pass
		
		

	while symbol_for_not in components:
		try:
		    n = next(x for x in components if x==symbol_for_not)
		    index_of_n = components.index(n)
		    not_gate = NOT(pinA=components[(index_of_n)-1])
		    components.insert(index_of_n, not_gate.output())
		    components.remove(components[(index_of_n)+1])
		    components.remove(components[(index_of_n)-1])
		except IndexError:
			pass
	while symbol_for_and in components:
		try:
		    n = next(x for x in components if x==symbol_for_and)
		    index_of_n = components.index(n)
		    and_gate = AND(pinA=components[(index_of_n)-1], pinB=components[(index_of_n)+1])
		    components.insert(index_of_n, and_gate.output())
		    components.remove(components[(index_of_n)+1])
		    
		    components.remove(components[(index_of_n)+2])
		    components.remove(components[(index_of_n)-1])
		except IndexError:
			pass

	while symbol_for_or in components:
		try:
		    n = next(x for x in components if x==symbol_for_or)
		    index_of_n = components.index(n)
		    or_gate = OR(pinA=components[(index_of_n)-1], pinB=components[(index_of_n)+1])
		    components.insert(index_of_n, or_gate.output())
		    components.remove(components[(index_of_n)+1])
		    components.remove(components[(index_of_n)+2])
		    components.remove(components[(index_of_n)-1])
		except IndexError:
			pass 
	logic_circuit_output = components[0]
	#return render_template("homepage_postsubmit1.html", equation = equation, components_no_delims = components_no_delimitors_or_repeat)
	return render_template("homepage_postsubmit.html", equation = equation, logic_of_variables = logic_of_variables, output = logic_circuit_output)

