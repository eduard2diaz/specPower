#install.packages("corrplot")
library(corrplot)

datos <- read.csv("../Data/specPowerDatamartTransform.csv")

matCorr <- cor(datos)

colnames(matCorr)[0:42] <- ""
rownames(matCorr)[0:42] <- ""

#corrplot(matCorr, method="color")
corrplot(matCorr, method="circle")

#true correlacion, false covarianzas
datos.acp <- prcomp(datos, scale = TRUE)

summary(datos.acp)
plot(datos.acp, type = "lines")

biplot(datos.acp, col=c("gray", "red"))

