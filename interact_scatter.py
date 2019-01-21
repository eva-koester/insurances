## project: interactive scatter plot (insured persons vs. compaints, slider per year)
import cleaning
from bokeh.layouts import widgetbox, row
from bokeh.models import HoverTool, ColumnDataSource, Slider
from bokeh.plotting import figure
from bokeh.io import curdoc

# load the cleaned dataframe and reset its index
df = cleaning.load_clean_data()
df = df.set_index(['Jahr'])

#Make the ColumnDataSource: source
source = ColumnDataSource(data={'x': df.loc[2002].Versicherte,
                                'y': df.loc[2002].Beschwerden,
                                'name': df.loc[2002].Name})

# Save the minimum and maximum values of the insured persons and compaints columns
xmin, xmax = min(df.Versicherte), max(df.Versicherte)
ymin, ymax = min(df.Beschwerden), max(df.Beschwerden)

# Create the figure: plot
plot = figure(title='relationship between no of insured persons and no of complaints', x_axis_label='complaints', y_axis_label='insured persons',
              plot_height = 400, plot_width = 700, x_range=(xmin, xmax), y_range=(ymin, ymax))

# Add a circle glyph to the figure p
plot.circle(x='x', y='y', fill_alpha=0.5, color='firebrick', size=8, source=source)

# Define the callback function: update_plot
def update_plot(attr, old, new):
    '''update slider value based on year'''
    yr = slider.value
    new_data = {'x': df.loc[yr].Versicherte,
                'y': df.loc[yr].Beschwerden,
                'name': df.loc[yr].Name}
    source.data = new_data
    plot.title.text = 'Insurance data for %d' % yr

# Make a slider object and attach it to the 'value' property of slider
slider = Slider(start=2002, end=2017, step=1, value=2002, title='Jahr')
slider.on_change('value', update_plot)

# Create a HoverTool and add it to the plot
hover = HoverTool(tooltips=[('name', '@name')])
plot.add_tools(hover)

# Make a row layout of widgetbox(slider) and plot and add it to the current document
layout = row(widgetbox(slider), plot)
curdoc().add_root(layout)
