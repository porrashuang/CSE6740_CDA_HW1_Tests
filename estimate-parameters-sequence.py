OK_FORMAT = True

test = {   'name': 'estimate-parameters-sequence',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> p_0, p_1, p_2 = (0.3, 0.7, 0.4)\n'
                                               '>>> Y_sequences = generate_test_sequence(p_0, p_1, p_2, n=3000, k=5)\n'
                                               '>>> p_est0, p_est1, p_est2 = estimate_parameters_sequence(Y_sequences)\n'
                                               '>>> p_0_lower = p_est0 < 0.5\n'
                                               '>>> assert abs(p_est0 - p_0) < 0.1 if p_0_lower else abs(1 - p_est0 - p_0) < 0.1\n'
                                               '>>> assert abs(p_est1 - p_1) < 0.1 if p_0_lower else abs(p_est2 - p_1) < 0.1\n'
                                               '>>> assert abs(p_est2 - p_2) < 0.1 if p_0_lower else abs(p_est1 - p_2) < 0.1\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1.3},
                                   {   'code': '>>> p_0, p_1, p_2 = (0.8, 0.3, 0.65)\n'
                                               '>>> Y_sequences = generate_test_sequence(p_0, p_1, p_2, n=3000, k=5)\n'
                                               '>>> p_est0, p_est1, p_est2 = estimate_parameters_sequence(Y_sequences)\n'
                                               '>>> p_0_higher = p_est0 > 0.5\n'
                                               '>>> assert abs(p_est0 - p_0) < 0.1 if p_0_higher else abs(1 - p_est0 - p_0) < 0.1\n'
                                               '>>> assert abs(p_est1 - p_1) < 0.1 if p_0_higher else abs(p_est2 - p_1) < 0.1\n'
                                               '>>> assert abs(p_est2 - p_2) < 0.1 if p_0_higher else abs(p_est1 - p_2) < 0.1\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1.3}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
