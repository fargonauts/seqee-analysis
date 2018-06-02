
def save_problems(df):
    problems = df['problem'].tolist()
    with open('problems.txt', 'w') as outfile:
        outfile.write('\n'.join(problems))
