# noqa: INP001

import argparse
import sys

from sqla_training.app import create_session, populate, run_queries

parser = argparse.ArgumentParser()

if __name__ == "__main__":
    parser.add_argument(
        "-p", "--populate", help="Populate database with users", action="store_true"
    )
    args = parser.parse_args()

    session = create_session()
    if args.populate:
        populate(session=session)
        sys.exit(0)

    run_queries(session=session)
