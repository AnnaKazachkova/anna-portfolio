# EV adoption forecast with an uncertainty band (Monte Carlo).
# Historical values are used as-is; for each projection year, the APS and
# STEPS scenario values are averaged (mean) and their gap sets the spread.
# Output: ev_mc_percentiles.csv (P5 / P50 / P95 per region and year),
# which feeds the Tableau "50th percentile" forecast chart.

REGIONS <- list(
  World = list(
    hist  = c(`2020` = 4.2, `2021` = 8.9, `2022` = 14, `2023` = 18),
    aps   = c(`2025` = 26, `2030` = 48, `2035` = 68),
    steps = c(`2025` = 25, `2030` = 44, `2035` = 55)
  ),
  China = list(
    hist  = c(`2020` = 5.7, `2021` = 16, `2022` = 29, `2023` = 38),
    aps   = c(`2025` = 49, `2030` = 68, `2035` = 85),
    steps = c(`2025` = 49, `2030` = 68, `2035` = 85)
  ),
  Europe = list(
    hist  = c(`2020` = 10, `2021` = 17, `2022` = 20, `2023` = 21),
    aps   = c(`2025` = 31, `2030` = 62, `2035` = 92),
    steps = c(`2025` = 31, `2030` = 60, `2035` = 87)
  ),
  USA = list(
    hist  = c(`2020` = 2.3, `2021` = 4.7, `2022` = 7.4, `2023` = 9.5),
    aps   = c(`2025` = 20, `2030` = 55, `2035` = 71),
    steps = c(`2025` = 20, `2030` = 55, `2035` = 71)
  )
)

set.seed(42)
N <- 5000
rows <- list()

for (region in names(REGIONS)) {
  d <- REGIONS[[region]]

  # Historical rows - no uncertainty
  for (year in names(d$hist)) {
    val <- d$hist[[year]]
    rows[[length(rows) + 1]] <- data.frame(
      Region = region, Year = as.integer(year), Type = "Historical",
      P5 = val, P50 = val, P95 = val, APS = val, STEPS = val
    )
  }

  # Projection rows - simulate
  proj_years <- sort(as.integer(names(d$aps)))
  for (year in proj_years) {
    year_chr <- as.character(year)
    mu    <- (d$aps[[year_chr]] + d$steps[[year_chr]]) / 2
    gap   <- abs(d$aps[[year_chr]] - d$steps[[year_chr]])
    sigma <- max(gap / 2, 2)  # volatility scales with scenario spread

    samples <- rnorm(N, mean = mu, sd = sigma)
    samples <- pmin(pmax(samples, 0), 100)

    rows[[length(rows) + 1]] <- data.frame(
      Region = region, Year = year, Type = "Projection",
      P5  = as.numeric(quantile(samples, 0.05)),
      P50 = as.numeric(quantile(samples, 0.50)),
      P95 = as.numeric(quantile(samples, 0.95)),
      APS = d$aps[[year_chr]], STEPS = d$steps[[year_chr]]
    )
  }
}

df <- do.call(rbind, rows)
write.csv(df, "ev_mc_percentiles.csv", row.names = FALSE)
