OK_FORMAT = True

test = {   'name': 'log-likelihood-sequence',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> y_seq = [1, 0, 1, 1, 0]\n'
                                               '>>> p0, p1, p2 = (0.5, 0.7, 0.4)\n'
                                               '>>> z_i = 1\n'
                                               '>>> expected = -4.171117621015062\n'
                                               '>>> assert np.isclose(compute_log_likelihood_sequence(y_seq, z_i, p0, p1, p2), expected, atol=1e-06)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1.3}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
