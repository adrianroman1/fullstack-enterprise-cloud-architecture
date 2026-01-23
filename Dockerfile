# Stage 1: Build
FROM maven:3.9.6-eclipse-temurin-21-alpine AS build
COPY . /app
WORKDIR /app
RUN mvn clean package -DskipTests

# Stage 2: Runtime
FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar

# Securitate: Rulăm aplicația ca utilizator non-root (Standard 2026)
RUN addgroup -S spring && adduser -S spring -G spring
USER spring:spring

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
