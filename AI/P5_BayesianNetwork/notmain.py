# Prior probabilities for StudyHours and ExamDifficulty
cpt_study_hours = {
    'Low': 0.3,
    'Medium': 0.4,
    'High': 0.3
}

cpt_exam_difficulty = {
    'Easy': 0.3,
    'Medium': 0.5,
    'Hard': 0.2
}

# Conditional probabilities for ExamResult given StudyHours and ExamDifficulty
cpt_exam_result = {
    ('Low', 'Easy', 'Pass'): 0.9,
    ('Low', 'Easy', 'Fail'): 0.1,
    ('Low', 'Medium', 'Pass'): 0.7,
    ('Low', 'Medium', 'Fail'): 0.3,
    ('Low', 'Hard', 'Pass'): 0.4,
    ('Low', 'Hard', 'Fail'): 0.6,
    ('Medium', 'Easy', 'Pass'): 0.8,
    ('Medium', 'Easy', 'Fail'): 0.2,
    ('Medium', 'Medium', 'Pass'): 0.6,
    ('Medium', 'Medium', 'Fail'): 0.4,
    ('Medium', 'Hard', 'Pass'): 0.3,
    ('Medium', 'Hard', 'Fail'): 0.7,
    ('High', 'Easy', 'Pass'): 0.7,
    ('High', 'Easy', 'Fail'): 0.3,
    ('High', 'Medium', 'Pass'): 0.4,
    ('High', 'Medium', 'Fail'): 0.6,
    ('High', 'Hard', 'Pass'): 0.2,
    ('High', 'Hard', 'Fail'): 0.8
}

network_structure = {
    'StudyHours': {
        'Parents': [],
        'CPT': cpt_study_hours,
        'Values': ['Low', 'Medium', 'High']
        },
    'ExamDifficulty': {
        'Parents': [],
        'CPT': cpt_exam_difficulty,
        'Values': ['Easy', 'Medium', 'Hard']
        },
    'ExamResult': {
        'Parents': ['StudyHours', 'ExamDifficulty'],
        'CPT': cpt_exam_result,
        'Values': ['Pass', 'Fail']
    }
}

def enumeration_inference(query_variable, evidence, network_structure):
    # Initialize the result probability distribution
    result_probabilities = {}

    # Get the CPT for the query variable
    query_cpt = network_structure[query_variable]['CPT']

    # Iterate through all possible values of the query variable
    for query_value in network_structure[query_variable]['Values']:
        # Initialize the probability for this query_value
        probability = 0.0

        # Iterate through all possible assignments of values to evidence variables
        for evidence_assignment in generate_assignments(evidence, network_structure):
            # Calculate the joint probability P(query_value, evidence_assignment)
            joint_probability = 1.0

            # Build a tuple of values for all relevant variables, including the query variable
            variable_values = tuple(evidence_assignment[var] for var in network_structure if var != query_variable)
            variable_values = (query_value,) + variable_values

            # Multiply the conditional probabilities according to the CPTs
            for variable in network_structure:
                if variable != query_variable:
                    parents_assignment = tuple(evidence_assignment[parent] for parent in network_structure[variable]['Parents'])
                    cpt_key = variable_values + parents_assignment  # Correctly build the key for the CPT
                    for key in cpt_key:
                        joint_probability *= network_structure[variable]['CPT'][key] if key in network_structure[variable]['CPT'] else 2
                    pass
            
            probability += joint_probability

        result_probabilities[query_value] = probability

    # Normalize the probabilities to make them sum to 1
    total_probability = sum(result_probabilities.values())
    result_probabilities = {key: value / total_probability for key, value in result_probabilities.items()}

    return result_probabilities

def generate_assignments(evidence, network_structure):
    # Helper function to generate all possible assignments of values to evidence variables
    # This function returns a generator
    if not evidence:
        yield {}
    else:
        variable = list(evidence.keys())[0]
        for value in network_structure[variable]['Values']:
            for rest_assignment in generate_assignments(evidence={k: v for k, v in evidence.items() if k != variable}, network_structure=network_structure):
                assignment = {variable: value}
                assignment.update(rest_assignment)
                yield assignment

query_variable = 'ExamResult'
evidence = {'ExamDifficulty': 'Low', 'StudyHours': 'Low'}
result = enumeration_inference(query_variable, evidence, network_structure)
print(result)