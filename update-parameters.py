OK_FORMAT = True

test = {   'name': 'update-parameters',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> Y_sequences = [[1, 0, 1, 1, 0], [0, 1, 0, 0, 0]]\n'
                                               '>>> p0, p1, p2 = (0.5, 0.7, 0.3)\n'
                                               '>>> posteriors = [compute_posterior_sequence(seq, p0, p1, p2) for seq in Y_sequences]\n'
                                               '>>> p0_new = sum(posteriors) / len(Y_sequences)\n'
                                               '>>> numerator_p1 = 0.0\n'
                                               '>>> denominator_p1 = 0.0\n'
                                               '>>> numerator_p2 = 0.0\n'
                                               '>>> denominator_p2 = 0.0\n'
                                               '>>> for post, seq in zip(posteriors, Y_sequences):\n'
                                               '...     h = sum(seq)\n'
                                               '...     k = len(seq)\n'
                                               '...     numerator_p1 += post * h\n'
                                               '...     denominator_p1 += post * k\n'
                                               '...     numerator_p2 += (1 - post) * h\n'
                                               '...     denominator_p2 += (1 - post) * k\n'
                                               '>>> p1_new = numerator_p1 / (denominator_p1 + 1e-12)\n'
                                               '>>> p2_new = numerator_p2 / (denominator_p2 + 1e-12)\n'
                                               '>>> expected = (0.3864864864696744, 0.5622377622369461, 0.2977973568358142)\n'
                                               '>>> assert all((np.isclose(u, v, atol=1e-06) for u, v in zip(update_parameters_sequence(Y_sequences, p0, p1, p2), expected)))\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1.3}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
