import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#variaveis
iluminacao = ctrl.Antecedent(np.arange(0, 101, 1), "iluminacao")
temperatura = ctrl.Antecedent(np.arange(0, 36, 1), "temperatura")
ergonomia = ctrl.Antecedent(np.arange(0, 101, 1), "ergonomia")
qualidade_equipamento = ctrl.Antecedent(np.arange(0, 101, 1), "qualidade_equipamento")

iluminacao["claro"] = fuzz.trimf(iluminacao.universe, [40, 100, 100])
iluminacao["escuro"] = fuzz.trimf(iluminacao.universe, [0, 0, 60])

temperatura["quente"] = fuzz.trapmf(temperatura.universe, [0, 0, 10, 20])
temperatura["ambiente"] = fuzz.trimf(temperatura.universe, [13, 22, 29])
temperatura["frio"] = fuzz.trapmf(temperatura.universe, [26, 30, 35, 35])

ergonomia["confortavel"] = fuzz.gaussmf(ergonomia.universe, 100, 20)
ergonomia["desconfortavel"] = fuzz.gaussmf(ergonomia.universe, 0, 20)

