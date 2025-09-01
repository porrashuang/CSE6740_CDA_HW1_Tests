OK_FORMAT = True

test = {   'name': 'm-step',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> Y = [1, 0, 1, 1, 0]\n'
                                               '>>> p0, p1, p2 = (0.4, 0.6, 0.3)\n'
                                               '>>> posteriors = [compute_posterior(y, p0, p1, p2) for y in Y]\n'
                                               '>>> expected = [0.45320197044334976, 0.7565217391304347, 0.4702702702702703]\n'
                                               '>>> assert all((np.isclose(u, v, atol=1e-06) for u, v in zip(update_parameters(Y, p0, p1, p2), expected)))\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1.0},
                                   {   'code': '>>> Y = generate_test(0.99999, 0.99999, 0.0001, n=200)\n'
                                               '>>> p_est0, p_est1, p_est2 = estimate_parameters(Y)\n'
                                               '>>> assert p_est0 * p_est1 + (1 - p_est0) * p_est2 > 0.9\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
