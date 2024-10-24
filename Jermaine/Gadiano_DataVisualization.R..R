#load the built in dataset
country_data <- read.csv("C:/Users/Mj Tabasa/Downloads/Gadiano_Data_Visualization 2.csv")

country_data_gold <-country_data[1:10,]
barplot(country_data_gold$Gold,
     xlab = "GOLD",
     ylab = "Frequency",
     main = "Bar Chart Country Gold Medals",
     horiz = TRUE,
     col = rainbow(10))

country_data_gold <-country_data[1:35,]
barplot(country_data_gold$Gold,
        xlab = "GOLD",
        ylab = "Frequency",
        main = "Histogram Country Gold Medals",
        col = rainbow(10))