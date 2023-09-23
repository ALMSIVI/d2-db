import csv
from pathlib import Path

from sqlalchemy import create_engine

from d2_db.dependency import create_dependency
from d2_db.services.__base__ import BaseService


def init_db():
    return create_engine('sqlite:///d2.db', echo=True)


def save(txt_path: Path, service: BaseService):
    dtos = []
    with txt_path.open() as f:
        reader = csv.DictReader(f, delimiter='\t')
        index = 0
        for row in reader:
            dtos.append(service.dto_from_txt(row, index))
            index += 1

    service.create_table()
    service.save_all(dtos)


if __name__ == '__main__':
    # TODO: add config to delete db file and specify db filename
    engine = init_db()
    for service_cls in create_dependency():
        # TODO: dynamic txt directory
        save(Path('txt') / service_cls.__txt__, service_cls(engine))
