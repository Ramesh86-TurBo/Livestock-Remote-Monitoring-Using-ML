import pandas as pd

# Specify your input and output file names
input_file = "mark2.csv"
output_file1 = "your_output_file1.csv"
# output_file2 = "your_output_file2.csv"

# creating first csv file

# Specify the columns of interest
columns_of_interest = ['time_stamp', 'sitting', 'standing', 'walking', 'grazing']

# Read the CSV file with the correct delimiter and only select columns of interest
df = pd.read_csv(input_file, parse_dates=['time_stamp'], usecols=columns_of_interest)

# Convert 'time_stamp' to datetime
df['time_stamp'] = pd.to_datetime(df['time_stamp'])

# Create a new DataFrame with the extended time
extended_time = pd.date_range(start=df['time_stamp'].min(), end=df['time_stamp'].max(), freq='S')
extended_df = pd.DataFrame({'time_stamp': extended_time})

# Merge the original DataFrame with the extended time DataFrame
df_extended = pd.merge(extended_df, df, on='time_stamp', how='left')

# Fill missing values with the previous values
df_extended = df_extended.ffill()

# Save the extended DataFrame to a new CSV file
df_extended.to_csv(output_file1, index=False)

# # creating second csv file

# # Read the CSV file into a DataFrame
# df2 = pd.read_csv('mark2.csv')

# # Define the columns for 'x', 'y', and 'z'
# x_columns = ['x_0', 'x_29', 'x_59', 'x_89', 'x_119', 'x_149', 'x_179', 'x_209', 'x_239', 'x_269']
# y_columns = ['y_0', 'y_29', 'y_59', 'y_89', 'y_119', 'y_149', 'y_179', 'y_209', 'y_239', 'y_269']
# z_columns = ['z_0', 'z_29', 'z_59', 'z_89', 'z_119', 'z_149', 'z_179', 'z_209', 'z_239', 'z_269']

# # Use the melt function to reshape the DataFrame for 'x'
# melted_x_df = pd.melt(df2, value_vars=x_columns, value_name='x_value')

# # Use the melt function to reshape the DataFrame for 'y'
# melted_y_df = pd.melt(df2, value_vars=y_columns, value_name='y_value')

# # Use the melt function to reshape the DataFrame for 'z'
# melted_z_df = pd.melt(df2, value_vars=z_columns, value_name='z_value')

# # Merge the three reshaped DataFrames on the common index
# result_df = melted_x_df.merge(melted_y_df, left_index=True, right_index=True).merge(melted_z_df, left_index=True, right_index=True)

# # Extract 'time_stamp' column from the original DataFrame
# result_df['time_stamp'] = pd.to_datetime(df['time_stamp'])

# # Drop unnecessary columns
# result_df = result_df[['time_stamp', 'x_value', 'y_value', 'z_value']]

# # Generate the extended time
# extended_time = pd.date_range(start=result_df['time_stamp'].min(), end=result_df['time_stamp'].max(), freq='S')

# # Create a DataFrame with the extended time
# extended_df = pd.DataFrame({'time_stamp': extended_time})

# # Merge using 'time_stamp' column
# final_df = pd.merge(extended_df, result_df, on='time_stamp', how='left')

# # Forward fill missing values
# final_df = final_df.ffill()

# # Save the final reshaped DataFrame to a new CSV file
# final_df.to_csv(output_file2, index=False)


# # add two csv files

# # Read the CSV files with the correct delimiter
# df3 = pd.read_csv(output_file1, parse_dates=['time_stamp'])
# df4 = pd.read_csv(output_file2, parse_dates=['time_stamp'])

# # Merge the two DataFrames on 'time_stamp' using outer join
# merged_df = pd.merge(df3, df4, on='time_stamp', how='outer')

# # Forward fill missing values
# merged_df = merged_df.ffill()

# # Save the merged DataFrame to a new CSV file
# merged_df.to_csv("final_output_file.csv", index=False)





