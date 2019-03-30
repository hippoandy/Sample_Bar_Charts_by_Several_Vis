library(shiny)

# global variables here
dat <- read.csv( "../food_rating.csv", header=TRUE, sep = ",", stringsAsFactors=TRUE )

# Define UI
ui <- fluidPage(

  # App title ----
  headerPanel( "Food Ratings" ),
  # Main panel for displaying outputs ----
  mainPanel( plotOutput( "bar" ) )
)

# Define server logic to plot various variables against mpg ----
server <- function( input, output )
{
  # Fill in the spot we created for a plot
  output$bar <- renderPlot(
  {
    # Render a barplot
    barplot( data.matrix( dat[, -1] ),
        main="Food Ratings",
        ylab="Average Rating",
        names.arg = dat$Country,
        beside=TRUE,
        las=2
    )
  })
}
shinyApp( ui, server )