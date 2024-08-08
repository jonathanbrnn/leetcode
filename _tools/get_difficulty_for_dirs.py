import requests
import json

def get_leetcode_problems():
    url = 'https://leetcode.com/graphql'
    query = '''
    {
      allQuestions {
        title
        difficulty
      }
    }
    '''
    response = requests.post(url, json={'query': query})
    data = response.json()
    problems = data['data']['allQuestions']
    return {problem['title']: problem['difficulty'] for problem in problems}

def save_problems(problems, filename):
    with open(filename, 'w') as f:
        json.dump(problems, f, indent=4)

if __name__ == "__main__":
    problems = get_leetcode_problems()
    save_problems(problems, '/Users/jonathan/PycharmProjects/leetcode/_data/difficulties.json')
