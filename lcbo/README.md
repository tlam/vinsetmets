## Create the table

        psql -U theusername vinsetmets < create.sql

# Convert to a hypertable called a `booze`

        SELECT create_hypertable('booze', 'added_on');
