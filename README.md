goodreads_avg_rate_df <- goodreads_df |>
  filter(ratings_count >= 100) |>
  group_by(author) |>
  mutate(n_qualifying_books = n()) |>
  ungroup() |>
  filter(n_qualifying_books >= 3) |>
  group_by(author) |>
  summarise(average_author_rating = mean(average_rating, na.rm = TRUE),
            n_books = n()) |>
  ungroup() |>
  arrange(desc(average_author_rating))