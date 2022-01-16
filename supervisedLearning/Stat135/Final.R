## F- test
f1 <- c(38.7, 39.2, 40.1, 38.9)
f2 <- c(41.9, 42.3, 41.3, 41.5)
f3 <- c(40.8, 41.2, 39.5, 38.9)
SSb <- sum((f1-39.225)**2) + sum((f2-41.75)**2) + sum((f3-40.1)**2)
f_total <- c(f1, f2, f3)
mean_total <- mean(f_total)
SSw <- 4*(39.225-mean_total)**2 + 4*(41.75-mean_total)**2 + 4*(40.1-mean_total)**2
f <- (SSw/2)/(SSb/9)
p_value <- pf(f, df=2, df2=9, lower.tail = FALSE)

## Chi-Squared
p_value2 <- pchisq(0.029, df=1, lower.tail=FALSE)

R1<- c(732, 842, 736, 732, 833)
R2 <- c(869, 648, 1045, 674, 821)
R3 <- c(694, 748, 767, 712, 800)
p_1 <- t.test(R1, R3, paired=TRUE, alternative="greater")
p1_1 <- t.test(R1, R2, paired=TRUE, alternative="two.sided")
