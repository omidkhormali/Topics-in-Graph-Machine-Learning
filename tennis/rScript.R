install.packages("tidyverse")
library("tidyverse")

data = read_csv("data/atp_tennis.csv")
# letters = c('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

# Separates the Date into Year, Month, and Day
data = separate_wider_delim(data, Date, "-", names=c('Year', 'Month', 'Day'))
data$Player_1 = str_replace(data$Player_1, " ", '_')
data$Player_2 = str_replace(data$Player_2, " ", '_')
data$Winner = str_replace(data$Winner, " ", '_')
data = sort_by(data, data$Year)

# For Match Info
write_csv(as.data.frame(data), file="data/atp_no_spaces.csv")

# Makes each set it's own observation and separates the game score into
# two columns- one for each player
data = separate_wider_delim(data, Score, " ", names=c('1', '2', '3', '4', '5'), too_few="align_start")
data = pivot_longer(data, cols=19:23, names_to="Set", values_to="Score", values_drop_na=T)
data = separate_wider_delim(data, Score, "-", names=c('Score_1', 'Score_2'))

# The Series names changed in 2009, so the following code changes
# old series names into their modern counterpart without breaking
# the already updated ones
data$Series = str_replace(data$Series, 'International Gold', 'ATP500')
data$Series = str_replace(data$Series, 'International', 'ATP250')
data$Series = str_replace(data$Series, 'Masters', 'Masters 1000')
data$Series = str_replace(data$Series, 'Masters 1000 1000', 'Masters 1000')
data$Series = str_replace(data$Series, 'Masters 1000 Cup', 'ATP Finals')

# For testing purposes
testData = filter(data, Year <= 2002)
write_csv(as.data.frame(testData), file="data/test_data_atp.csv")
