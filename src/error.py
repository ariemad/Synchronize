import sys

def throw_and_exit(e):
    print(f"Error: {e}")
    sys.exit(0)

def throw_missing_keys(missingKeys):
    print('The following keys are missing in the config:')
    for key in missingKeys:
        print('-',key)
    print()
    throw_and_exit('Missing Keys')

def throw_incorrect_paths(incorrectPaths):
    print('The following paths are incorrect in the config:')
    for key in incorrectPaths:
        print(key,':', incorrectPaths[key])
    print()
    throw_and_exit('Incorrect Path')