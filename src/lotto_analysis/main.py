import lotto_analysis.process as process

if __name__ == "__main__":
    data_path = "Mega-Millions-Winning-Numbers.csv"
    df = process.read_csv(data_path)
