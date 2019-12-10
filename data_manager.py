import connection as connection

QUESTIONS = 'data/questions.csv'
ANSWERS = 'data/answers.csv'

questions_list = connection.read_questions(QUESTIONS)
answers_list = connection.read_answers(ANSWERS)


def add_question(title, message):
    new_question = {'id': len(questions_list),
                    'submission_time': '',
                    'view_number': 0,
                    'vote_number': 0,
                    'title': title,
                    'message': message,
                    'image': ''
                    }
    questions_list.append(new_question)
    connection.write_questions(QUESTIONS, questions_list)


def add_answer(question_id, message):
    new_answer = {'id': len(answers_list),
                  'submission_time': 0,
                  'vote_number': 0,
                  'question_id': question_id,
                  'message': message,
                  'image': ''}
    answers_list.append(new_answer)
    connection.write_answers(ANSWERS, answers_list)


def vote_question(question_id, option):
    vote_number = questions_list[int(question_id)]['vote_number']
    if option == 'vote_up':
        questions_list[int(question_id)]['vote_number'] = int(vote_number) + 1
        connection.write_questions(QUESTIONS, questions_list)
    elif option == 'vote_down':
        questions_list[int(question_id)]['vote_number'] = int(vote_number) - 1
        connection.write_questions(QUESTIONS, questions_list)


def vote_answer(answer_id, option):
    vote_number = answers_list[int(answer_id)]['vote_number']

    if option == 'vote_up':
        answers_list[int(answer_id)]['vote_number'] = int(vote_number) + 1
        connection.write_answers(ANSWERS, answers_list)
    elif option == 'vote_down':
        answers_list[int(answer_id)]['vote_number'] = int(vote_number) - 1
        connection.write_answers(ANSWERS, answers_list)
    print(answers_list)