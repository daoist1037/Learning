import random

capitals = {    '河北':'石家庄',    '河南':'郑州',     '湖北':'武汉',   '湖南':'长沙' }
for quizNum in range(3):
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerFile = open('capitalsquiz_answer%s.txt' %(quizNum+1) ,'w')

    quizFile.write('Name:\nDate:\nPeriod:\n\n')
    quizFile.write( (' '*20) + 'province capitals Quiz (Form %s)' % (quizNum+1))
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(4):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer,3)
        answerOption = wrongAnswer + [correctAnswer]
        random.shuffle(answerOption)

        quizFile.write('%s. what is the capital of %s\n' %(questionNum+1, states[questionNum]))
        for i in range(4):
            quizFile.write('%s. %s\n'%('ABCD'[i], answerOption[i]))
        quizFile.write('\n')

        answerFile.write('%s. %s\n'  %(questionNum+1, 'ABCD'[answerOption.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()

