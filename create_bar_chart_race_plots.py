import plotly.express as px
from create_bar_chart_race_data import CreateBarChartRaceData
import pandas as pd
from raceplotly.plots import barplot

create_bar_chart_race_data = CreateBarChartRaceData()
cumulative_votes_by_time_candidate = create_bar_chart_race_data.create_cumulative_votes_by_time_candidate()
covid_19_confirmed = create_bar_chart_race_data.create_covid_19_confirmed()

early_collected = cumulative_votes_by_time_candidate[cumulative_votes_by_time_candidate["collected_at"] < pd.to_datetime("2024-01-13 17:30:00")]
max_cumulative_votes = early_collected["cumulative_sum_votes"].max()

candidate_colors = {
    '賴清德/蕭美琴': 'rgb(27, 148, 49, 1)',
    '侯友宜/趙少康': 'rgb(0, 0, 149)',
    '柯文哲/吳欣盈': 'rgb(40, 200, 200)'}

"""
fig = px.bar(early_collected,
             x="cumulative_sum_votes", y="candidate", color="candidate",
             animation_frame="collected_at", animation_group="candidate",
             range_x=[0, max_cumulative_votes])
fig.show()

max_confirmed = covid_19_confirmed["confirmed"].max()
fig = px.bar(covid_19_confirmed,
             x="confirmed", y="country", color="country", 
             animation_frame="reported_on", animation_group="country",
             range_x=[0, max_confirmed])
fig.update_yaxes(categoryorder="total ascending")
fig.show()
"""

# Draw candidate bar chart by using race plotly
vote_raceplot = barplot(early_collected, item_column="candidate", value_column="cumulative_sum_votes",
                        time_column="collected_at", top_entries=3)
fig = vote_raceplot.plot(item_label = "Votes collected by candidate", value_label="Number of votes",
                         frame_duration=50)
fig.write_html("bar_chart_race_votes.html")

# Draw covid bar chart by race plotly
confirmed_raceplot = barplot(covid_19_confirmed, item_column="country", value_column="confirmed",
                             time_column="reported_on")
fig = confirmed_raceplot.plot(item_label = "Confirmed by country", value_label="Number of cases",
                              frame_duration=50)
fig.write_html("bar_chart_race_confirmed.html")