import os
from .domain.Rater import Rater
from .repo import RatingManualRepository
from aspire.app.database.engine import ConnectionManager


def rate(rating_manual_id, rating_manual_repository, rating_inputs):
    rating_manual = rating_manual_repository.get(rating_manual_id)

    rater = Rater(rating_manual)
    rate_result = rater.rate(rating_inputs)

    return rate_result


def rate_from_csv(rating_manual_id, file_path):
    import csv

    if not os.path.isfile(file_path):
        raise Exception("Unable to locate input file")

    with open(file_path) as csv_file:
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]

    session = ConnectionManager().get_session()
    repository = RatingManualRepository.RatingManualRepository(session)

    if not rows or len(rows) == 0:
        raise Exception("No Data To Process!")

    keys = {}
    for i, row in enumerate(rows):
        print("Processing Row #" + str(i))
        row['rate'] = rate(rating_manual_id, repository, row.copy())
        print("Rate:" + row['rate'])
        if i == 1:
            keys = row.keys()

    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, keys)
        writer.writeheader()
        writer.writerows(rows)

    print("Done!")
