install.packages("tidyverse")
library("tidyverse")
library("tidyr")

data = read_csv("atp_tennis.csv")
data = separate_wider_delim(data, Date, "-", names=c('Year', 'Month', 'Day'))
data = separate_wider_delim(data, Score, " ", names=c('1', '2', '3', '4', '5'), too_few="align_start")
data = pivot_longer(data, cols=19:23, names_to="Set", values_to="Score", values_drop_na=T)
data = separate_wider_delim(data, Score, "-", names=c('Score_W', 'Score_L'))
data = as.data.frame(data)
                
write_csv(as.data.frame(data), file="updated_atp.csv")
