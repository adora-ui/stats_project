import pandas as pd
import matplotlib.pyplot as plt

# Function to read survey data from CSV

def read_survey_data(file_path):
    return pd.read_csv(file_path)

# Function to generate survey responses chart

def plot_survey_responses(data):
    plt.figure(figsize=(10, 6), dpi=300)
    plt.plot(data['Year'], data['Great deal'], label='Great deal', marker='o')
    plt.plot(data['Year'], data['Fair amount'], label='Fair amount', marker='o')
    plt.plot(data['Year'], data['Only a little'], label='Only a little', marker='o')
    plt.plot(data['Year'], data['Not at all'], label='Not at all', marker='o')
    plt.plot(data['Year'], data['No opinion'], label='No opinion', marker='o')
    plt.title('Survey Responses (2001-2025)', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Responses (%)', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.gca().set_facecolor('white')
    plt.tight_layout()
    plt.savefig('survey_responses.png', dpi=300)
    plt.close()

# Function to generate opinion ratings chart

def plot_opinion_ratings(data):
    plt.figure(figsize=(10, 6), dpi=300)
    plt.plot(data['Year'], data['Excellent'], label='Excellent', marker='o')
    plt.plot(data['Year'], data['Good'], label='Good', marker='o')
    plt.plot(data['Year'], data['Only fair'], label='Only fair', marker='o')
    plt.plot(data['Year'], data['Poor'], label='Poor', marker='o')
    plt.plot(data['Year'], data['No opinion'], label='No opinion', marker='o')
    plt.title('Opinion Ratings (2001-2025)', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Ratings (%)', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.gca().set_facecolor('white')
    plt.tight_layout()
    plt.savefig('opinion_ratings.png', dpi=300)
    plt.close()

# Function to generate Environment vs Economic Growth Priority chart

def plot_growth_priority(data):
    plt.figure(figsize=(10, 6), dpi=300)
    plt.plot(data['Year'], data['Environment'], label='Environment', marker='o')
    plt.plot(data['Year'], data['Economic Growth'], label='Economic Growth', marker='o')
    plt.title('Environment vs Economic Growth Priority (1984-2025)', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Priority (%)', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.gca().set_facecolor('white')
    plt.tight_layout()
    plt.savefig('growth_priority.png', dpi=300)
    plt.close()

# Function to generate approval ratings chart

def plot_approval_ratings(data):
    plt.figure(figsize=(10, 6), dpi=300)
    plt.plot(data['Year'], data['Approval'], label='Approval Ratings', marker='o')
    plt.title('Approval Ratings (1992-2025)', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Approval (%)', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.gca().set_facecolor('white')
    plt.tight_layout()
    plt.savefig('approval_ratings.png', dpi=300)
    plt.close()

# Main function to call all plotting functions

def main():
    # Assuming CSV files are saved as 'survey_data.csv', 'opinion_data.csv', 'growth_data.csv', 'approval_data.csv'
    survey_data = read_survey_data('survey_data.csv')
    opinion_data = read_survey_data('opinion_data.csv')
    growth_data = read_survey_data('growth_data.csv')
    approval_data = read_survey_data('approval_data.csv')

    plot_survey_responses(survey_data)
    plot_opinion_ratings(opinion_data)
    plot_growth_priority(growth_data)
    plot_approval_ratings(approval_data)

if __name__ == '__main__':
    main()
