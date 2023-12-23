# import pandas as pd

# # Read the CSV file into a DataFrame
# df = pd.read_csv('your_file.csv')

# # Define the columns for 'x', 'y', and 'z'
# x_columns = ['x_0', 'x_29', 'x_59', 'x_89', 'x_119', 'x_149', 'x_179', 'x_209', 'x_239', 'x_269']
# y_columns = ['y_0', 'y_29', 'y_59', 'y_89', 'y_119', 'y_149', 'y_179', 'y_209', 'y_239', 'y_269']
# z_columns = ['z_0', 'z_29', 'z_59', 'z_89', 'z_119', 'z_149', 'z_179', 'z_209', 'z_239', 'z_269']

# # Use the melt function to reshape the DataFrame for 'x'
# melted_x_df = pd.melt(df, value_vars=x_columns, value_name='x_value')

# # Use the melt function to reshape the DataFrame for 'y'
# melted_y_df = pd.melt(df, value_vars=y_columns, value_name='y_value')

# # Use the melt function to reshape the DataFrame for 'z'
# melted_z_df = pd.melt(df, value_vars=z_columns, value_name='z_value')

# # Merge the three reshaped DataFrames on the common index
# result_df = melted_x_df.merge(melted_y_df, left_index=True, right_index=True).merge(melted_z_df, left_index=True, right_index=True)

# # Drop unnecessary columns
# result_df = result_df[['x_value', 'y_value', 'z_value']]

# # Save the final reshaped DataFrame to a new CSV file
# result_df.to_csv('reshaped_file.csv', index=False)


# ?????????????????????????????????????????????????????????????????????

