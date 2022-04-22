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
        'video': ['https://www.youtube.com/embed/WPBdbYR5Bnk?start=133&end=340'],
        'hint': [['Establish position', 'A defensive player with both feet standing on the ground and torso square facing the opponent is said to have established position.']],
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
        'video': [
            "https://www.youtube.com/embed/01NsieAjzdU?start=118&end=158",
            'https://www.youtube.com/embed/ERzhKUakC6M?end=20'
        ],
        'hint':[],
        'type': 'd'
    },
    {
        'id': 3,
        'name': 'Hand Check',
        'description': "When a player continually uses their hands on an opposing player. This foul is typically called on defenders at the perimeter to keep a safe distance between the ball handler and the basket.",
        'img': 'https://dsgmedia.blob.core.windows.net/pub/2017/12/HandCheck1.jpg',
        'video': [
            "https://www.youtube.com/embed/VLHqHDCw3JI"
        ],
        'hint':[],
        'type': 'd'
    },
    {
        'id': 4,
        'name': 'Travelling',
        'description': "When an offensive player takes more than two steps with the ball or moves their pivot foot after the player has stopped dribbling or takes any step before dribbling, a travelling violation will be called.",
        'img': 'https://dsgmedia.blob.core.windows.net/pub/2017/12/Traveling.jpg',
        'video': ["https://www.youtube.com/embed/J5xGKioMsIo?start=128&end=155"],
        'hint': [
            ['Pivot Foot', "When a player lands with one foot when performs a jump shot, the landing foot is the pivot foot, and when a players lands with both feet, either can be pivot foot."],
            ['Two Steps', "The two steps starts counting when the player stops dribbling and gaining full control of the basketball. So while moving and having one foot on the floor while catching the ball or ending a dribble the next foot or feet to touch the floor is step one and will become the pivot foot. The catching step is step 0."]
        ],
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
        'video': [
            "https://www.youtube.com/embed/H8bbQZCHSF8?start=255&end=277",
            "https://www.youtube.com/embed/H8bbQZCHSF8?start=370&end=394",
            "https://www.youtube.com/embed/H8bbQZCHSF8?start=419&end=441"
        ],
        'hint':[],
        'type': 'o'
    },
    {
        'id': 6,
        'name': 'Charging',
        'description': "When an offensive player makes contact with a defender or moving into a defender’s torso who has established position in front of an offensive player with or without the basketball and is not moving. Some courts, especially those used for youth basketball, make this call easier to identify by having a “charge circle” marked below the basket. If a defender is outside the circle with their feet planted, it is a charge.",
        'img': 'https://dsgmedia.blob.core.windows.net/pub/2017/12/Charging_Pushing.jpg',
        'video': [
            "https://www.youtube.com/embed/WnNT0Sy226w?start=129&end=153"
        ],
        'hint':[],
        'type': 'o'
    },
]

