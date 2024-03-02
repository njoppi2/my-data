import plotly.graph_objs as go
import pandas as pd

# Read data from CSV file
df = pd.read_csv('crepioca.csv', delimiter=';')

# Extract data for plotting
x_data = df.iloc[:, 0]
y_data = df.iloc[:, 1]
z_data = df.iloc[:, 2]
logs = df.iloc[:, 3]

# Normalize data for coloring
normalized_x = (x_data - x_data.min()) / (x_data.max() - x_data.min())
normalized_y = (y_data - y_data.min()) / (y_data.max() - y_data.min())
normalized_z = (z_data - z_data.min()) / (z_data.max() - z_data.min())

# Define colors based on RGB values
colors = [(r, g, b) for r, g, b in zip(normalized_x, normalized_y, normalized_z)]

# Create the scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=x_data,
    y=y_data,
    z=z_data,
    mode='markers',
    marker=dict(
        size=8,
        color=colors,  # Use combined scalar values for color mapping
        opacity=0.8,
        line=dict(
            color='rgba(0,0,0,0.5)',  # Set the border color
            width=1  # Set the border width
        )
    )
)])

# Add interactivity (display message on click)
fig.update_traces(hoverinfo='text',
                  hovertext=df.iloc[:, 3])  # Assuming the message is in the 5th column


# Set layout
fig.update_layout(scene=dict(
    xaxis_title='Banana',
    yaxis_title='Ovo',
    zaxis_title='Tapioca'
))

# Show the plot
fig.show()
