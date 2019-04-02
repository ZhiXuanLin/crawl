library(rvest)
library(dplyr)
article_detail <- function(url){
  raw_html <- read_html(url)
  
  author <- ".article-metaline:nth-child(1) .article-meta-value"
  title <- ".article-metaline:nth-child(3) .article-meta-value"
  time <- ".article-metaline:nth-child(4)  .article-meta-value"
  main_content <- "#main-content"
  ip <- ".hl+ .f2"
  push <- ".push-tag"
  push_id <- ".push-userid"
  push_content <- ".push-content"
  push_time <- ".push-ipdatetime"
  
  article_detail_info <- list()
  columns <- c(author, title, time, main_content, ip, push, push_id, push_content, push_time)
  for (i in 1:length(columns)){
    article_content <- raw_html %>%
      html_nodes(css = columns[i]) %>%
      html_text()
    article_detail_info[[i]] <- article_content
  }
  names(article_detail_info) <- c("author", "title", "time", "main_content", "ip", "push", "push_id", "push_content", "push_time")
  return(article_detail_info)
}

article_url <- "https://www.ptt.cc/bbs/NBA/M.1553160476.A.E4B.html"
nba_article_details <- article_detail(article_url)
nba_article_details$author
nba_article_details$title


