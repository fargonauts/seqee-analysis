
def save_problems(df):
    problems = df['problem'].tolist()
    #print(problems)
    with open('problems.txt', 'w') as outfile:
        outfile.write('\n'.join(' '.join(map(str, p)) for p in problems))
