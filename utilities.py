# additional functions for working with data


def save_dataset(data, directory):
    data.repartition(1).write.option("header", True).csv(directory, sep=";")
