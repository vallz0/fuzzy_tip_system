import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


class FuzzyTipSystem:
    def __init__(self) -> None:
        self.quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
        self.service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
        self.tip = ctrl.Consequent(np.arange(0, 21, 1), 'tip')

        self._setup_membership_functions()
        self.rules = self._create_rules()
        self.control_system = ctrl.ControlSystem(self.rules)
        self.simulation = ctrl.ControlSystemSimulation(self.control_system)

    def _setup_membership_functions(self) -> None:
        self.quality.automf(number=3, names=['poor', 'good', 'excellent'])
        self.service.automf(number=3, names=['poor', 'acceptable', 'great'])

        self.tip['low'] = fuzz.trimf(self.tip.universe, [0, 0, 10])
        self.tip['medium'] = fuzz.trimf(self.tip.universe, [0, 10, 20])
        self.tip['high'] = fuzz.trimf(self.tip.universe, [10, 20, 20])

    def _create_rules(self) -> list[ctrl.Rule]:
        rule1 = ctrl.Rule(self.quality['poor'] | self.service['poor'], self.tip['low'])
        rule2 = ctrl.Rule(self.service['acceptable'], self.tip['medium'])
        rule3 = ctrl.Rule(self.service['great'] | self.quality['excellent'], self.tip['high'])
        return [rule1, rule2, rule3]

    def compute_tip(self, quality: float, service: float) -> float:
        self.simulation.input['quality'] = quality
        self.simulation.input['service'] = service
        self.simulation.compute()
        return self.simulation.output['tip']

    def save_tip_graph(self) -> None:
        self.tip.view(sim=self.simulation)
        plt.savefig("Images/tip_view.png")
        plt.savefig("Images/tip_view.pdf")
