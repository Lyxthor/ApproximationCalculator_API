from decimal import Decimal, getcontext
from operator import attrgetter
from controllers.Validation import BisectionVars
import re


getcontext().prec=50

def dec_round(number, prec) :
    return str(round(Decimal(str(number)), prec))
def wrap_string_numbers_in_decimal(s):
    # Regular expression to find numbers (integers and decimals)
    pattern = r'\d+(?:\.\d+)?'
    
    # Replace each number with Decimal('_number')
    wrapped_string = re.sub(pattern, lambda m: f"Decimal('{m.group()}')", s)
    
    return wrapped_string
class Bisection :
    def __init__(self, vars : BisectionVars) :
        self.iteration_rows = {
            "a" : [],
            "b" : [],
            "x" : [],
            "Fa" : [],
            "Fb" : [],
            "Fx" : []
        }
        (formula, a, b, stop_condition, stop_value, decimal_places) = attrgetter('expression', 'a', 'b', 'stop_condition', 'stop_value', 'decimal_places')(vars)
        formula = formula.replace("^", "**")
        print(formula)
        self.formula = wrap_string_numbers_in_decimal(formula)
        self.stop_condition = stop_condition
        self.stop_value = Decimal(str(stop_value)) if stop_condition == "precision" else stop_value
        self.stop_index = 0
        self.a = Decimal(str(a))
        self.b = Decimal(str(b))
        self.decimal_places = decimal_places
    def func(self, x) :
        result = eval(self.formula)
        return result
    def countX(self, a, b) :
        Fa = self.func(a)
        Fb = self.func(b)
        result = (a*Fb-b*Fa) / (Fb-Fa)
        return result
    def isIterationContinue(self, fx) :
        if self.stop_condition == "iteration" :
            iteration = self.stop_index + 1
            self.stop_index = iteration
            return iteration <= self.stop_value
        elif self.stop_condition == "precision" :
            precision = fx
            self.stop_index = precision
            return precision > self.stop_value
    def startIterations(self) :
        return self.iterations(self.a, self.b)
    def iterations(self, a, b) :
        x = self.countX(a, b)
        fa = self.func(a)
        fb = self.func(b)
        fx = self.func(x)
        if self.isIterationContinue(fx) :
            self.iteration_rows["a"].append(dec_round(a, self.decimal_places))
            self.iteration_rows["b"].append(dec_round(b, self.decimal_places))
            self.iteration_rows["x"].append(dec_round(x, self.decimal_places))
            self.iteration_rows["Fa"].append(dec_round(fa, self.decimal_places))
            self.iteration_rows["Fb"].append(dec_round(fb, self.decimal_places))
            self.iteration_rows["Fx"].append(dec_round(fx, self.decimal_places))
            
            if fx * fa < 0:
                b = x
            elif fx * fb < 0:
                a = x
            return self.iterations(a, b)
        else :
            return self.iteration_rows