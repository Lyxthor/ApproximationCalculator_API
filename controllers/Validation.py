from pydantic import BaseModel

class BisectionVars(BaseModel) :
    expression : str
    a : float
    b : float
    stop_condition : str
    stop_value : float
    decimal_places : int