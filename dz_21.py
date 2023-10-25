import csv
import json


class CsvFileHandler:
    def read_file(self, filepath, as_dict=False):
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            if as_dict:
                data = [dict(zip(next(reader), row)) for row in reader]
            else:
                data = [row for row in reader]
        return data

    def write_file(self, filepath, data, as_dict=False):
        with open(filepath, 'w') as file:
            writer = csv.writer(file)
            if as_dict:
                headers = list(data[0].keys())
                writer.writerow(headers)
                for row in data:
                    writer.writerow(row.values())
            else:
                for row in data:
                    writer.writerow(row)

    def append_file(self, filepath, data, as_dict=False):
        with open(filepath, 'a') as file:
            writer = csv.writer(file)
            if as_dict:
                headers = list(data[0].keys())
                writer.writerow(headers)
                for row in data:
                    writer.writerow(row.values())
            else:
                for row in data:
                    writer.writerow(row)


class JsonFileHandler:
    def read_file(self, filepath, as_dict=False):
        with open(filepath, 'r') as file:
            data = json.load(file)
            if as_dict:
                data = [dict(row) for row in data]
        return data

    def write_file(self, filepath, data, as_dict=False):
        with open(filepath, 'w') as file:
            if as_dict:
                json.dump(data, file, indent=4)
            else:
                json.dump([list(row.values()) for row in data], file, indent=4)

    def append_file(self, filepath, data):
        raise TypeError("This file type does not support appending data")


class TxtFileHandler:
    def read_file(self, filepath):
        with open(filepath, 'r') as file:
            data = file.readlines()
        return data

    def write_file(self, filepath, data):
        with open(filepath, 'w') as file:
            file.writelines(data)

    def append_file(self, filepath, data):
        with open(filepath, 'a') as file:
            file.writelines(data)
