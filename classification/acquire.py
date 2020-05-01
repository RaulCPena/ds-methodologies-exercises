import pandas as pd
import env

# new eddit s I can commit this properly


def get_db_url(dbname) -> str:
    url = 'mysql+pymysql://{}:{}@{}/{}'
    return url.format(env.user, env.password, env.host, dbname)

# Function for eaxercise
def get_titanic_data():
    return pd.read_sql('SELECT * FROM passengers', get_db_url('titanic_db'))



# get iris data 
def get_iris_data():
    sql_query = """
    SELECT species_id,
    species_name,
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
    FROM measurements
    JOIN species
    USING(species_id)
    """
    return pd.read_sql(sql_query, get_db_url('iris_db'))

