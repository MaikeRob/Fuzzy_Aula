import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#variaveis
iluminacao = ctrl.Antecedent(np.arange(0, 101, 1), "iluminacao")
temperatura = ctrl.Antecedent(np.arange(0, 36, 1), "temperatura")
ergonomia = ctrl.Antecedent(np.arange(0, 101, 1), "ergonomia")
qualidade_equipamento = ctrl.Antecedent(np.arange(0, 101, 1), "qualidade_equipamento")

iluminacao["claro"]
iluminacao["claro"]
