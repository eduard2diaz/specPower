#library(ggplot2)
datos <- read.csv("../Data/specPowerDatamartTransform.csv")
mat_corr <- cor(datos)
mat_cov <- cov(datos)
#plot(mat_corr['Nodes.'])
attach(datos)
names(datos)
#datos[2]
#pairs(datos)
write.csv(datos, file = "Preprocessing/Ejemplo1.csv", row.names = FALSE)
write.csv(mat_corr, file = "Preprocessing/MatCorrelacionR.csv", row.names = FALSE)
write.csv(mat_cov, file = "Preprocessing/MatCovarianzaR.csv", row.names = FALSE)