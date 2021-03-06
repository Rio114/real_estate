import luigi

from tasks.get_candles import GetCandles  # noqa
from tasks.preprocess_candles import PreprocessCandles  # noqa


def main():
    luigi.run(["PreprocessCandles", "--local-scheduler"])


if __name__ == "__main__":
    main()