quizzes = [
    {
        "id":"1",
        "question":"What rule or violation is violated in the following GIF based on the hand signal of referee?",
        "hint":"Think about if offensive player takes more than two steps with the ball or moves their pivot foot after the player has stopped dribbling or takes any step before dribbling.",
        "choice":["Illegal Screen","Blocking","Charging","Travelling"],
        "img":"https://c.tenor.com/uYWM4E5tzEcAAAAC/referee-travel.gif"
    
    },
    {
        "id":"2",
        "question":"What is the foul or violation in the following play?",
        "hint":"Look carefully to see whether it's an offensive foul or a defensive foul.",
        "choice":["Blocking","Illegal Screen","Charging","Hand Check"],
        "video":"zfpBxKjYLT8",
        "start":"37",
        "stop":"52",
        "mute":"no"
    },
    {
        "id":"3",
        "question":"What is the foul or violation in the following play?",
        "hint":"Does the defender establish the position?",
        "choice":["Charging","Blocking","Illegal Use of Hands","Illegal Screen"],
        "video":"UJbBUi7SgtM",
        "start":"63",
        "stop":"66",
        "mute":"yes"
    },
    {
        "id":"4",
        "question":"What rule or violation is violated in the following image based on the hand signal of referee?",
        "hint":"Maybe to focus on the hand.",
        "choice":["Illegal Use of Hands","Hand Check","Travelling","Blocking"],
        "img":"https://dsgmedia.blob.core.windows.net/pub/2017/12/HandCheck1.jpg"
    },
    {
        "id":"5",
        "question":"Did the player in 10 red violate any rule? If he did, what rule did he break?",
        "hint":"Look carefully on whether he had a contact with the other player.",
        "choice":["No, he did not violate any rules.","Yes, he made a charging foul.","Yes, he made a illegal screen foul.","Yes, he made a travelling foul."],
        "video":"t9Z58NOR6c8",
        "start":"21",
        "stop":"30",
        "mute":"no"
    },
    {
        "id":"6",
        "question":"What is the foul or violation in the following play?",
        "hint":"Look carefully on whether he had a contact with the other player.",
        "choice":["Hand Check","Charging","Illegal Screen","Illegal Use of Hand"],
        "video":"sRYsGCKrLlI",
        "start":"73",
        "stop":"79",
        "mute":"yes"
    },
    {
        "id":"7",
        "question":"To distinguish between charging and blocking is difficult, can you get it right?",
        "hint":"Look carefully on whether the defender had establish a legal position.",
        "choice":["Blocking","Charging"],
        "video":"3fmalq_EGMY",
        "start":"152",
        "stop":"156",
        "mute":"no"
    },
    {
        "id":"8",
        "question":"Sometimes it is hard to judge whether it is a travelling foul, can you get it right?",
        "hint":"If an offensive player takes more than two steps with the ball or moves their pivot foot after the player has stopped dribbling or takes any step before dribbling, then it results in a travelling foul.",
        "choice":["Yes, it is a travelling foul.","No, it isn't."],
        "video":"x0h_ETeFGCg",
        "start":"264",
        "stop":"270",
        "mute":"no"
    },
    {
        "id":"9",
        "question":"Did the player in 1 white make an illegal screen faul?",
        "hint":"When a player fails to maintain a set position or doesn't allow the defender the opportunity to avoid contact while setting a screen or pick, a illegal screen will be given. Screens must be performed in a standstill manner. A step must separate the screener and defender while the screener may not move laterally or towards the defender that they are setting the screen on.",
        "choice":["Yes, it is an illegal screen faul.","No, it isn't."],
        "video":"e7aErY-r414",
        "start":"71",
        "stop":"76",
        "mute":"no"
    },
    {
        "id":"10",
        "question":"What rule or violation is violated in the following GIF?",
        "hint":"First make sure which player break the rule, offensive or defensive player?",
        "choice":["Blocking","Illegal Use of Hand","Hand Check","Charging"],
        "img":"http://fc02.deviantart.net/fs71/f/2010/263/0/5/kbwadeshot_by_immortal24-d2z4szz.gif"
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
        "answer":"Travelling"
    },
    {
        "id":"2",
        "answer":"Blocking"
    },
    {
        "id":"3",
        "answer":"Charging"
    },
    {
        "id":"4",
        "answer":"Hand Check"
    },
    {
        "id":"5",
        "answer":"Yes, he made a illegal screen foul."
    },
    {
        "id":"6",
        "answer":"Illegal Use of Hand"
    },
    {
        "id":"7",
        "answer":"Blocking"
    },
    {
        "id":"8",
        "answer":"Yes, it is a travelling foul."
    },
    {
        "id":"9",
        "answer":"Yes, it is an illegal screen faul."
    },
    {
        "id":"10",
        "answer":"Hand Check"
    }
]

tracking = []

#initial score
score = 0

@app.route("/")
def home_page():
    return render_template('home.html', learning=learning, tracking=tracking)

@app.route("/quiz_start")
def quiz_start():
    return render_template('quiz_start.html')

@app.route("/quiz/<id>")
def quiz(id = None):
    global quizzes
    id = int(id)
    id -= 1
    print(id)
    data = quizzes[id]
    print(data)
    if 'img' in data:
        return render_template("quiz.html", data = data)
    elif 'video' in data:
        return render_template("quiz_video.html", data = data)

@app.route("/checkAnswer", methods=["POST", "GET"])
def check():
    global score
    global UserChoiceOnQuiz
    global AnswerForQuiz

    if "POST" == request.method:
        if "radAnswer" in request.form:
            print(request.form)
            UserAnswer = request.form['radAnswer']
            quizNumber = request.form['button']
            currentTime = datetime.now()
            timestring = currentTime.strftime("%Y-%m-%d %H:%M:%S")

            #store user's state to UserChoiceOnQuiz
            UserChoiceOnQuiz[int(quizNumber)-1]['answer'] = UserAnswer
            UserChoiceOnQuiz[int(quizNumber)-1]['submitTime'] = timestring
            print(UserChoiceOnQuiz)

            #compare to the correct answer
            correcrAnswer = AnswerForQuiz[int(quizNumber)-1]['answer']
            print("correct answer:",correcrAnswer)

            #if correct
            if UserAnswer == correcrAnswer:
                score += 1
                print('score:',score)
            if "img" in quizzes[int(quizNumber)-1]:
                return render_template("quiz_feedback.html", data = quizzes[int(quizNumber)-1], score = score, UserAnswer = UserAnswer, correcrAnswer = correcrAnswer)
            else:
                return render_template("quiz_feedback_video.html", data = quizzes[int(quizNumber)-1], score = score, UserAnswer = UserAnswer, correcrAnswer = correcrAnswer)

@app.route("/final")
def final():
    global score
    return render_template("final.html",score = score)

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
    print(tracking)
    return jsonify(0)

if __name__ == '__main__':
   app.run(debug = True)
