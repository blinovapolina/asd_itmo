from collections import defaultdict
from lab6.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def process_elections(candidates_input):
    votes = defaultdict(int)

    for line in candidates_input:
        candidate, vote_count = line.split()
        votes[candidate] += int(vote_count)

    sorted_candidates = sorted(votes.items())

    result = []
    for candidate, votes in sorted_candidates:
        result.append(f'{candidate} {votes}')

    return result


def task_5(input_file, output_file):
    candidates = open_file(input_file)
    inputs = ''.join(candidates)
    result = '\n'.join(process_elections(candidates))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(process_elections, candidates)


if __name__ == '__main__':
    task_5(PATH_INPUT, PATH_OUTPUT)
