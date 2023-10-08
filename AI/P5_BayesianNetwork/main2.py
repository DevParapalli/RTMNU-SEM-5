from typing import Any

def joint_probability_distribution(variables: dict[str, Any], network: dict) -> float:
    """
    Computes the joint probability distribution of a set of variables given a Bayesian network.

    :param variables: A list of variable names.
    :param values: A list of values for each variable.
    :param network: A Bayesian network.
    :return: The joint probability distribution of the variables.
    """
    
    joint = 0
    for i, variable in enumerate(variables):
        if i == 0:
            joint = probability(variable, variables[variable], variables, network)
        else:
            joint *= probability(variable, variables[variable], variables, network)
    
    return joint



def probability(variable, value: str, variables, network) -> float:
    """
    Computes the probability of a variable given its parents.

    :param variable: The name of a variable (the one whos probablity we want to compute)
    :param value: The value of the variable. 
    :param variables: A dict of variables and their values. (for parents reference)
    :param network: A Bayesian network.
    :return: The probability of the variable.
    """
    parents = network[variable]['Parents']
    if len(parents) == 0:
        return network[variable]['CPT'][(value,)]
    else:
        _cpt_values = []
        for parent in parents:
            _cpt_values.append(variables[parent])
        _cpt_values.append(value)
        return network[variable]['CPT'][tuple(_cpt_values)]

NETWORK = {
    'Burglary': {
        'CPT': {
            ('True',): 0.002,
            ('False',): 0.998,
        },
        'Parents': [],
    },
    'Fire': {
        'CPT': {
            ('True',): 0.001,
            ('False',): 0.999,
        },
        'Parents': [],
    },
    'Alarm': {
        'CPT': {
            ('True', 'True', 'True'): 0.94,
            ('True', 'True', 'False'): 0.06,
            ('True', 'False', 'True'): 0.95,
            ('True', 'False', 'False'): 0.04,
            ('False', 'True', 'True'): 0.31,
            ('False', 'True', 'False'): 0.69,
            ('False', 'False', 'True'): 0.001,
            ('False', 'False', 'False'): 0.999,
        }, 
        'Parents': ['Burglary', 'Fire'],
    },
    'David': {
        'CPT': {
            ('True', 'True'): 0.91,
            ('True', 'False'): 0.09,
            ('False', 'True'): 0.05,
            ('False', 'False'): 0.95,
        }, 
        'Parents': ['Alarm'],
    },
    'Sophia': {
        'CPT': {
            ('True', 'True'): 0.75,
            ('True', 'False'): 0.25,
            ('False', 'True'): 0.02,
            ('False', 'False'): 0.98,
        }, 
        'Parents': ['Alarm'],
    }
}

def main():
    print(joint_probability_distribution({
        'Burglary': 'False',
        'Fire': 'False',
        'Alarm': 'True',
        'David': 'True',
        'Sophia': 'True',
    }, NETWORK))


if __name__ == '__main__':
    main()