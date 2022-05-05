from crypt import methods
import re
from flask import Flask
from flask import render_template, request, jsonify, Response, redirect
import random
import datetime
from datetime import datetime

app = Flask(__name__)

learning = [
    {
        'id': 1,
        'name': 'Blocking Foul',
        'description': 'When a defender makes contact with an offensive player without establishing position, without giving proper space or is in the charge circle, a blocking foul will be given.',
        'img': 'https://dsgmedia.blob.core.windows.net/pub/2017/12/Blocking.jpg',
        'acc': 'Ref showing blocking foul signal',
        'video': ['https://www.youtube.com/embed/WPBdbYR5Bnk?start=133&end=340&controls=0'],
        'vacc': 'Video of a blocking foul',
        'hint': [['Establish position', 'A defensive player with both feet standing on the ground and torso square facing the opponent is said to have established position.',"0"],
                ],
        'learn': 'In the video, it teaches you the blocking foul in details and you can watch in-gaame plays to help you determine whether it is a blocking foul.',
        'type': 'd'
    },
    {
        'id': 2,
        'name': 'Illegal Use of Hands',
        'description': "When a defender uses their hands in a fashion that referees deem illegal, typically in the form of touching a shooter's arm or hand through their release or touching after an attempted steal, a illegal use of hands, also called reaching in foul, will be given.",
        'Examples': ['When defender puts both hands on offensive player', 
                    'When defender slaps or hits the arm of offensive player, especially when shooting',
            ],
        'img': 'https://dsgmedia.blob.core.windows.net/pub/2017/12/IllegalHandUse_ReachingIn.jpg',
        'acc': 'Ref showing illegal use of hands foul signal',
        'video': [
            "https://www.youtube.com/embed/01NsieAjzdU?start=118&end=158&controls=0",
            'https://www.youtube.com/embed/ERzhKUakC6M?end=20&controls=0'
        ],
        'vacc': 'Video of a illegal use of hands',
        'hint':[],
        'learn':  'In the video, it explains with in-game example why illegal use of hand is called by the referee and helps you understand the rule better.',
        'type': 'd'
    },
    {
        'id': 3,
        'name': 'Hand Check',
        'description': "When a player continually uses their hands on an opposing player. This foul is typically called on defenders at the perimeter to keep a safe distance between the ball handler and the basket.",
        'img': 'https://dsgmedia.blob.core.windows.net/pub/2017/12/HandCheck1.jpg',
        'acc': 'Ref showing hand check foul signal',
        'video': [
            "https://www.youtube.com/embed/01NsieAjzdU?start=117&end=229&controls=0"
        ],
        'vacc': 'Video of hand check',
        'hint':[],
        'learn':'In the video, it teaches you the hand check in details with examples.', 
        'type': 'd'
    },
    {
        'id': 4,
        'name': 'Travelling',
        'description': "When an offensive player takes more than two steps with the ball or moves their pivot foot after the player has stopped dribbling or takes any step before dribbling, a travelling violation will be called.",
        'img': 'https://dsgmedia.blob.core.windows.net/pub/2017/12/Traveling.jpg',
        'acc': 'Ref showing travelling foul signal',
        'video': ["https://www.youtube.com/embed/J5xGKioMsIo?start=128&end=155&controls=0"],
        'vacc': 'Video of travelling',
        'hint': [
            ['Pivot Foot', "When a player lands with one foot when performs a jump shot, the landing foot is the pivot foot, and when a players lands with both feet, either can be pivot foot.","0"],
            ['Gather Step', "Gather step refers to the step players take when they stop dribbling and gain full control of the ball. The two steps starts counting after the gather step. So while moving and having one foot on the floor while catching the ball or ending a dribble the next foot or feet to touch the floor is step one and will become the pivot foot. The gather step is step 0.","1"],
            ],
        'learn': 'In the video, it teaches you what is gather step and how the steps are counted in detail. You can also learn from in-game play.',
        'type': 'o'
    },
    # {
    #     'id': 8,
    #     'name': 'Traveling Special Caes',
    #     'video': [
    #         'A player who falls to the floor with the ball has not traveled unless they get up to at least one knee.',
    #         'Rolling over to get away from another player is traveling.',
    #         'Sliding along the floor is not traveling.',
    #         'A player may not touch the floor consecutively with the same foot or both feet after ending his dribble or gaining control of the ball.'
    #     ],
    #     'type': 'o'
    # },
    {
        'id': 5,
        'name': 'Illegal Screen',
        'description': "When a player fails to maintain a set position or doesn't allow the defender the opportunity to avoid contact while setting a screen or pick, a illegal screen will be given. Screens must be performed in a standstill manner. A step must separate the screener and defender while the screener may not move laterally or towards the defender that they are setting the screen on.",
        'Examples': ["Illegal use of hands while screening; such as holding, pushing or hitting the defender.", 
                    "Setting the screen and leaning in with the shoulder and or bumping the defender.", 
                    "Sticking out the leg to prevent the player."
                ],
        'img': 'https://dsgmedia.blob.core.windows.net/pub/2017/12/Moving_PickScreen.jpg',
        'acc': 'Ref showing illegal screen foul signal',
        'video': [
            "https://www.youtube.com/embed/H8bbQZCHSF8?start=255&end=305&controls=0",
            "https://www.youtube.com/embed/H8bbQZCHSF8?start=370&end=394&controls=0",
            "https://www.youtube.com/embed/H8bbQZCHSF8?start=419&end=441&controls=0"
        ],
        'vacc': 'Video of an illegal screen',
        'hint':[],
        'learn': 'In the video, it includes several examples of illegal screen to help you learn better and accurately identify an illegal screen when it happens.',
        'type': 'o'
    },
    {
        'id': 6,
        'name': 'Charging',
        'description': "When an offensive player makes contact with a defender or moving into a defender’s torso who has established position in front of an offensive player with or without the basketball and is not moving. Some courts, especially those used for youth basketball, make this call easier to identify by having a “charge circle” marked below the basket. If a defender is outside the circle with their feet planted, it is a charge.",
        'img': 'https://dsgmedia.blob.core.windows.net/pub/2017/12/Charging_Pushing.jpg',
        'acc': 'Ref showing charging foul signal',
        'video': [
            "https://www.youtube.com/embed/WnNT0Sy226w?start=129&end=153&controls=0"
        ],
        'vacc': 'Video of charging foul',
        'hint':[],
        'learn': 'In the video, it shows you all the charging foul drew by 2022 Defensive player of the year Marcus Smart and allows you to learn from the plays.',
        'type': 'o'
    },
]

