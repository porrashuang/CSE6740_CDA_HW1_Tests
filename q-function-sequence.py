OK_FORMAT = True

test = {   'name': 'q-function-sequence',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> Y_sequences = [[1, 0, 1, 1, 0], [0, 0, 0, 1, 1]]\n'
                                               '>>> p0, p1, p2 = (0.5, 0.7, 0.3)\n'
                                               '>>> p0_t, p1_t, p2_t = (0.4, 0.6, 0.2)\n'
                                               '>>> expected = -8.859417052938802\n'
                                               '>>> assert np.isclose(Q_function_sequence(Y_sequences, p0, p1, p2, p0_t, p1_t, p2_t), expected, atol=1e-06)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1.3}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
