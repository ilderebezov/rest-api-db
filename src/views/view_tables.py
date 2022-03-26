import pandas
from sql import client


def tables_out():

    users_df = pandas.read_sql_table('users', client)
    events_df = pandas.read_sql_table('events', client)
    tariffs_df = pandas.read_sql_table('tariffs', client)
    out = 'Table: users' + '\n' * 2 + users_df.to_string() + '\n' * 2  \
          + 'Table: events' + '\n' * 2 + events_df.to_string() + '\n' * 2 \
          + 'Table: tariffs' + '\n' * 2 + tariffs_df.to_string() + '\n'
    return out
