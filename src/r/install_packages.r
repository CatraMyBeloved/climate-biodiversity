# Install required packages
packages <- c(
  "tidyverse", "shiny", "shinydashboard", "sf", "terra",
  "raster", "DBI", "duckdb", "tidymodels", "caret",
  "randomForest", "gbm", "ranger", "ggplot2", "leaflet",
  "rmarkdown", "knitr", "testthat", "devtools", "reticulate",
  "tsibble", "fable", "feasts"
)

# Install packages not already installed
new_packages <- packages[!(packages %in% installed.packages()[, "Package"])]
if (length(new_packages)) install.packages(new_packages)

# Print confirmation
cat("Installed packages:\n")
print(packages)