quizzes = [
    {
        "id":"1",
        "question":"What rule or violation is violated in the following GIF based on the hand signal of referee?",
        "hint":"Think about if offensive player takes more than two steps with the ball or moves their pivot foot after the player has stopped dribbling or takes any step before dribbling.",
        "choice":[{"option":"A","selection":"Illegal Screen"},{"option":"B","selection":"Blocking"},{"option":"C","selection":"Charging"},{"option":"D","selection":"Travelling"}],
        "img":"https://c.tenor.com/uYWM4E5tzEcAAAAC/referee-travel.gif",
        'acc': 'Image of a foul'
    },
    {
        "id":"2",
        "question":"What is the foul or violation in the following play?",
        "hint":"Look carefully to see whether the player in dark jersey is in an established guarding position. Whether he is there before the player in white.",
        "choice":[{"option":"A","selection":"Blocking"},{"option":"B","selection":"Illegal Screen"},{"option":"C","selection":"Charging"},{"option":"D","selection":"Hand Check"}],
        "video":"zfpBxKjYLT8",
        'acc': 'Video of a foul',
        "start":"83",
        "stop":"110",
        "mute":"yes"
    },
    {
        "id":"3",
        "question":"What is the foul or violation in the following play?",
        "hint":"Does the defender establish the position?",
        "choice":[{"option":"A","selection":"Charging"},{"option":"B","selection":"Blocking"},{"option":"C","selection":"Illegal Use of Hands"},{"option":"D","selection":"Illegal Screen"}],
        "video":"UJbBUi7SgtM",
        'acc': 'Video of a foul',
        "start":"63",
        "stop":"66",
        "mute":"yes"
    },
    {
        "id":"4",
        "question":"What rule or violation is violated in the following image based on the hand signal of referee?",
        "hint":"Maybe to focus on the hand.",
        "choice":[{"option":"A","selection":"Illegal Use of Hands"},{"option":"B","selection":"Hand Check"},{"option":"C","selection":"Travelling"},{"option":"D","selection":"Blocking"}],
        "img":"https://dsgmedia.blob.core.windows.net/pub/2017/12/HandCheck1.jpg",
        'acc': 'Image of a foul'
    },
    {
        "id":"5",
        "question":"Did the player in 21 white violate any rule? If he did, what rule did he break?",
        "hint":"Look carefully on whether he had a contact with the other player.",
        "choice":[{"option":"A","selection":"No, he did not violate any rules."},{"option":"B","selection":"Yes, he made a charging foul."},{"option":"C","selection":"Yes, he made a illegal screen foul."},{"option":"D","selection":"Yes, he made a travelling violation."}],
        "video":"H8bbQZCHSF8",
        'acc': 'Video of a foul',
        "start":"90",
        "stop":"101",
        "mute":"yes"
    },
    {
        "id":"6",
        "question":"What is the foul or violation in the following play?",
        "hint":"Look carefully on whether he had a contact with the other player.",
        "choice":[{"option":"A","selection":"Hand Check"},{"option":"B","selection":"Charging"},{"option":"C","selection":"Illegal Screen"},{"option":"D","selection":"Illegal Use of Hand"}],
        "video":"aZarLAPyj-c",
        'acc': 'Video of a foul',
        "start":"198",
        "stop":"205",
        "mute":"yes"
    },
    {
        "id":"7",
        "question":"To distinguish between charging and blocking is difficult, can you get it right?",
        "hint":"Look carefully on whether the defender had establish a legal position.",
        "choice":[{"option":"A","selection":"Blocking"},{"option":"B","selection":"Charging"}],
        "video":"8Oj5R6kzFfY",
        'acc': 'Video of a foul',
        "start":"33",
        "stop":"49",
        "mute":"yes"
    },
    {
        "id":"8",
        "question":"Sometimes it is hard to judge whether it is a travelling foul, can you get it right?",
        "hint":"If an offensive player takes more than two steps with the ball or moves their pivot foot after stopped dribbling or takes any step before dribbling, then it results in a travelling violation. Think carefully about the gather step.",
        "choice":[{"option":"A","selection":"Yes, it is a travelling."},{"option":"B","selection":"No, it isn't."}],
        "video":"KZu5iE7yrPI",
        'acc': 'Video of a foul',
        "start":"23",
        "stop":"32",
        "mute":"yes"
    },
    {
        "id":"9",
        "question":"Did the player in 1 white make an illegal screen violation?",
        "hint":"Think about whether the player has established his position and allowed the defender to avoid contact. Consider if the screener is moving laterally or towards the defender that they are setting the screen on.",
        "choice":[{"option":"A","selection":"Yes, it is an illegal screen faul."},{"option":"B","selection":"No, it isn't."}],
        "video":"e7aErY-r414",
        'acc': 'Video of a foul',
        "start":"71",
        "stop":"76",
        "mute":"yes"
    },
    {
        "id":"10",
        "question":"What rule or violation is violated in the following GIF?",
        "hint":"First make sure which player break the rule, offensive or defensive player?",
        "choice":[{"option":"A","selection":"Blocking"},{"option":"B","selection":"Illegal Use of Hand"},{"option":"C","selection":"Hand Check"},{"option":"D","selection":"Charging"}],
        "img":"http://fc02.deviantart.net/fs71/f/2010/263/0/5/kbwadeshot_by_immortal24-d2z4szz.gif",
        'acc': 'Image of a foul'
    }
]

