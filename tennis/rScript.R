install.packages("tidyverse")
library("tidyverse")

data = read_csv("tennis_data/atp_tennis.csv")

# Separates the Date into Year, Month, and Day
data = separate_wider_delim(data, Date, "-", names=c('Year', 'Month', 'Day'))

# Makes each set it's own observation and separates the game score into
# two columns- one for each player
data = separate_wider_delim(data, Score, " ", names=c('1', '2', '3', '4', '5'), too_few="align_start")
data = pivot_longer(data, cols=19:23, names_to="Set", values_to="Score", values_drop_na=T)
data = separate_wider_delim(data, Score, "-", names=c('Score_W', 'Score_L'))

# The Series names changed in 2009, so the following code changes
# old series names into their modern counterpart without breaking
# the already updated ones
data$Series = str_replace(data$Series, 'International Gold', 'ATP500')
data$Series = str_replace(data$Series, 'International', 'ATP250')
data$Series = str_replace(data$Series, 'Masters', 'Masters 1000')
data$Series = str_replace(data$Series, 'Masters 1000 1000', 'Masters 1000')
data$Series = str_replace(data$Series, 'Masters 1000 Cup', 'ATP Finals')

write_csv(as.data.frame(data), file="tennis_data/updated_atp.csv")

# For testing purposes
testData = filter(data, Year <= 2002)
write_csv(as.data.frame(testData), file="tennis_data/test_data_atp.csv")
