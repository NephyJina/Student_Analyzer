import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def load_data(path):
    df = pd.read_csv(path)
    return df


def clean_data(df):
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove extra spaces
    df["name"] = df["name"].str.strip()
    df["subject"] = df["subject"].str.strip()

    # Convert marks to numbers
    df["mark1"] = pd.to_numeric(df["mark1"], errors="coerce")
    df["mark2"] = pd.to_numeric(df["mark2"], errors="coerce")
    df["mark3"] = pd.to_numeric(df["mark3"], errors="coerce")

    # Replace missing marks with median
    df["mark1"] = df["mark1"].fillna(df["mark1"].median())
    df["mark2"] = df["mark2"].fillna(df["mark2"].median())
    df["mark3"] = df["mark3"].fillna(df["mark3"].median())

    # Fix marks above 100
    df["mark1"] = df["mark1"].clip(0, 100)
    df["mark2"] = df["mark2"].clip(0, 100)
    df["mark3"] = df["mark3"].clip(0, 100)

    # Clean attendance
    df["attendance_pct"] = (
        df["attendance_pct"].astype(str).str.replace("%", ""))
    df["attendance_pct"] = pd.to_numeric(df["attendance_pct"], errors="coerce")

    # Fix attendance
    df["attendance_pct"] = df["attendance_pct"].clip(0, 100)
    df["attendance_pct"] = df["attendance_pct"].fillna(df["attendance_pct"].median())

    # Calculate total again
    df["total"] = df["mark1"] + df["mark2"] + df["mark3"]

    df.columns = df.columns.str.title()

    return df


def compute_metrics(df):
    df["Average"] = df["Total"] / 3
    df = df.sort_values("Average")

    df["Status"] = df[["Mark1", "Mark2", "Mark3"]].min(axis=1).apply(
        lambda x: "Pass" if x > 35 else "Fail"
    )

    df["Rank"] = df["Average"].rank(ascending=False)
    df["Average"] = df["Average"].clip(0, 100)

    df["At_risk"] = df.apply(
        lambda row: "Yes" if row["Average"] < 50 and row["Attendance_Pct"] < 75 else "No",
        axis=1
    )

    df = df.sort_values("Rank")
    return df


def build_summary(df):
    summary_df = df.groupby("Name").agg(
        Average_Marks=("Average", "mean"),
        Attendance_Pct=("Attendance_Pct", "mean")
    ).reset_index()

    summary = df[["Name", "Status", "Rank", "At_risk"]].copy()
    merged = summary_df.merge(summary)

    return merged, summary


def generate_charts(df):
    sns.histplot(df["Total"])
    plt.title("Total Marks of Students")
    plt.savefig("Total Marks of Students.png")
    plt.show()

    sns.scatterplot(x="Attendance_Pct", y="Total", data=df)
    plt.title("Total by Attendance_Pct")
    plt.savefig("Total by Attendance_Pct.png")
    plt.show()


def main():
    df = load_data("data.csv")
    df = clean_data(df)

    df.to_csv("cleaned_student_marks.csv", index=False)
    print("Data cleaned successfully!")
    print(df.head())

    df = compute_metrics(df)

    merged, summary = build_summary(df)
    print(merged)
    summary.to_csv("summary.csv", index=False)

    generate_charts(df)


if __name__ == "__main__":
    main()