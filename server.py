from crypt import methods
from flask import Flask
from flask import render_template, request, jsonify, Response, redirect
import random
app = Flask(__name__)

learning = [
    {
        'id': 1,
        'name': 'Blocking Foul',
        'description': 'When a defender makes contact with an offensive player without establishing position, without giving proper space or is in the charge circle, a blocking foul will be given.',
        'img': 'https://dsgmedia.blob.core.windows.net/pub/2017/12/Blocking.jpg',
        'video': ['https://www.youtube.com/embed/WPBdbYR5Bnk?start=133&end=340']
    },
    {
        'id': 2,
        'name': 'Establish position',
        'description': 'A defensive player with both feet standing on the ground and torso square facing the opponent is said to have established position.',
    },
    {
        'id': 3,
        'name': 'Illegal Use of Hands',
        'description': "When a defender uses their hands in a fashion that referees deem illegal, typically in the form of touching a shooter’s arm or hand through their release or touching after an attempted steal, a illegal use of hands, also called reaching in foul, will be given.",
        'Examples': ['When defender puts both hands on offensive player', 
                    'When defender slaps or hits the arm of offensive player, especially when shooting',
            ],
        'img': 'https://dsgmedia.blob.core.windows.net/pub/2017/12/IllegalHandUse_ReachingIn.jpg',
        'video': [
            "https://www.youtube.com/embed/01NsieAjzdU?start=118&end=158",
            'https://www.youtube.com/embed/ERzhKUakC6M?end=20'
        ]
    },
    {
        'id': 4,
        'name': 'Hand Check',
        'description': "When a player continually uses their hands on an opposing player. This foul is typically called on defenders at the perimeter to keep a safe distance between the ball handler and the basket.",
        'img': 'https://dsgmedia.blob.core.windows.net/pub/2017/12/HandCheck1.jpg',
        'video': [
            "https://www.youtube.com/embed/VLHqHDCw3JI"
        ]
    },
    {
        'id': 5,
        'name': 'Travelling',
        'description': "When an offensive player takes more than two steps with the ball or moves their pivot foot after the player has stopped dribbling or takes any step before dribbling, a travelling violation will be called.",
        'img': 'https://dsgmedia.blob.core.windows.net/pub/2017/12/Traveling.jpg',
    },
    {
        'id': 6,
        'name': 'Pivot Foot',
        'description': "When a player lands with one foot when performs a jump shot, the landing foot is the pivot foot, and when a players lands with both feet, either can be pivot foot.",
    },
    {
        'id': 7,
        'name': 'Two Steps',
        'description': "The two steps starts counting when the player stops dribbling and gaining full control of the basketball. So while moving and having one foot on the floor while catching the ball or ending a dribble the next foot or feet to touch the floor is step one and will become the pivot foot. The catching step is step 0.",
        'video': [
            "https://www.youtube.com/embed/J5xGKioMsIo?start=128&end=155"
        ]
    },
    {
        'id': 8,
        'name': 'Traveling Speical Caes',
        'video': [
            'A player who falls to the floor with the ball has not traveled unless they get up to at least one knee.',
            'Rolling over to get away from another player is traveling.',
            'Sliding along the floor is not traveling.',
            'A player may not touch the floor consecutively with the same foot or both feet after ending his dribble or gaining control of the ball.'
        ]
    },
    {
        'id': 9,
        'name': 'Illegal Screen',
        'description': "When a player fails to maintain a set position or doesn’t allow the defender the opportunity to avoid contact while setting a screen or pick, a illegal screen will be given. Screens must be performed in a standstill manner. A step must separate the screener and defender while the screener may not move laterally or towards the defender that they are setting the screen on.",
        'Examples': ["Illegal use of hands while screening; such as holding, pushing or hitting the defender.", 
                    "Setting the screen and leaning in with the shoulder and or bumping the defender.", 
                    "Sticking out the leg to prevent the player."
                ],
        'img': 'https://dsgmedia.blob.core.windows.net/pub/2017/12/Moving_PickScreen.jpg',
        'video': [
            "https://www.youtube.com/embed/H8bbQZCHSF8?start=255&end=277",
            "https://www.youtube.com/embed/H8bbQZCHSF8?start=370&end=394",
            "https://www.youtube.com/embed/H8bbQZCHSF8?start=419&end=441"
        ]
    },
    {
        'id': 10,
        'name': 'Charging',
        'description': "When an offensive player makes contact with a defender or moving into a defender’s torso who has established position in front of an offensive player with or without the basketball and is not moving. Some courts, especially those used for youth basketball, make this call easier to identify by having a “charge circle” marked below the basket. If a defender is outside the circle with their feet planted, it is a charge.",
        'img': 'https://dsgmedia.blob.core.windows.net/pub/2017/12/Charging_Pushing.jpg',
        'video': [
            "https://www.youtube.com/embed/WnNT0Sy226w?start=129&end=153"
        ]
    },
]

@app.route("/")
def home_page():
    return render_template('home.html')