UserChoiceOnQuiz = [
    {
        "id":"1",
        "answer": "",
        "submitTime": ""
    },
    {
        "id":"2",
        "answer": "",
        "submitTime": ""
    },
    {
        "id":"3",
        "answer": "",
        "submitTime": ""
    },
    {
        "id":"4",
        "answer": "",
        "submitTime": ""
    },
    {
        "id":"5",
        "answer": "",
        "submitTime": ""
    },
    {
        "id":"6",
        "answer": "",
        "submitTime": ""
    },
    {
        "id":"7",
        "answer": "",
        "submitTime": ""
    },
    {
        "id":"8",
        "answer": "",
        "submitTime": ""
    },
    {
        "id":"9",
        "answer": "",
        "submitTime": ""
    },
    {
        "id":"10",
        "answer": "",
        "submitTime": ""
    }
]

AnswerForQuiz = [
    {
        "id":"1",
        "answer":"Travelling",
        "choice": "D"
    },
    {
        "id":"2",
        "answer":"Charging",
        "choice":"C"
    },
    {
        "id":"3",
        "answer":"Charging",
        "choice":"A"
    },
    {
        "id":"4",
        "answer":"Hand Check",
        "choice" : "B"
    },
    {
        "id":"5",
        "answer":"Yes, he made a illegal screen foul.",
        "choice" : "C"
    },
    {
        "id":"6",
        "answer":"Illegal Use of Hand",
        "choice" : "D"
    },
    {
        "id":"7",
        "answer":"Charging",
        "choice" : "B"
    },
    {
        "id":"8",
        "answer":"No, it isn't.",
        "choice" : "B"
    },
    {
        "id":"9",
        "answer":"Yes, it is an illegal screen faul.",
        "choice":"A"
    },
    {
        "id":"10",
        "answer":"Hand Check",
        "choice" : "C"
    }
]

