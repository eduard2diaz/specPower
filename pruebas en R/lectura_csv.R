#library(ggplot2)

datos <- read.csv("specNormalizado.csv")

mat_corr <- cor(datos)
mat_cov <- cov(datos)

#plot(mat_corr['Nodes.'])

attach(datos)
names(datos)
#datos[2]

#pairs(datos)



write.csv(datos, file = "Ejemplo1.csv", row.names = FALSE)
write.csv(mat_corr, file = "MatCorrelacionR.csv", row.names = FALSE)
write.csv(mat_cov, file = "MatCovarianzaR.csv", row.names = FALSE)

