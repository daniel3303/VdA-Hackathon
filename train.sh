# connects to the database and updates the data fields
./update_data_files.py

# trains the model
python -m rasa_nlu.train -c config/config.yml --data data/nlu/ -o models --fixed_model_name glosa --project current
python -m rasa_core.train -d data/dialogue/domain.yml -s data/dialogue/stories.md -o models/dialogue #-c config/dialogue.yml