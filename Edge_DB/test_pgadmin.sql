/*
  tests to run on PGAdmin instead of using flask + python
  */

COPY shots TO STDOUT (DELIMITER ',');

INSERT INTO shots (shot_time,
                   process_time,
                   event_id,
                   preprocessed_audio_hash,
                   postprocessed_audio_hash,
                   relative_coords,
                   absolute_coords,
                   gun_type)
VALUES (2023-08-20 10:12:32 +05:00,
        2023-08-20 10:14:10 +05:00,
        1,
        '4204204204204204204204204204204204204204',
        '6969696969696969696969696969696969696969',
        (10, 0, 0), -- r= 10, theta= 0, phi= 0
        (45, 45),
        'ak47'
        );