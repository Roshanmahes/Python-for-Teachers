library(readr)
library(nnet)
library(MASS)
library(caret)


main <- function() {
  
  header <- c("sepal_length", "sepal_width", "petal_length", "petal_width", "class")
  iris <- read.csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
  names(iris) <- header
  sample <- sample.int(n = nrow(iris), size = floor(.8 * nrow(iris)), replace=F)
  train <- iris[sample, ]
  test  <- iris[-sample, ]
  
  # logistic regression
  lr <- multinom(class ~ ., data = train, trace = F)
  
  # linear discriminant analysis
  lda_model <- lda(class ~ ., data = train)
  
  # KNN
  man_grid <- expand.grid(k = c(1:10))
  ctrl <- trainControl(method="cv", number = 5)
  knn <- train(class ~ ., data = train, method = "knn", trControl = ctrl, tuneGrid = man_grid)
  
  # SVM
  man_grid <- expand.grid(cost = c(1:10))
  ctrl <- trainControl(method="cv", number = 5)
  svm <- train(class ~ ., data = train, method = "svmLinear2", trControl = ctrl, tuneGrid = man_grid)
  
  # Evaluate
  lr_accuracy <- sum(predict(lr, test) == test$class) / nrow(test)
  lda_accuracy <- sum(predict(lda_model, test)$class == test$class) / nrow(test)
  knn_accuracy <- sum(predict(knn, test) == test$class) / nrow(test)
  svm_accuracy <- sum(predict(svm, test) == test$class) / nrow(test)
  
  # print(paste(lr_accuracy, ",", lda_accuracy, ",", knn_accuracy, ",", svm_accuracy))
}


now <- Sys.time()
for (i in c(1:5)) {
  main()
}
print(Sys.time() - now)


a = 2
b <- 2
b