Answers = ['D','C','A','B','C','D','B','B','A','C']

userchoice = []

tracking = []

#initial score array
score = []

@app.route("/")
def home_page():
    return render_template('home.html', learning=learning, tracking=tracking)

@app.route("/quiz_start")
def quiz_start():
    userchoice.clear()
    score.append(0)
    print(score)
    return render_template('quiz_start.html')

@app.route("/quiz/<id>")
def quiz(id = None):
    global quizzes
    id = int(id)
    id -= 1
    data = quizzes[id]
    if 'img' in data:
        return render_template("quiz.html", data = data, process = (int(data['id']))*10, userChoice = userchoice, correctChoice = Answers)
    elif 'video' in data:
        return render_template("quiz_video.html", data = data, process = (int(data['id']))*10, userChoice = userchoice, correctChoice = Answers)

@app.route("/checkAnswer", methods=["POST", "GET"])
def check():
    global score
    global UserChoiceOnQuiz
    global AnswerForQuiz
    
    print(score)
    print(request.form)
    currentScore = score[-1]

    if "POST" == request.method:
        if "radAnswer" in request.form:
            UserAnswer = request.form['radAnswer']
            quizNumber = request.form['button']
            currentTime = datetime.now()
            timestring = currentTime.strftime("%Y-%m-%d %H:%M:%S")

            #store user's state to UserChoiceOnQuiz
            UserChoiceOnQuiz[int(quizNumber)-1]['answer'] = UserAnswer
            UserChoiceOnQuiz[int(quizNumber)-1]['submitTime'] = timestring
            

            #compare to the correct answer
            correcrAnswer = AnswerForQuiz[int(quizNumber)-1]['answer']
            correctChoice = AnswerForQuiz[int(quizNumber)-1]['choice']
            
            print("correctChoice:",correctChoice)

            allchoices = quizzes[int(quizNumber)-1]
            for item in allchoices['choice']:
                if item['selection'] == UserAnswer:
                    userChoice = item['option']
                    userchoice.append(userChoice)
            print("userChoice:",  userchoice)

            #if correct
            if UserAnswer == correcrAnswer:
                currentScore += 1
                score[-1] = currentScore
                print(score)
            if "img" in quizzes[int(quizNumber)-1]:
                return render_template("quiz_feedback.html", data = quizzes[int(quizNumber)-1], cscore = score[-1], UserAnswer = UserAnswer, correcrAnswer = correcrAnswer,process = (int(quizNumber))*10, userChoice = userchoice, correctChoice = Answers)
            else:
                return render_template("quiz_feedback_video.html", data = quizzes[int(quizNumber)-1], cscore = score[-1], UserAnswer = UserAnswer, correcrAnswer = correcrAnswer,process = (int(quizNumber))*10, userChoice = userchoice, correctChoice = Answers)

@app.route("/final")
def final():
    global score
    return render_template("final.html",score = score[-1],userChoice = userchoice, correctChoice = Answers)

@app.route("/learning/<ftype>/<index>")
def learningpage(ftype = None, index = None):
    data = []
    for foul in learning:
        if foul['type'] == ftype:
            data.append(foul)
    return render_template("learning.html", data = data, ftype = ftype, index = int(index))

@app.route("/defensive")
def defensive_page():
    return render_template("defensive.html")
    
@app.route("/offensive")
def offensive_page():
    return render_template("offensive.html")

@app.route('/track_learning', methods=['GET', 'POST'])
def track_learning():
    global tracking

    curr_location = request.get_json()
    tracking.append(curr_location)
    return jsonify(0)

if __name__ == '__main__':
   app.run(debug = True)
