
mkdir templates 
python3 scaffold.py user username email password phone country_id:references
python3 scaffold.py country name
python3 scaffold.py programming_session title description user_id:references timestamp pic:file
python3 scaffold.py sewing_session title description user_id:references pic:file timestamp
python3 scaffold.py sport_session title description user_id:references pic:file timestamp
python3 scaffold.py application_development title description user_id:references timestamp pic:file dev_or_prod_mode:radio
