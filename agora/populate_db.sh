# Populate db with initial data
echo populating affiliations
python manage.py loaddata ./fixtures/affiliations.json
echo populating areas of activity
python manage.py loaddata ./fixtures/areas_of_activity.json
echo populating ESFRI domains
python manage.py loaddata ./fixtures/esfridomains.json
echo populating ESFRI types
python manage.py loaddata ./fixtures/esfritypes.json
echo populating providers
python manage.py loaddata ./fixtures/organisations.json
echo populating societal grand challenges
python manage.py loaddata ./fixtures/societal_grand_challenges.json
echo populating structure types
python manage.py loaddata ./fixtures/structures.json
echo populating target users
python manage.py loaddata ./fixtures/target_users.json
echo populating users
python manage.py loaddata ./fixtures/users.json
