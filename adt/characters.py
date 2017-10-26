
from adt.items import *

brian = {
    "name": "Brian Ferguson",

    "occupation": "Nurse",

    "age": 26,

    "gender": "male",

    "check": "none",

    "dialogue":["I'm trying to convince trisha to take my next shift."], # If visited before murder scene (6)

    "extra":{
        "dialogue1": ["Can't believe she's dead"] # Hospital murder scene (6)
    }
}
dead_developer = {
    "name": "Dead Developer",

    "occupation": "Nurse",

    "age": 26,

    "gender": "male",

    "check": "none",

    "alive" : False,

    "inventory" : [police_badge],
    "dialogue":[]
}
doctor = {
    "name": "Dr. House",

    "occupation": "Doctor",

    "age": 58,

    "gender": "male",

    "check": "Assault, vandalism, and property destruction.",

    "dialogue":["Gotta go! Building full of sick people, if I hurry, maybe I can avoid them."], # If visited before murder scene (6)
    
    "extra":{
        "dialogue1": ["I saw trisha and brian arguing earlier about their shifts"] # Hospital murder Scene (6)
    }
}
priest = {
    "name": "Father Putin",

    "occupation": "Priest",

    "age": 75,

    "gender": "male",

    "check": "none",

    "dialogue": ["This book is bullsh..... OH!...I didnt see you there."]

}
diane_killer = {
    "name": "Miss Diane Brass",

    "occupation": "Waitress",

    "age":21,

    "gender": "female",

    "check": "The Killer",

    "dialogue": []
}
denzel = {
    "name": "Mr Denzel Brass",

    "occupation": "Sport teacher",

    "age": 60,

    "gender": "male",

    "check": "Committed suicide after the final verdict came back guilty."

}
barry = {
    "name": "Barry Sloane",

    "gender": "male",

    "check": "Murdered by Mr Denzel Brass"
}
smith = {
    "name": "Mr Smith",

    "occupation": "Con artist",

    "age": 27,

    "gender": "male",

    "check": "Mr Steven's Best Friend.",

    "dialogue": []
}
blade = {
    "name": "Blade",

    "occupation": "Unemployed",

    "age": 30,

    "gender": "male",

    "check": "Used to be Mr Steven Cornwall's cellmate.",

    "dialogue": []
}
patrick = {
    "name": "Mr Patrick",

    "occupation": "Bank Manager",

    "age": 47,

    "gender": "male",

    "check": "Brother-in-law to Mr Steven Cornwall.",

    "dialogue": ["How can I help you today?"], # If visited before the murder scene (5)

    "extra":{
        "dialogue1":["I wasn't here when it happened, the CCTV shows that I was in my office"] # Bank murder Scene (5)
    }
}
diane = {
    "name": "Miss Diane B",

    "occupation": "Waitress",

    "age": 21,

    "gender": "female",

    "check": "Mistress to Mr Clark Davidson.",

}
james = {
    "name": "Mr James Robin",

    "occupation": "Business Man",

    "age": 35,

    "gender": "male",

    "check": "Business partner to Mr Clark Davidson since 2013",

    "dialogue": []
}
clark_2 = {
    "name": "Mrs Clark Davidson",

    "occupation": "Wife",

    "age": 30,

    "gender": "female",

    "check": "Filed for divorce",

    "dialogue": []
}
thomas = {
    "name": "Thomas Reese",

    "occupation": "Factory Manager",

    "age": 26,

    "gender": "male",

    "check": "Witness of a 6 year murder investigation.",

    "dialogue": []
}
trisha = {
    "name": "Trisha Banns",

    "occupation": "Nurse",

    "age": 30,

    "gender": "female",

    "check": "Witness of a 6 year murder investigation.",

    "dialogue": ["I'm not taking brian's next shift I've been awake for 30 hours straight."]

}
christine = {
    "name": "Miss Christine Lambart",

    "occupation": "Stripper",

    "age": 28,

    "gender": "female",

    "check": "Possession of illegal substance and a witness in a 6 year murder investigation.",

    "dialogue": []
}
steven = {
    "name": "Mr Steven Cornwall",

    "occupation": "Civil servant",

    "age": 38,

    "gender": "male",

    "check": "Theft, possession of illegal substance and witness in a 6 year murder investigation.",
 
    "dialogue": ["I'm busy, i'm in the middle of a job."],

    "alive" : False
}

kirill = {
    
    "name": "Kirill",

    "occupation": "Barman",

    "age" : 28,

    "gender": "male",

    "check": "none",
    
    "dialogue": ["Hello there Decetive, How can I help you?","Bugs are evil"],
    
}
clark = {
    "name" : "Mr Clark Davidson",

    "occupation": "Plumber",

    "age": 33,

    "gender": "male",

    "check": "Witness in a 6 year murder investigation.",

    "dialogue" : ["Please leave me alone!"],
    "dialogue" : ["Please leave me alone!"],

}
police_man = {
    "name" : "Detective Carter",
    "occupation" : "Homicide Detective",
    "age" : 36,
    "gender" : "male",
    "check" : "none",
    "dialogue" : ["Morning Detective, I think you left your badge in the morgue!"]
}

scene_1_police_officer = {
    "name" : "Police Officer",
    "occupation" : "Copper",
    "age" : 31,
    "gender" : "male",
    "check": "none",
    "dialogue": ["Horrible situation isn't it. The investigative team found an unfired 9mm bullet outside.",
                 "I'd focus on trying to find the murder weapon!"]
}

scene_2_police_officer = {
    "name" : "Lab Technician",
    "occupation" : "Scientists",
    "age" : 12,
    "gender" : "male",
    "check": "none",
    "dialogue": ["Drop that knife and i'll run do some blood analysis for you!",
                 "The results may take a few hours"]
}


getCharacter = {
    "Kirill": kirill,
    "Clark Davidson": clark, 
}


char_list = [kirill,dead_developer,clark,police_man,scene_1_police_officer,scene_2_police_officer,denzel,barry,smith,blade,patrick,diane,james,clark_2,diane_killer,thomas,trisha,christine,steven,doctor,brian,priest]



