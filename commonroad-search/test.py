if __name__ == '__main__':
    import os
    import sys

    path_notebook = os.getcwd()

    # add the SMP folder to python path
    sys.path.append(os.path.join(path_notebook, "../../"))

    # add the 1_search_algorithms folder to python path
    sys.path.append(os.path.join(path_notebook, "../"))

    import matplotlib.pyplot as plt

    from commonroad.common.file_reader import CommonRoadFileReader
    from commonroad.visualization.mp_renderer import MPRenderer

    from SMP.motion_planner.motion_planner import MotionPlanner
    from SMP.maneuver_automaton.maneuver_automaton import ManeuverAutomaton
    from SMP.motion_planner.utility import plot_primitives, display_steps

    # load scenario
    path_scenario = os.path.join(path_notebook, "./scenarios/tutorial/")
    id_scenario = 'ZAM_Tutorial_Urban-3_2'

    # read in scenario and planning problem set
    scenario, planning_problem_set = CommonRoadFileReader(path_scenario + id_scenario + '.xml').open()
    # retrieve the first planning problem in the problem set
    planning_problem = list(planning_problem_set.planning_problem_dict.values())[0]

    # plot the scenario and the planning problem set
    plt.figure(figsize=(15, 5))
    renderer = MPRenderer()

    scenario.draw(renderer)
    planning_problem_set.draw(renderer)

    plt.gca().set_aspect('equal')
    plt.margins(0, 0)
    renderer.render()
    plt.show()

    # load the xml with stores the motion primitives
    name_file_motion_primitives = 'V_9.0_9.0_Vstep_0_SA_-0.2_0.2_SAstep_0.2_T_0.5_Model_BMW_320i.xml'

    # generate automaton
    automaton = ManeuverAutomaton.generate_automaton(name_file_motion_primitives)

    # plot motion primitives
    plot_primitives(automaton.list_primitives)

    # construct motion planner
    planner_BFS = MotionPlanner.BreadthFirstSearch(scenario=scenario,
                                                   planning_problem=planning_problem,
                                                   automaton=automaton)
    # prepare input for visualization
    scenario_data = (scenario, planner_BFS.state_initial, planner_BFS.shape_ego, planning_problem)

    # display search steps
    display_steps(scenario_data=scenario_data, algorithm=planner_BFS.execute_search,
                  config=planner_BFS.config_plot)