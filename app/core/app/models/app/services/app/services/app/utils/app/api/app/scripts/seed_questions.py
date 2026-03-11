from app.core.database import questions_collection

questions = [

{
"question":"What is 8 × 9?",
"options":["72","81","64","70"],
"correct_answer":"72",
"difficulty":0.3,
"topic":"Algebra",
"tags":["multiplication"]
},

{
"question":"Solve: x + 6 = 10",
"options":["2","3","4","5"],
"correct_answer":"4",
"difficulty":0.4,
"topic":"Algebra",
"tags":["equation"]
},

{
"question":"15% of 200?",
"options":["20","25","30","40"],
"correct_answer":"30",
"difficulty":0.5,
"topic":"Arithmetic",
"tags":["percentage"]
},

{
"question":"Synonym of 'abundant'",
"options":["rare","plentiful","tiny","weak"],
"correct_answer":"plentiful",
"difficulty":0.6,
"topic":"Vocabulary",
"tags":["synonym"]
}

]

questions_collection.insert_many(questions)

print("Questions inserted")
