from sql_data.db import Base, engine
from sql_data.Models.movies import *


def main():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
