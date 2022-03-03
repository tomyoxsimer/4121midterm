import pandas as pd
import numpy as np
import pandas_bokeh as pb
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
import streamlit as st

pb.output_notebook()


df = pd.read_csv("hotel_bookings.csv")



pb.output_notebook()




#NCchart = NCdf.plot_bokeh(kind='bar', x='RegionName', y=['2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12', '2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06', '2021-07', '2021-08', '2021-09', '2021-10'], xlabel = 'City', ylabel = 'Rent Price', title = 'Rent Prices by Month in North Carolina')
#st.bokeh_chart(NCchart, use_container_width=True)


# Create and load Pie graph
d = {'col1': ['Resort Hotels', 'City Hotels'], 'col2': [40060, 79330]}

hotel_df = pd.DataFrame(data=d)

hotel_pie = hotel_df.plot_bokeh.pie(x="col1", y="col2", title="Types of Hotels Booked")

st.bokeh_chart(hotel_pie, use_container_width=True)

# Create and load line chart
d = {'col1': ['July', 'August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June'], 'col2': [12661, 13877, 10508, 11160, 6794, 6780, 5929, 8068, 9794, 11089, 11791, 10939]}

d = {'col1': ['July', 'August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June'], 'Bookings': [12661, 13877, 10508, 11160, 6794, 6780, 5929, 8068, 9794, 11089, 11791, 10939]}
bookings_df = pd.DataFrame(data=d)

booking_line = bookings_df.plot_bokeh.line(x='col1', y='Bookings', title="Bookings Over Months", xlabel ="Month", ylabel ="Bookings")

st.bokeh_chart(booking_line, use_container_width=True)

# Create and load bar chart

d = {'Year': [2015, 2016, 2017], 'Not Canceled':[13854, 36370, 24942], 'Canceled': [8142, 20337, 15745]}
canned_df = pd.DataFrame(data=d).set_index("Year")

canned_bar = canned_df.plot_bokeh.bar(title="Cancellations vs Non Cancellations by Year")

st.bokeh_chart(canned_bar, use_container_width=True)

