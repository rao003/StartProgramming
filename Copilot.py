import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load data from an Excel file."""
    return pd.read_excel(file_path)

def basic_statistics(df):
    """Print basic statistics of the dataframe."""
    print("Basic Statistics:")
    print(df.describe())
    print("\nMissing Values:")
    print(df.isnull().sum())

def generate_visualizations(df):
    """Generate common visualizations."""
    # Histogram for each numeric column
    df.hist(figsize=(10, 10))
    plt.suptitle('Histograms')
    plt.show()

    # Correlation heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

    # Pairplot
    sns.pairplot(df)
    plt.suptitle('Pairplot', y=1.02)
    plt.show()

def main(file_path):
    df = load_data(file_path)
    basic_statistics(df)
    generate_visualizations(df)

if __name__ == "__main__":
    file_path = input("Enter the path to your Excel file: ")
    main(file_path)