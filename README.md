# DS-Unit-3-Sprint-3-Productization-and-Cloud
Building a real deployed full-stack application, backed by Data Science
--------------------

*Note* - assignments this week are all steps in a larger week-long project. They
are to be worked on in a repo you make with your own account, as instructed in
the first day. You should still fork this repo, and open a PR where you add a
`work_notes.md` file that includes a link to your project repo. You should then
update `work_notes.md` each day with the following:

- What went well (in the context of working on the assignment) today?
- What was particularly interesting or surprising about the topic(s) today?
- What was the most challenging part of the work today, and why?


# Setup
'''sh
pipenv install
'''
# Migrate the database
'''sh
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
# Basilica
'''sh
import basilica
with basilica.Connection('0d0eac92-48c9-b3df-d2af-73b972de69c5') as c:
    embeddings = c.embed_sentences(["Hello world!", "How are you?"])
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]
'''
# Usage

'''sh
FLASK_APP=web_app flask run
'''

