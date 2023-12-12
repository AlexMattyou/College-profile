from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import pandas as pd

model = BayesianNetwork([('Rain', 'Traffic_Jam'), ('Accident', 'Traffic_Jam')])

cpd_rain = TabularCPD(variable='Rain', variable_card=2, values=[[0.3], [0.7]])
cpd_accident = TabularCPD(variable='Accident', variable_card=2, values=[[0.2], [0.8]])
cpd_traffic_jam = TabularCPD(variable='Traffic_Jam', variable_card=2, values=[[0.9, 0.3, 0.7, 0.1],[0.1, 0.7, 0.3, 0.9]], evidence=['Rain', 'Accident'], evidence_card=[2, 2])

model.add_cpds(cpd_rain, cpd_accident, cpd_traffic_jam)
print(model.check_model())
inference = VariableElimination(model)

result1 = inference.query(variables=['Traffic_Jam'], evidence={'Rain': 1})
print(result1)

result2 = inference.query(variables=['Traffic_Jam'], evidence={'Accident': 1})
print(result2)


