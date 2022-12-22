'''
Copyright © Tao Xiang:
This code is written by Tao Xiang from TUM (ge25pof, 03711727) for the challenge "AI Programming Exercise 2022 - Bonus exercise" and not aimed for public use. Any use for improper purposes will be subject to legal action.
Improper purposes include but not limited to:
- copy&paste for personal submission for "AI Programming Exercise 2022 - Bonus exercise"
- copy&paste and share it online
- copy&paste and share it to others
Tao Xiang reserves the right to extend the improper purposes.
This copyright statement should only be seen by the administrators of the challenge "AI Programming Exercise 2022 - Bonus exercise" and is made for case of e.g. internet hacking or illegal disclosure.
'''

from typing import Union,List
from SMP.motion_planner.node import PriorityNode
import numpy as np
from SMP.motion_planner.plot_config import DefaultPlotConfig
from SMP.motion_planner.search_algorithms.best_first_search import GreedyBestFirstSearch




class MetricMixin:
    '''
    A Metric mixin for the current node. It will compute following metrics of the current node:
    - orientation diff
    - trajectory efficiency
    - velocity diff
    - time diff
    - position diff
    '''
    def __init__(self) -> None:
        super().__init__()

    def set_metrics_of_node(self, node_current:PriorityNode):
        '''
        compute the metrics for given node.

        :param node_current: current node
        :return: None
        '''

        last_path = node_current.list_paths[-1]
        start_state = last_path[0]
        last_state = last_path[-1]
        last_state_orientation = last_state.orientation
        last_state_velocity = last_state.velocity

        # 1 orrientation diff
        a2g = self.calc_angle_to_goal(last_path[-1])
        orientation_diff = abs(self.calc_orientation_diff(a2g, last_state_orientation))

        # 2 trajectory efficiency
        time = 0.
        for i in node_current.list_paths:
            time += self.calc_time_cost(i)
        traj_effi = time/len(node_current.list_paths)

        # 3 velocity diff
        if self.velocity_desired is None:
            vel_diff = None
        else:
            vel_diff = (self.velocity_desired.start+ self.velocity_desired.end)/2 - last_state_velocity

        # 4 time diff
        if self.time_desired is None:
            time_diff = None
        else:
            time_diff = self.time_desired.start - last_state.time_step

        # 5 position diff
        if self.position_desired is None:
            pos_diff = None
        else:
            if np.isclose(last_state_velocity, 0):
                 pos_diff = np.inf

            else:
                 pos_diff = self.calc_euclidean_distance(current_node=node_current) / last_state_velocity



        self.__metrics__ = np.array([
            orientation_diff,
            traj_effi,
            vel_diff,
            time_diff,
            pos_diff
        ])
        self.__metrics_len__ = len(self.__metrics__)


        self.__post_processing__()



    def metric_loss(self, *, weights: List[Union[int,float]])-> float:
        '''
        compute the heuristic loss given the weights. The length of the weights should be equal to number of metrics. The weights are first normalized using softmax function, then the loss is computed as the inner product of weights and metrics.

        :param weights: a List of weights
        :return: computed loss
        '''
        assert len(weights) == self.__metrics_len__
        weights = np.array(weights)
        weights = self.__softmax_by_tao_xiang__(weights)
        ret = float(np.inner(weights,self.__metrics__))
        if np.isnan(ret): return np.inf
        return ret

    def __post_processing__(self):
        # replace None/nan/inf with large number
        f = lambda x: 99999 if (x is None or np.isnan(x) or x == np.inf) else x
        self.__metrics__ = np.array(list(map(f, self.__metrics__)))

    def __softmax_by_tao_xiang__(self,vector: np.array):
        temp = np.exp(vector)
        sum = np.sum(temp)
        return temp/sum





class StudentMotionPlanner(GreedyBestFirstSearch, MetricMixin):
    """
    Motion planner implementation by students.
    Note that you may inherit from any given motion planner as you wish, or come up with your own planner.
    Here as an example, the planner is inherited from the GreedyBestFirstSearch planner.
    """

    def __init__(self, scenario, planningProblem, automata, plot_config=DefaultPlotConfig):
        GreedyBestFirstSearch.__init__(self,scenario=scenario, planningProblem=planningProblem, automaton=automata,
                         plot_config=plot_config)
        MetricMixin.__init__(self)

    def evaluation_function(self, node_current: PriorityNode) -> float:
        ########################################################################
        # todo: Implement your own evaluation function here.                   #
        ########################################################################
        return super().evaluation_function(node_current)

    def heuristic_function(self, node_current: PriorityNode) -> float:
        ########################################################################
        # todo: Implement your own heuristic cost calculation here.            #
        # Hint:                                                                #
        #   Use the State of the current node and the information from the     #
        #   planning problem, as well as from the scenario.                    #
        #   Some helper functions for your convenience can be found in         #
        #   ./search_algorithms/base_class.py                             #
        ########################################################################

        return self.new_heu_fn_temp(node_current)



    def new_heu_fn_even(self, node_current: PriorityNode):
        last_path = node_current.list_paths[-1]

        if self.reached_goal(last_path):
            return 0.0

        # set metrics
        self.set_metrics_of_node(node_current)

        return self.metric_loss(
            weights=[
                10, # orientation diff
                10, # trajectory efficiency
                10, # velocity diff
                10, # time diff
                10, # position diff
            ]
        )


    def new_heu_fn_pos(self,node_current: PriorityNode) ->float:
        last_path = node_current.list_paths[-1]

        if self.reached_goal(last_path):
            return 0.0

        # set metrics
        self.set_metrics_of_node(node_current)
        return self.metric_loss(weights=[
            10,  # orientation diff
            10,  # trajectory efficiency
            10,  # velocity diff
            10,  # time diff
            100,  # position diff
        ])

    def new_heu_fn_time(self,node_current: PriorityNode) ->float:
        last_path = node_current.list_paths[-1]

        if self.reached_goal(last_path):
            return 0.0

        # set metrics
        self.set_metrics_of_node(node_current)
        return self.metric_loss(weights=[
            10,  # orientation diff
            10,  # trajectory efficiency
            10,  # velocity diff
            100,  # time diff
            10,  # position diff
        ])

    def new_heu_fn_temp(self,node_current: PriorityNode) ->float:
        last_path = node_current.list_paths[-1]

        if self.reached_goal(last_path):
            return 0.0

        # set metrics
        self.set_metrics_of_node(node_current)
        return self.metric_loss(weights=[
            10,  # orientation diff
            10,  # trajectory efficiency
            10,  # velocity diff
            100,  # time diff
            100,  # position diff
        ])


